from datetime import date
from unittest import TestCase
from unittest.mock import Mock, patch

from src.bright_helper import BrightHelper
from src.common import DayOfWeek, MealType, FoodType, Gender
from src.meal_planner import MealPlanner


class TestMealPlanner(TestCase):
    def setUp(self):
        self._male_weight_loss_helper = BrightHelper.build_weight_loss_helper(Gender.MALE)
        date_patcher = patch('src.meal_planner.date')
        self.addCleanup(date_patcher.stop)
        self.mock_date = date_patcher.start()
        self.mock_date.today.return_value = date(2018, 8, 29)

    def test_meal_plan_length(self):
        """
        Given a meal plan for 2 days starting today
        When you ask for the length of the meal plan
        Then it returns 2
        """
        meal_planner = MealPlanner(self._male_weight_loss_helper, plan_length=2)
        self.assertEqual(2, meal_planner.plan_length)

    def test_get_empty_meal_plan(self):
        """
        Given a meal plan for 2 days starting today
          and today is Wednesday, Aug 29, 2018
        When you ask for the meal plan
        Then it returns Wednesday & Thursday with nothing in them
        """
        meal_planner = MealPlanner(self._male_weight_loss_helper, start_in_days=0, plan_length=2)
        expected = {
            DayOfWeek.WEDNESDAY: {},
            DayOfWeek.THURSDAY: {}
        }
        self.assertEqual(expected, meal_planner.get_current_plan())

    def test_get_empty_meal_plan_that_cycles_week(self):
        """
        Given a meal plan for 7 days from today
          and today is Wednesday, Aug 29, 2018
        When you ask for the meal plan
        Then it returns Wednesday through Tuesday with nothing in them
        """
        meal_planner = MealPlanner(self._male_weight_loss_helper, start_in_days=0, plan_length=7)
        expected = {
            DayOfWeek.WEDNESDAY: {},
            DayOfWeek.THURSDAY: {},
            DayOfWeek.FRIDAY: {},
            DayOfWeek.SATURDAY: {},
            DayOfWeek.SUNDAY: {},
            DayOfWeek.MONDAY: {},
            DayOfWeek.TUESDAY: {}
        }
        self.assertEqual(expected, meal_planner.get_current_plan())

    def test_get_meal_allowances_by_date(self):
        meal_planner = MealPlanner(self._male_weight_loss_helper, start_in_days=0, plan_length=2)
        actual = meal_planner.get_meal_allowances()
        expected = {
            DayOfWeek.WEDNESDAY: {
                MealType.BREAKFAST: {
                    FoodType.PROTEIN: 1.0,
                    FoodType.GRAIN: 1.0,
                    FoodType.FRUIT: 1.0
                },
                MealType.LUNCH: {
                    FoodType.PROTEIN: 1.0,
                    FoodType.VEGGIES: 1.0,
                    FoodType.FRUIT: 1.0,
                    FoodType.FAT: 1.0
                },
                MealType.DINNER: {
                    FoodType.PROTEIN: 1.0,
                    FoodType.VEGGIES: 1.0,
                    FoodType.SALAD: 1.0,
                    FoodType.FAT: 1.0
                }
            },
            DayOfWeek.THURSDAY: {
                MealType.BREAKFAST: {
                    FoodType.PROTEIN: 1.0,
                    FoodType.GRAIN: 1.0,
                    FoodType.FRUIT: 1.0
                },
                MealType.LUNCH: {
                    FoodType.PROTEIN: 1.0,
                    FoodType.VEGGIES: 1.0,
                    FoodType.FRUIT: 1.0,
                    FoodType.FAT: 1.0
                },
                MealType.DINNER: {
                    FoodType.PROTEIN: 1.0,
                    FoodType.VEGGIES: 1.0,
                    FoodType.SALAD: 1.0,
                    FoodType.FAT: 1.0
                }
            }
        }
        self.assertEqual(expected, actual)



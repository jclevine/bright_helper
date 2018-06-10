from datetime import date
from unittest import TestCase
from unittest.mock import Mock, patch

from src.bright_helper import BrightHelper
from src.common import DayOfWeek, MealType, FoodType, Gender, Food
from src.food_option import FoodOption
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
        """
        Given a 2-day meal plan for a weight losing male
         When you ask for all the meal allowances
         Then it returns all the allowances for both Wednesday & Thursday
        """
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

    def test_get_food_options_for_a_specific_day_for_a_specific_meal_type_and_food_type(self):
        """
        Given a 2-day meal plan for a weight losing male
         When you ask for the food options for a breakfast protein
         Then it returns all the possible protein options for 1 Breakfast Protein
        """
        meal_planner = MealPlanner(self._male_weight_loss_helper, plan_length=2)
        actual = meal_planner.get_food_options(DayOfWeek.WEDNESDAY, MealType.BREAKFAST, FoodType.PROTEIN)
        expected = {
            FoodOption(Food.MILK_NON_DAIRY, 8), FoodOption(Food.TOFU, 6),
            FoodOption(Food.TEMPEH, 6), FoodOption(Food.BEANS, 6),
            FoodOption(Food.BEANS_ROASTED, 3), FoodOption(Food.LENTILS, 6),
            FoodOption(Food.HUMMUS, 6), FoodOption(Food.SOYA_GRANULES, 3),
            FoodOption(Food.EDAMAME_SHELLED, 6), FoodOption(Food.NUTS, 2),
            FoodOption(Food.NUT_BUTTER, 2), FoodOption(Food.VEGGIE_BURGER, 6),
            FoodOption(Food.SEEDS, 2), FoodOption(Food.NUTS_SOY, 3),
            FoodOption(Food.EDAMAME_DRY_ROASTED, 3)
        }

        self.assertEqual(expected, actual)

    def test_choose_food(self):
        """
        Given a 2-day meal plan for a weight losing male
         When you choose 4oz of non-dairy milk for breakfast on Wednesday
          and you ask for food options for protein for breakfast on Wednesday
         Then it returns all the possible protein options for 0.5 Breakfast Protein (4oz of milk is 1/2 the allowance)
        """
        meal_planner = MealPlanner(self._male_weight_loss_helper, plan_length=2)
        meal_planner.choose_food(DayOfWeek.WEDNESDAY, MealType.BREAKFAST, Food.MILK_NON_DAIRY, 4)

        actual = meal_planner.get_food_options(DayOfWeek.WEDNESDAY, MealType.BREAKFAST, FoodType.PROTEIN)

        expected = {
            FoodOption(Food.MILK_NON_DAIRY, 4.0), FoodOption(Food.TOFU, 3.0),
            FoodOption(Food.TEMPEH, 3.0), FoodOption(Food.BEANS, 3.0),
            FoodOption(Food.BEANS_ROASTED, 1.5), FoodOption(Food.LENTILS, 3.0),
            FoodOption(Food.HUMMUS, 3.0), FoodOption(Food.SOYA_GRANULES, 1.5),
            FoodOption(Food.EDAMAME_SHELLED, 3.0), FoodOption(Food.NUTS, 1.0),
            FoodOption(Food.NUT_BUTTER, 1.0), FoodOption(Food.VEGGIE_BURGER, 3.0),
            FoodOption(Food.SEEDS, 1.0), FoodOption(Food.NUTS_SOY, 1.5),
            FoodOption(Food.EDAMAME_DRY_ROASTED, 1.5)
        }

        self.assertEqual(expected, actual)



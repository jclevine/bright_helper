from unittest import TestCase

from src.bright_helper import BrightHelper
from src.common import MealType, Food, FoodType, Gender, DayOfWeek
from src.food_option import FoodOption
from src.meal_planner import MealPlanner
from datetime import date
from unittest.mock import patch, Mock


class TestMealPlanUseCase(TestCase):

    @patch('src.meal_planner.date', return_value=Mock(side_effect=lambda *args, **kw: date(*args, **kw)))
    def test_use_case_2(self, mock_date):
        mock_date.today.return_value = date(2018, 8, 29)

        # 1. Create the meal planner for a 2-day male weight loss meal plan.
        meal_planner = MealPlanner(BrightHelper.build_weight_loss_helper(Gender.MALE), start_in_days=0, plan_length=2)

        # 2. If you get the details of your current plan, it's empty.
        current_plan = meal_planner.get_current_plan()
        expected = {
            DayOfWeek.WEDNESDAY: {},
            DayOfWeek.THURSDAY: {}
        }
        self.assertEqual(expected, current_plan)

        # 3. You ask for all the allowances you're allowed throughout your meal plan 2-day period.
        meal_allowances_by_day = meal_planner.get_meal_allowances()
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
        self.assertEqual(expected, meal_allowances_by_day)

        # 4. You ask for the food options for protein for Wednesday's breakfast.
        food_options = meal_planner.get_food_options(DayOfWeek.WEDNESDAY, MealType.BREAKFAST, FoodType.PROTEIN)
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
        self.assertEqual(expected, food_options)

        # 5. You choose 4oz of non-dairy milk for Wednesday.
        meal_planner.choose_food(DayOfWeek.WEDNESDAY, MealType.BREAKFAST, Food.MILK_NON_DAIRY, 4)

        # 6. You look at what options you have left for protein for Wednesday's breakfast.
        food_options = meal_planner.get_food_options(DayOfWeek.WEDNESDAY, MealType.BREAKFAST, FoodType.PROTEIN)
        expected = {
            FoodOption(Food.MILK_NON_DAIRY, 4.0), FoodOption(Food.TOFU, 3.0),
            FoodOption(Food.TEMPEH, 3.0), FoodOption(Food.BEANS, 3.0),
            FoodOption(Food.BEANS_ROASTED, 1.5), FoodOption(Food.LENTILS, 3.0),
            FoodOption(Food.HUMMUS, 3.0), FoodOption(Food.SOYA_GRANULES, 1.5),
            FoodOption(Food.EDAMAME_SHELLED, 3.0), FoodOption(Food.NUTS, 1),
            FoodOption(Food.NUT_BUTTER, 1.0), FoodOption(Food.VEGGIE_BURGER, 3),
            FoodOption(Food.SEEDS, 1.0), FoodOption(Food.NUTS_SOY, 1.5),
            FoodOption(Food.EDAMAME_DRY_ROASTED, 1.5)
        }
        self.assertEqual(expected, food_options)

        # 7. You choose 1oz of nut butter
        meal_planner.choose_food(DayOfWeek.WEDNESDAY, MealType.BREAKFAST, Food.NUT_BUTTER, 1)

        # 8. You look at what your meal plan allowances are for Wednesday breakfast
        meal_allowances = meal_planner.get_meal_allowances_by_day_and_meal(DayOfWeek.WEDNESDAY, MealType.BREAKFAST)
        self.assertEqual({
            FoodType.PROTEIN: 0.0,
            FoodType.GRAIN: 1.0,
            FoodType.FRUIT: 1.0
        }, meal_allowances)

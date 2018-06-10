from unittest import TestCase

from src.bright_helper import BrightHelper
from src.common import MealType, Food, FoodType, Gender, DayOfWeek
from src.food_option import FoodOption
from src.meal_planner import MealPlanner
from datetime import date
from unittest.mock import patch, Mock


class TestMealPlanUseCase(TestCase):

    @patch('src.meal_planner.date', return_value=Mock(side_effect=lambda *args, **kw: date(*args, **kw)))
    def test_use_case(self, mock_date):
        mock_date.today.return_value = date(2018, 8, 29)

        meal_planner = MealPlanner(BrightHelper.build_weight_loss_helper(Gender.MALE), start_in_days=0, plan_length=2)

        current_plan = meal_planner.get_current_plan()

        expected = {
            DayOfWeek.WEDNESDAY: {},
            DayOfWeek.THURSDAY: {}
        }
        self.assertEqual(expected, current_plan)

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
        # bright_helper.choose_food(MealType.BREAKFAST, Food.POTATO, 2)
        # actual = bright_helper.get_meal_allowances(MealType.BREAKFAST)
        # expected = {
        #     FoodType.GRAIN: 0.5,
        #     FoodType.PROTEIN: 1,
        #     FoodType.FRUIT: 1,
        # }
        # self.assertEqual(expected, actual)

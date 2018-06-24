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

        # Hello, are you male or female?
        # Male

        # In how many days would you like to start your meal plan?
        # 0 (Now)

        # How long would you like your meal plan to last?
        # 2 days

        # Are you losing weight or maintaining your weight?
        # Losing weight

        meal_planner = MealPlanner(BrightHelper.build_weight_loss_helper(Gender.MALE), start_in_days=0, plan_length=2)

        # Let's get to it!
        # Here are your allowances for your first day, Wednesday

        current_plan = meal_planner.get_meal_allowances_by_day(DayOfWeek.WEDNESDAY)
        expected = {
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
        self.assertEqual(expected, current_plan)


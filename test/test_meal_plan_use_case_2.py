from unittest import TestCase

from src.bright_helper import BrightHelper
from src.common import MealType, Food, FoodType, Gender, DayOfWeek
from src.food_option import FoodOption
from src.meal_planner import MealPlanner
from datetime import date
from unittest.mock import patch, Mock
from src.food_master import PyFoodMaster as FoodMaster


class TestMealPlanUseCase(TestCase):

    @patch('src.meal_planner.date', return_value=Mock(side_effect=lambda *args, **kw: date(*args, **kw)))
    def test_use_case_2(self, mock_date):
        mock_date.today.return_value = date(2018, 8, 29)

        # Hello, are you male or female?
        # > Male

        # In how many days would you like to start your meal plan?
        # > 0 (Now)

        # How long would you like your meal plan to last?
        # > 2 days

        # Are you losing weight or maintaining your weight?
        # > Losing weight

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

        # Let's start with breakfast. Here are your options for protein
        food_options = meal_planner.get_food_options(DayOfWeek.WEDNESDAY, MealType.BREAKFAST, FoodType.PROTEIN)
        self.assertEqual({
            FoodOption(Food.MILK_NON_DAIRY, 8), FoodOption(Food.TOFU, 6),
            FoodOption(Food.TEMPEH, 6), FoodOption(Food.BEANS, 6),
            FoodOption(Food.BEANS_ROASTED, 3), FoodOption(Food.LENTILS, 6),
            FoodOption(Food.HUMMUS, 6), FoodOption(Food.SOYA_GRANULES, 3),
            FoodOption(Food.EDAMAME_SHELLED, 6), FoodOption(Food.NUTS, 2),
            FoodOption(Food.NUT_BUTTER, 2), FoodOption(Food.VEGGIE_BURGER, 6),
            FoodOption(Food.SEEDS, 2), FoodOption(Food.NUTS_SOY, 3),
            FoodOption(Food.EDAMAME_DRY_ROASTED, 3)}, food_options)

        # What would you like?
        # > Milk, Non-Dairy

        # How many ounces?
        # > 4 oz

        # Would you like this for more than one day?
        # > Yes

        # Which days?
        # > All
        meal_planner.choose_food([DayOfWeek.WEDNESDAY, DayOfWeek.THURSDAY],
                                 MealType.BREAKFAST, Food.MILK_NON_DAIRY, 4.0)

        food_type = FoodMaster.get_food_type(Food.MILK_NON_DAIRY)
        self.assertEqual(FoodType.PROTEIN, food_type)

        has_more_protein_allowance = meal_planner.has_more_allowance(DayOfWeek.WEDNESDAY, MealType.BREAKFAST,
                                                                     FoodType.PROTEIN)
        self.assertEqual(True, has_more_protein_allowance)

        # Ok, you still have some protein allowance for Wednesday breakfast
        # Here are your options:
        food_options = meal_planner.get_food_options(DayOfWeek.WEDNESDAY, MealType.BREAKFAST, FoodType.PROTEIN)
        self.assertEqual({
            FoodOption(Food.MILK_NON_DAIRY, 4.0), FoodOption(Food.TOFU, 3.0),
            FoodOption(Food.TEMPEH, 3.0), FoodOption(Food.BEANS, 3.0),
            FoodOption(Food.BEANS_ROASTED, 1.5), FoodOption(Food.LENTILS, 3.0),
            FoodOption(Food.HUMMUS, 3.0), FoodOption(Food.SOYA_GRANULES, 1.5),
            FoodOption(Food.EDAMAME_SHELLED, 3.0), FoodOption(Food.NUTS, 1.0),
            FoodOption(Food.NUT_BUTTER, 1.0), FoodOption(Food.VEGGIE_BURGER, 3.0),
            FoodOption(Food.SEEDS, 1.0), FoodOption(Food.NUTS_SOY, 1.5),
            FoodOption(Food.EDAMAME_DRY_ROASTED, 1.5)}, food_options)

        # What would you like?
        # > Nut Butter

        # How many ounces?
        # > 1

        # Would you like this for more than one day?
        # > Yes

        # Which days?
        # > All
        meal_planner.choose_food([DayOfWeek.WEDNESDAY, DayOfWeek.THURSDAY], MealType.BREAKFAST, Food.NUT_BUTTER, 1.0)

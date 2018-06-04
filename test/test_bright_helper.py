from unittest import TestCase
from src.bright_helper import BrightHelper
from src.common import Gender, MealType, FoodType, Food
from src.food_option import FoodOption


class TestBrightHelper(TestCase):

    def test_how_much(self):
        bright_helper = BrightHelper.build_weight_loss_helper(Gender.MALE)
        actual = bright_helper.get_meal_type_options(MealType.BREAKFAST, FoodType.GRAIN)
        expected = {
            FoodOption(Food.POTATO, 4), FoodOption(Food.POTATO_SWEET, 4),
            FoodOption(Food.YAM, 4), FoodOption(Food.RICE, 4),
            FoodOption(Food.QUINOA, 4), FoodOption(Food.MILLET, 4),
            FoodOption(Food.OATMEAL, 1), FoodOption(Food.BRAN_OAT, 1),
            FoodOption(Food.CREAM_OF_RICE, 1), FoodOption(Food.GRITS, 1),
            FoodOption(Food.CREAM_OF_WHEAT, 1), FoodOption(Food.QUINOA_FLAKES, 1),
            FoodOption(Food.CEREAL, 1)
        }
        self.assertEqual(expected, actual)

    def test_how_much_after_choose(self):
        bright_helper = BrightHelper.build_weight_loss_helper(Gender.MALE)

        bright_helper.choose_food(MealType.BREAKFAST, Food.POTATO, 4)
        actual = bright_helper.get_meal_type_options(MealType.BREAKFAST, FoodType.GRAIN)
        expected = set()
        self.assertEqual(expected, actual)


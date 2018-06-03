from unittest import TestCase
from src.bright_helper import BrightHelper
from src.common import Gender, MealType, FoodType, Food
from src.food_option import FoodOption


class TestBrightHelper(TestCase):

    def setUp(self):
        self.bright_helper = BrightHelper.build_weight_loss_helper(Gender.MALE)

    # def test_male_weight_loss_meal_allowances(self):
    #     self.assertEqual(1, self.bright_helper.get_allowance(MealType.BREAKFAST, FoodType.PROTEIN))
    #     self.assertEqual(1, self.bright_helper.get_allowance(MealType.BREAKFAST, FoodType.GRAIN))
    #     self.assertEqual(1, self.bright_helper.get_allowance(MealType.BREAKFAST, FoodType.FRUIT))
    #     self.assertEqual(0, self.bright_helper.get_allowance(MealType.BREAKFAST, FoodType.VEGGIES))
    #     self.assertEqual(0, self.bright_helper.get_allowance(MealType.BREAKFAST, FoodType.FAT))
    #     self.assertEqual(0, self.bright_helper.get_allowance(MealType.BREAKFAST, FoodType.SALAD))
    #
    #     self.assertEqual(1, self.bright_helper.get_allowance(MealType.LUNCH, FoodType.PROTEIN))
    #     self.assertEqual(0, self.bright_helper.get_allowance(MealType.LUNCH, FoodType.GRAIN))
    #     self.assertEqual(1, self.bright_helper.get_allowance(MealType.LUNCH, FoodType.FRUIT))
    #     self.assertEqual(1, self.bright_helper.get_allowance(MealType.LUNCH, FoodType.VEGGIES))
    #     self.assertEqual(1, self.bright_helper.get_allowance(MealType.LUNCH, FoodType.FAT))
    #     self.assertEqual(0, self.bright_helper.get_allowance(MealType.LUNCH, FoodType.SALAD))
    #
    #     self.assertEqual(1, self.bright_helper.get_allowance(MealType.DINNER, FoodType.PROTEIN))
    #     self.assertEqual(0, self.bright_helper.get_allowance(MealType.DINNER, FoodType.GRAIN))
    #     self.assertEqual(0, self.bright_helper.get_allowance(MealType.DINNER, FoodType.FRUIT))
    #     self.assertEqual(1, self.bright_helper.get_allowance(MealType.DINNER, FoodType.VEGGIES))
    #     self.assertEqual(1, self.bright_helper.get_allowance(MealType.DINNER, FoodType.FAT))
    #     self.assertEqual(1, self.bright_helper.get_allowance(MealType.DINNER, FoodType.SALAD))
    pass

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



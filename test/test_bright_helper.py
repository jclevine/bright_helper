from unittest import TestCase
from src.bright_helper import BrightHelper
from src.common import Gender, MealType, FoodType


class TestBrightHelper(TestCase):

    def test(self):
        bright_helper = BrightHelper.build_weight_loss_helper(Gender.MALE)
        self.assertEqual(1, bright_helper.get_allowance(MealType.BREAKFAST, FoodType.PROTEIN))
        self.assertEqual(1, bright_helper.get_allowance(MealType.BREAKFAST, FoodType.GRAIN))
        self.assertEqual(1, bright_helper.get_allowance(MealType.BREAKFAST, FoodType.FRUIT))
        self.assertEqual(0, bright_helper.get_allowance(MealType.BREAKFAST, FoodType.VEGGIES))
        self.assertEqual(0, bright_helper.get_allowance(MealType.BREAKFAST, FoodType.FAT))
        self.assertEqual(0, bright_helper.get_allowance(MealType.BREAKFAST, FoodType.SALAD))

        self.assertEqual(1, bright_helper.get_allowance(MealType.LUNCH, FoodType.PROTEIN))
        self.assertEqual(0, bright_helper.get_allowance(MealType.LUNCH, FoodType.GRAIN))
        self.assertEqual(1, bright_helper.get_allowance(MealType.LUNCH, FoodType.FRUIT))
        self.assertEqual(1, bright_helper.get_allowance(MealType.LUNCH, FoodType.VEGGIES))
        self.assertEqual(1, bright_helper.get_allowance(MealType.LUNCH, FoodType.FAT))
        self.assertEqual(0, bright_helper.get_allowance(MealType.LUNCH, FoodType.SALAD))


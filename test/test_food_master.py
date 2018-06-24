from unittest import TestCase
from src.food_master import PyFoodMaster as FoodMaster
from src.common import Food, FoodType


class TestFoodMaster(TestCase):

    def test_get_food_type(self):
        food_type = FoodMaster.get_food_type(Food.MILK_NON_DAIRY)
        self.assertEqual(FoodType.PROTEIN, food_type)

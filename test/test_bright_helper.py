from unittest import TestCase
from src.bright_helper import BrightHelper
from src.common import Gender, MealType, FoodType, Food
from src.food_option import FoodOption


class TestBrightHelper(TestCase):

    def test_male_weight_loss_breakfast_options_correct(self):
        """
        Given a male on a weight loss meal plan
          and they have not chosen any food yet
        When he asks for breakfast grain options
        Then he gets all the correct options
        """
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

    def test_how_much_after_choose_all_meal_type_allowance(self):
        """
        Given a male on a weight loss meal plan
        When he chooses 4 oz of potato for breakfast (the whole allowance)
         and he asks for breakfast grain options
        Then he gets no options

        """
        bright_helper = BrightHelper.build_weight_loss_helper(Gender.MALE)

        bright_helper.choose_food(MealType.BREAKFAST, Food.POTATO, 4)
        actual = bright_helper.get_meal_type_options(MealType.BREAKFAST, FoodType.GRAIN)
        expected = set()
        self.assertEqual(expected, actual)

    def test_how_much_after_choose_half_meal_type_allowance(self):
        """
        Given a male on a weight loss meal plan
        When he chooses 4 oz of potato for breakfast (half the allowance)
         and he asks for breakfast grain options
        Then he gets all options with only half available oz

        """
        bright_helper = BrightHelper.build_weight_loss_helper(Gender.MALE)

        bright_helper.choose_food(MealType.BREAKFAST, Food.YAM, 2)
        actual = bright_helper.get_meal_type_options(MealType.BREAKFAST, FoodType.GRAIN)
        expected = {
            FoodOption(Food.POTATO, 2), FoodOption(Food.POTATO_SWEET, 2),
            FoodOption(Food.YAM, 2), FoodOption(Food.RICE, 2),
            FoodOption(Food.QUINOA, 2), FoodOption(Food.MILLET, 2),
            FoodOption(Food.OATMEAL, 0.5), FoodOption(Food.BRAN_OAT, 0.5),
            FoodOption(Food.CREAM_OF_RICE, 0.5), FoodOption(Food.GRITS, 0.5),
            FoodOption(Food.CREAM_OF_WHEAT, 0.5), FoodOption(Food.QUINOA_FLAKES, 0.5),
            FoodOption(Food.CEREAL, 0.5)
        }
        self.assertEqual(expected, actual)

    def test_how_much_after_choose_half_meal_type_allowance_and_then_remaining_allowance(self):
        """
        Given a male on a weight loss meal plan
        When he chooses 2 oz of quinoa for breakfast (half the allowance)
         and he chooses 0.5 oz of oatmeal (the remaining amount of allowance)
         and he asks for breakfast grain options
        Then he gets no options

        """
        bright_helper = BrightHelper.build_weight_loss_helper(Gender.MALE)

        bright_helper.choose_food(MealType.BREAKFAST, Food.QUINOA, 2)
        bright_helper.choose_food(MealType.BREAKFAST, Food.OATMEAL, 0.5)
        actual = bright_helper.get_meal_type_options(MealType.BREAKFAST, FoodType.GRAIN)
        expected = set()
        self.assertEqual(expected, actual)

    def test_(self):
        """
        Given a male on a weight loss meal plan
        When he asks for his allowances left for breakfast
        Then he gets 1 Grain, 1 Protein, and 1 Fruit
        """
        bright_helper = BrightHelper.build_weight_loss_helper(Gender.MALE)

        actual = bright_helper.get_meal_allowances(MealType.BREAKFAST)
        expected = {
            FoodType.GRAIN: 1,
            FoodType.PROTEIN: 1,
            FoodType.FRUIT: 1
        }
        self.assertEqual(expected, actual)

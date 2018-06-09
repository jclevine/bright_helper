from unittest import TestCase

from src.meal_planner import MealPlanner


class TestMealPlanner(TestCase):

    def test_meal_plan_length(self):
        """
        Given a meal planer for 2 days
        When you ask for the length of the meal plan
        Then it returns 2
        """
        meal_planner = MealPlanner(plan_length=2)
        self.assertEqual(2, meal_planner.plan_length)

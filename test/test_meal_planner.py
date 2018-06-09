from datetime import date
from unittest import TestCase
from unittest.mock import Mock, patch

from src.common import DayOfWeek
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

    @patch('src.meal_planner.date', return_value=Mock(side_effect=lambda *args, **kw: date(*args, **kw)))
    def test_get_empty_meal_plan(self, mock_date):
        """
        Given a meal planer for 2 days from today
          and today is Wednesday, Aug 29, 2018
        When you ask for the meal plan
        Then it returns Wednesday & Thursday with nothing in them
        """
        mock_date.today.return_value = date(2018, 8, 29)

        meal_planner = MealPlanner(start_in_days=0, plan_length=2)
        expected = {
            DayOfWeek.WEDNESDAY: {},
            DayOfWeek.THURSDAY: {}
        }
        self.assertEqual(expected, meal_planner.get_current_plan())

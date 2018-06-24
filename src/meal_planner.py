from datetime import date, timedelta

from src.bright_helper import BrightHelper as MealHelper
from src.common import DayOfWeek, MealType
from itertools import cycle, islice


class MealPlanner(object):
    def __init__(self, meal_plan_helper, start_in_days=0, plan_length=7):
        # TODO: jlevine - Maybe get rid of some unnecessary instance variables
        self._meal_plan_helper = meal_plan_helper
        self._start_date = date.today() + timedelta(start_in_days)
        self._plan_length = plan_length
        start_day_of_week = self._start_date.weekday()
        end_day_of_week = start_day_of_week + self._plan_length
        self._all_days = list(islice(cycle(DayOfWeek), start_day_of_week, end_day_of_week))
        self._meal_plan_helpers = {day_of_week: MealHelper.clone(meal_plan_helper) for day_of_week in self._all_days}

    @property
    def plan_length(self):
        return self._plan_length

    def get_current_plan(self):
        return {day_of_week: {} for day_of_week in self._all_days}

    def get_meal_allowances(self):
        return {
            day_of_week: meal_plan_helper.get_meal_allowances(MealType.ALL)
            for day_of_week, meal_plan_helper in self._meal_plan_helpers.items()
        }

    def get_meal_allowances_by_day_and_meal(self, day_of_week, meal_type):
        return self._meal_plan_helpers[day_of_week].get_meal_allowances(meal_type)

    def get_meal_allowances_by_day(self, day_of_week):
        return self._meal_plan_helpers[day_of_week].get_meal_allowances(MealType.ALL)

    def get_food_options(self, day_of_week, meal_type, food_type):
        return self._meal_plan_helpers[day_of_week].get_meal_type_options(meal_type, food_type)

    def choose_food(self, days_of_week, meal_type, food, ounces):
        days_list = [days_of_week] if type(days_of_week) != list else days_of_week
        [self._meal_plan_helpers[day_of_week].choose_food(meal_type, food, ounces) for day_of_week in days_list]

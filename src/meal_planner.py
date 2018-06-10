from datetime import date, timedelta
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

    @property
    def plan_length(self):
        return self._plan_length

    def get_current_plan(self):
        return {day_of_week: {} for day_of_week in self._all_days}

    def get_meal_allowances(self):
        return {day_of_week: self._meal_plan_helper.get_meal_allowances(MealType.ALL) for day_of_week in self._all_days}

    def get_food_options(self, day_of_week, meal_type, food_type):
        return self._meal_plan_helper.get_meal_type_options(meal_type, food_type)

from datetime import date, timedelta
import calendar
from src.common import DayOfWeek
from itertools import cycle, islice


class MealPlanner(object):
    def __init__(self, start_in_days=0, plan_length=7):
        self._start_date = date.today() + timedelta(start_in_days)
        self._plan_length = plan_length

    @property
    def plan_length(self):
        return self._plan_length

    def get_current_plan(self):
        start_day_of_week = self._start_date.weekday()
        end_day_of_week = start_day_of_week + self._plan_length
        return {day_of_week: {} for day_of_week in list(islice(cycle(DayOfWeek), start_day_of_week, end_day_of_week))}

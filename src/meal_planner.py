class MealPlanner(object):
    def __init__(self, plan_length=7):
        self._plan_length = plan_length

    @property
    def plan_length(self):
        return self._plan_length

from src.common import MealPlanType, MealType
from src.allowance_master import PyAllowanceMaster as AllowanceMaster


class BrightHelper(object):
    def __init__(self, gender, meal_plan_type):
        self._allowance_master = AllowanceMaster(gender, meal_plan_type)

    @property
    def gender(self):
        return self._allowance_master.gender

    @property
    def meal_plan_type(self):
        return self._allowance_master.meal_plan_type

    @staticmethod
    def build_weight_loss_helper(gender):
        return BrightHelper(gender, MealPlanType.WEIGHT_LOSS)

    def get_meal_type_options(self, meal_type, food_type):
        return self._allowance_master.get_meal_type_options(meal_type, food_type)

    def choose_food(self, meal_type, food, ounces):
        self._allowance_master.choose_food(meal_type, food, ounces)

    def get_meal_allowances(self, meal_type):
        if meal_type == MealType.ALL:
            return {meal_type: self._allowance_master.get_meal_allowances(meal_type) for meal_type in MealType.get_all()}
        return self._allowance_master.get_meal_allowances(meal_type)

    @staticmethod
    def clone(bright_helper):
        return BrightHelper(bright_helper.gender, bright_helper.meal_plan_type)

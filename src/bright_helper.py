from src.common import MealPlanType
from src.allowance_master import PyAllowanceMaster as AllowanceMaster


class BrightHelper(object):
    def __init__(self, gender, meal_plan_type):
        self._allowance_master = AllowanceMaster(gender, meal_plan_type)


    @staticmethod
    def build_weight_loss_helper(gender):
        return BrightHelper(gender, MealPlanType.WEIGHT_LOSS)

    def get_allowance(self, meal_type, food_type):
        return self._allowance_master.get_allowance(meal_type, food_type)

    def get_meal_type_options(self, meal_type, food_type):
        return self._allowance_master.get_meal_type_options(meal_type, food_type)

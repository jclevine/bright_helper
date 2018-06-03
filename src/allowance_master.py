from src.common import MealType, Gender, MealPlanType, FoodType
from copy import deepcopy
from src.food_master import PyFoodMaster as FoodMaster


class PyAllowanceMaster(object):
    _bible = {
        Gender.MALE: {
            MealPlanType.WEIGHT_LOSS: {
                MealType.BREAKFAST: {
                    FoodType.PROTEIN: 1,
                    FoodType.GRAIN: 1,
                    FoodType.FRUIT: 1
                },
                MealType.LUNCH: {
                    FoodType.PROTEIN: 1,
                    FoodType.VEGGIES: 1,
                    FoodType.FRUIT: 1,
                    FoodType.FAT: 1
                },
                MealType.DINNER: {
                    FoodType.PROTEIN: 1,
                    FoodType.VEGGIES: 1,
                    FoodType.SALAD: 1,
                    FoodType.FAT: 1
                }
            }
        }
    }

    def __init__(self, gender, meal_plan_type):
        self._gender = gender
        self._meal_plan_type = meal_plan_type
        self._food_types_remaining = deepcopy(self._bible)
        self._food_master = FoodMaster(gender, meal_plan_type)

    def get_meal_type_options(self, meal_type, food_type):
        if self._dict_has_all_nested_keys(self._food_types_remaining, self._gender,
                                          self._meal_plan_type, meal_type, food_type):
            this_food_remaining = self._food_types_remaining[self._gender][self._meal_plan_type][meal_type][food_type]
            return self._food_master.get_options(food_type, this_food_remaining)
        else:
            return []

    def choose_food(self, meal_type, food_type):
        pass

    @staticmethod
    def _dict_has_all_nested_keys(a_dict, *keys):
        _element = a_dict
        for key in keys:
            try:
                _element = _element[key]
            except KeyError:
                return False
        return True


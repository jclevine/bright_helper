from src.common import MealType, Gender, MealPlanType, FoodType
from copy import deepcopy
from src.food_master import PyFoodMaster as FoodMaster


class PyAllowanceMaster(object):
    _allowance_bible = {
        Gender.MALE: {
            MealPlanType.WEIGHT_LOSS: {
                MealType.BREAKFAST: {
                    FoodType.PROTEIN: 1.0,
                    FoodType.GRAIN: 1.0,
                    FoodType.FRUIT: 1.0
                },
                MealType.LUNCH: {
                    FoodType.PROTEIN: 1.0,
                    FoodType.VEGGIES: 1.0,
                    FoodType.FRUIT: 1.0,
                    FoodType.FAT: 1.0
                },
                MealType.DINNER: {
                    FoodType.PROTEIN: 1.0,
                    FoodType.VEGGIES: 1.0,
                    FoodType.SALAD: 1.0,
                    FoodType.FAT: 1.0
                }
            }
        }
    }

    def __init__(self, gender, meal_plan_type):
        self._gender = gender
        self._meal_plan_type = meal_plan_type
        self._food_types_remaining = deepcopy(self._allowance_bible)
        self._food_master = FoodMaster(gender, meal_plan_type)

    def get_meal_type_options(self, meal_type, food_type):
        if self._is_food_type_allowed_for_meal_type(meal_type, food_type):
            food_type_allowance_remaining = self._get_food_type_allowance_remaining(meal_type, food_type)
            return self._food_master.get_options(food_type, food_type_allowance_remaining)
        else:
            return set()

    def _get_food_type_allowance_remaining(self, meal_type, food_type):
        return self.get_meal_allowances(meal_type)[food_type]

    def choose_food(self, meal_type, food, ounces):
        if self._is_food_type_allowed_for_meal_type(meal_type, food.type):
            food_type_allowance_remaining = self._get_food_type_allowance_remaining(meal_type, food.type)
            one_serving_in_oz = self._food_master.get_one_serving_in_ounces(food)
            oz_remaining = food_type_allowance_remaining * one_serving_in_oz

            if ounces > oz_remaining:
                raise Exception('{} oz of {} is more than your limit for {} -- only {} oz remaining'
                                .format(ounces, food, meal_type, oz_remaining))
            else:
                food_type_allowance_remaining = food_type_allowance_remaining - (ounces / one_serving_in_oz)
                self._set_food_type_allowance_remaining(meal_type, food.type, food_type_allowance_remaining)

        else:
            raise Exception('You are not allowed {} for {}. Sorry.'.format(food, meal_type))

    def _set_food_type_allowance_remaining(self, meal_type, food_type, allowance_remaining):
        self._food_types_remaining[self._gender][self._meal_plan_type][meal_type][food_type] = allowance_remaining

    def _is_food_type_allowed_for_meal_type(self, meal_type, food_type):
        return self._dict_has_all_nested_keys(self._food_types_remaining, self._gender,
                                              self._meal_plan_type, meal_type, food_type)

    @staticmethod
    def _dict_has_all_nested_keys(a_dict, *keys):
        _element = a_dict
        for key in keys:
            try:
                _element = _element[key]
            except KeyError:
                return False
        return True

    def get_meal_allowances(self, meal_type):
        return self._food_types_remaining[self._gender][self._meal_plan_type][meal_type]

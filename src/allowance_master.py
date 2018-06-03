from src.common import MealType, Gender, MealPlanType, FoodType


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
                }
            }
        }

    }

    def __init__(self, gender, meal_plan_type):
        self._gender = gender
        self._meal_plan_type = meal_plan_type

    def get_allowance(self, meal_type, food_type):
        if self._bible_has_all_nested_keys(self._gender, self._meal_plan_type, meal_type, food_type):
            return self._bible[self._gender][self._meal_plan_type][meal_type][food_type]
        else:
            return 0

    def _bible_has_all_nested_keys(self, *keys):
        _element = self._bible
        for key in keys:
            try:
                _element = _element[key]
            except KeyError:
                return False
        return True


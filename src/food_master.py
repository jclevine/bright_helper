from src.common import Gender, MealPlanType, FoodType, Food
from src.food_option import FoodOption


class PyFoodMaster(object):
    _plan = {
        Gender.MALE: {
            MealPlanType.WEIGHT_LOSS: {
                FoodType.GRAIN: {
                    FoodOption(Food.POTATO, 4), FoodOption(Food.POTATO_SWEET, 4),
                    FoodOption(Food.YAM, 4), FoodOption(Food.RICE, 4),
                    FoodOption(Food.QUINOA, 4), FoodOption(Food.MILLET, 4),
                    FoodOption(Food.OATMEAL, 1), FoodOption(Food.BRAN_OAT, 1),
                    FoodOption(Food.CREAM_OF_RICE, 1), FoodOption(Food.GRITS, 1),
                    FoodOption(Food.CREAM_OF_WHEAT, 1), FoodOption(Food.QUINOA_FLAKES, 1),
                    FoodOption(Food.CEREAL, 1)
                }
            }
        }

    }

    def __init__(self, gender, meal_plan_type):
        self._gender = gender
        self._meal_plan_type = meal_plan_type

    def get_options(self, food_type, amount_remaining):
        return {food_option for food_option in self._plan[self._gender][self._meal_plan_type][food_type]}

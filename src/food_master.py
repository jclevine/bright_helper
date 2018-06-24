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
                },
                FoodType.PROTEIN: {
                    FoodOption(Food.MILK_NON_DAIRY, 8), FoodOption(Food.TOFU, 6),
                    FoodOption(Food.TEMPEH, 6), FoodOption(Food.BEANS, 6),
                    FoodOption(Food.BEANS_ROASTED, 3), FoodOption(Food.LENTILS, 6),
                    FoodOption(Food.HUMMUS, 6), FoodOption(Food.SOYA_GRANULES, 3),
                    FoodOption(Food.EDAMAME_SHELLED, 6), FoodOption(Food.NUTS, 2),
                    FoodOption(Food.NUT_BUTTER, 2), FoodOption(Food.VEGGIE_BURGER, 6),
                    FoodOption(Food.SEEDS, 2), FoodOption(Food.NUTS_SOY, 3),
                    FoodOption(Food.EDAMAME_DRY_ROASTED, 3)
                }
            }
        },
        Gender.FEMALE: {
            MealPlanType.WEIGHT_LOSS: {
                FoodType.GRAIN: {
                    FoodOption(Food.POTATO, 4), FoodOption(Food.POTATO_SWEET, 4),
                    FoodOption(Food.YAM, 4), FoodOption(Food.RICE, 4),
                    FoodOption(Food.QUINOA, 4), FoodOption(Food.MILLET, 4),
                    FoodOption(Food.OATMEAL, 1), FoodOption(Food.BRAN_OAT, 1),
                    FoodOption(Food.CREAM_OF_RICE, 1), FoodOption(Food.GRITS, 1),
                    FoodOption(Food.CREAM_OF_WHEAT, 1), FoodOption(Food.QUINOA_FLAKES, 1),
                    FoodOption(Food.CEREAL, 1)
                },
                FoodType.PROTEIN: {
                    FoodOption(Food.MILK_NON_DAIRY, 8), FoodOption(Food.TOFU, 4),
                    FoodOption(Food.HUMMUS, 4), FoodOption(Food.SOYA_GRANULES, 2),
                    FoodOption(Food.NUTS, 2), FoodOption(Food.NUT_BUTTER, 2),
                    FoodOption(Food.SEEDS, 2), FoodOption(Food.TEMPEH, 4),
                    FoodOption(Food.BEANS, 6), FoodOption(Food.BEANS_ROASTED, 2),
                    FoodOption(Food.LENTILS, 6), FoodOption(Food.EDAMAME_SHELLED, 4),
                    FoodOption(Food.VEGGIE_BURGER, 4), FoodOption(Food.NUTS_SOY, 2),
                    FoodOption(Food.EDAMAME_DRY_ROASTED, 2)
                }
            }
        }

    }

    def __init__(self, gender, meal_plan_type):
        self._gender = gender
        self._meal_plan_type = meal_plan_type

    def get_one_serving_in_ounces(self, food):
        return {
            food_option.ounces
            for food_option in self._plan[self._gender][self._meal_plan_type][food.type]
            if food_option.food == food
        }.pop()

    def get_options(self, food_type, food_type_remaining):
        return {
            FoodOption(food_option.food, food_option.ounces * food_type_remaining)
            for food_option in self._plan[self._gender][self._meal_plan_type][food_type]
            if food_option.ounces * food_type_remaining != 0
        }

    @staticmethod
    def get_food_type(food):
        return Food.get_food_type(food)

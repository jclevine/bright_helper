from enum import Enum


class Gender(Enum):
    MALE = 'Male'
    FEMALE = 'Female'


class MealType(Enum):
    BREAKFAST = 'Breakfast'
    LUNCH = 'Lunch'
    DINNER = 'Dinner'

    def __str__(self):
        return self.value


class FoodType(Enum):
    PROTEIN = 'Protein'
    GRAIN = 'Grain'
    FRUIT = 'Fruit'
    VEGGIES = 'Veggies'
    FAT = 'Fat'
    SALAD = 'Salad'


class MealPlanType(Enum):
    WEIGHT_LOSS = 'Weight Loss'


class Food(Enum):
    POTATO = ('Potato', FoodType.GRAIN)
    POTATO_SWEET = ('Sweet Potato', FoodType.GRAIN)
    YAM = ('Yam', FoodType.GRAIN)
    QUINOA = ('Quinoa', FoodType.GRAIN)
    RICE = ('Rice', FoodType.GRAIN)
    CREAM_OF_RICE = ('Cream of Rice', FoodType.GRAIN)
    CREAM_OF_WHEAT = ('Cream of Wheat', FoodType.GRAIN)
    QUINOA_FLAKES = ('Quinoa Flakes', FoodType.GRAIN)
    GRITS = ('Grits', FoodType.GRAIN)
    MILLET = ('Millet', FoodType.GRAIN)
    OATMEAL = ('Oatmeal', FoodType.GRAIN)
    BRAN_OAT = ('Oat Bran', FoodType.GRAIN)
    CEREAL = ('Cereal', FoodType.GRAIN)

    @property
    def type(self):
        return self.value[1]

    def __str__(self):
        return self.value[0]

    def __repr__(self):
        return self.value


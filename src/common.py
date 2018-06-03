from enum import Enum


class Gender(Enum):
    MALE = 'Male'
    FEMALE = 'Female'


class MealType(Enum):
    BREAKFAST = 'Breakfast'
    LUNCH = 'Lunch'
    DINNER = 'Dinner'


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
    POTATO = 'Potato'
    POTATO_SWEET = 'Sweet Potato'
    YAM = 'Yam'
    QUINOA = 'Quinoa'
    RICE = 'Rice'
    CREAM_OF_RICE = 'Cream of Rice'
    CREAM_OF_WHEAT = 'Cream of Wheat'
    QUINOA_FLAKES = 'Quinoa Flakes'
    GRITS = 'Grits'
    MILLET = 'Millet'
    OATMEAL = 'Oatmeal'
    BRAN_OAT = 'Oat Bran'
    CEREAL = 'Cereal'

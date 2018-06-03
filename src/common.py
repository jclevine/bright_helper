from enum import Enum


class Gender(Enum):
    MALE = 'Male'
    FEMALE = 'Female'


class MealType(Enum):
    BREAKFAST = 'Breakfast'


class FoodType(Enum):
    PROTEIN = 'Protein'
    GRAIN = 'Grain'
    FRUIT = 'Fruit'
    VEGGIES = 'Veggies'
    FAT = 'Fat'


class MealPlanType(Enum):
    WEIGHT_LOSS = 'Weight Loss'

from enum import Enum


class Gender(Enum):
    MALE = 'Male'
    FEMALE = 'Female'


class MealType(Enum):
    BREAKFAST = 'Breakfast'
    LUNCH = 'Lunch'
    DINNER = 'Dinner'
    ALL = 'All'

    @classmethod
    def get_all(cls):
        return [cls.BREAKFAST, cls.LUNCH, cls.DINNER]

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


class DayOfWeek(Enum):
    MONDAY = ('Monday', 0)
    TUESDAY = ('Tuesday', 1)
    WEDNESDAY = ('Wednesday', 2)
    THURSDAY = ('Thursday', 3)
    FRIDAY = ('Friday', 4)
    SATURDAY = ('Saturday', 5)
    SUNDAY = ('Sunday', 6)

    @property
    def name(self):
        return self.value[0]

    @property
    def index(self):
        return self.value[1]

    def __eq__(self, other):
        return self.index == other.index

    def __hash__(self):
        return hash(self.name)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

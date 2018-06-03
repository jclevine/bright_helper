class FoodOption(object):

    def __init__(self, food, ounces):
        self._food, self._ounces = food, ounces

    @property
    def food(self):
        return self._food

    @property
    def ounces(self):
        return self._ounces

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __hash__(self):
        return hash(self._food)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return '{}: {} ounces'.format(self.food, self.ounces)

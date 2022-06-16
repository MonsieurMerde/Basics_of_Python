from abc import ABC, abstractmethod


class Clothing(ABC):

    _total_clothing_require = 0

    @abstractmethod
    def clothing_require(self):
        pass

    @abstractmethod
    def add_to_reserve(self):
        pass


class Coat(Clothing):

    def __init__(self, size):
        self.size = size

    @property
    def clothing_require(self):
        return self.size/6.5 + 0.5

    @property
    def add_to_reserve(self):
        Coat._total_clothing_require += self.size/6.5 + 0.5
        return Coat._total_clothing_require


class Costume(Clothing):

    def __init__(self, height):
        self.height = height

    @property
    def clothing_require(self):
        return self.height*2 + 0.3

    @property
    def add_to_reserve(self):
        Costume._total_clothing_require += self.height*2 + 0.3
        return Costume._total_clothing_require


coat_1 = Coat(12)
coat_2 = Coat(1)
coat_3 = Coat(144)
print(coat_1.clothing_require)
print(coat_1.add_to_reserve)
print(coat_2.clothing_require)
print(coat_2.add_to_reserve)
print(coat_3.clothing_require)
print(coat_3.add_to_reserve)
print('\n')
costume_1 = Costume(10)
costume_2 = Costume(2)
costume_3 = Costume(125)
print(costume_1.clothing_require)
print(costume_1.add_to_reserve)
print(costume_2.clothing_require)
print(costume_2.add_to_reserve)
print(costume_3.clothing_require)
print(costume_3.add_to_reserve)

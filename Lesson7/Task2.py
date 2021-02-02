from abc import ABC, abstractmethod


class Wearings(ABC):
    @abstractmethod
    def common_material(self):
        pass


class Suit(Wearings):

    def __init__(self, my_size):
        self.material_spent = my_size * 2 + 0.3
        self.__my_size = my_size

    @property
    def my_size(self):
        return self.__my_size

    @my_size.setter
    def my_size(self, my_size):
        if my_size < 1:
            self.__my_size = 1
        else:
            self.__my_size = my_size

    def common_material(self):
        return round(self.material_spent, 2)


class Coat(Wearings):
    def __init__(self, height):
        self.material_spent = (height / 6.5 + 0.5)
        self.__my_height = height

    @property
    def my_height(self):
        return self.__my_height

    @my_height.setter
    def my_height(self, size):
        if size < 1:
            self.__my_height = 1
        else:
            self.__my_height = size

    def common_material(self):
        return str(round(self.material_spent, 2))

try:
    a = Coat(float(input("Please enter person height for coat material calculation: ")))
    b = Suit(float(input("Please enter person size for suit material calculation: ")))

    print(f"For person {str(a.my_height)} tall you need {str(a.common_material())} sq.m materials")
    print(f"For person {str(b.my_size)} size you need {str(b.common_material())} sq.m materials")
except ValueError as error:
    print(f"Wrong size or height entered: {error}")
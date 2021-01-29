class Road:
    _length = 0
    _width = 0
    thickness = 5
    weight = 25

    def __init__(self, length=0, width=0, thickness=0):
        self._length = length
        self._width = width
        self.thickness = thickness

    def calculator(self):
        print(f"Total weight is {self._length * self._width * self.thickness * self.weight / 1000} tonns")


try:
    asphalt = Road(int(input("Please enter length: ")), int(input("Please enter width: ")),
                   int(input("Please enter thickness: ")))
    asphalt.calculator()
except ValueError as error:
    print(error)

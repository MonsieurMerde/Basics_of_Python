class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def total_mass(self, thickness):
        total_mass = (self._length * self._width * 25 * thickness) // 1000
        return f'{self._length} м*{self._width} м*25 кг*{thickness} см = {total_mass} т'


new_road_1 = Road(40, 10000)
print(new_road_1.total_mass(5))

new_road_2 = Road(60, 25550)
print(new_road_2.total_mass(7))

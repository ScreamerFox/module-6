import math

class Figure:
    sides_count = 0

    def __init__(self, *sides):
        self.__sides = []
        self.__color = [0, 0, 0]
        self.filled = False
        self.set_sides(*sides)

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if all(isinstance(value, int) and 0 <= value <= 255 for value in (r, g, b)):
            return True
        return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]


    def __is_valid_sides(self, *sides):
        if len(sides) != self.sides_count:
            return False
        if all(isinstance(side, int) and side > 0 for side in sides):
            return True
        return False

    def get_sides(self):
        return self.__sides

    def set_sides(self, *sides):
        if self.__is_valid_sides(*sides):
            self.__sides = list(sides)


    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(*sides)
        if len(sides) != self.sides_count:
            self.set_sides(1)
        else:
            self.__radius = self.__calculate_radius(sides[0])
        self.set_color(*color)

    def __calculate_radius(self, circum):
        return circum / (2 * math.pi)

    def get_square(self):
        return math.pi * self.__radius ** 2

    def set_sides(self, *sides):
        if len(sides) == self.sides_count and all(isinstance(side, int) and side > 0 for side in sides):
            circumference = sides[0]
            self.__radius = self.__calculate_radius(circumference)
            super().set_sides(circumference)



class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(*sides)
        if len(sides) != self.sides_count:
            self.set_sides(1, 1, 1)
        else:
            self.__height = self.__calculate_height(*sides)
        self.set_color(*color)

    def __calculate_height(self, a, b, c):
        # Используем формулу Герона для расчета площади и затем высоты
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        height = (2 * area) / a  # Высота к стороне a
        return height

    def get_square(self):
        a = self.get_sides()[0]
        return 0.5 * a * self.__height


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(*sides)
        if len(sides) != 1:
            self.set_sides(1)
        else:
            self.set_sides(sides[0])
        self.set_color(*color)

    def set_sides(self, side):
        if isinstance(side, int) and side > 0:
            sides = [side] * self.sides_count
            super().set_sides(*sides)


    def get_volume(self):
        side = self.get_sides()[0]
        return side ** 3


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
#cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

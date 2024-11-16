import math

class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__color = list(color)
        if len(list(sides)) == self.sides_count:
            self.__sides = list(sides)
        elif len(list(sides)) == 1:
            self.__sides = list(sides * self.sides_count)
        else:
            self.__sides = list([1] * self.sides_count)

    def info(self):
        print(f'Name: {self.name}, color: {self.__color}, sides: {self.__sides}')

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        self.r, self.g, self.b = r, g, b
        if isinstance(self.r, int) and isinstance(self.g, int) and isinstance(self.b, int):
            if 0 <= self.r <= 255 and 0 <= self.g <= 255 and 0 <= self.b <= 255:
                return True
            else:
                return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, new_sides):
        if len(new_sides) == self.sides_count:
            for side in new_sides:
                if isinstance(side, int) and side > 0:
                    return True
                else:
                    return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides):
            self.__sides = list(new_sides)

class Circle(Figure):
    sides_count = 1
    name = "Circle"

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self.get_sides()[0] / (2 * math.pi)

    def get_square(self):
        return math.pi * (self.__radius ** 2)

class Triangle(Figure):
    sides_count = 3
    name = "Triangle"

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_square(self):
        p = len(self)/2
        a, b, c = self.get_sides()[0], self.get_sides()[1], self.get_sides()[2]
        return math.sqrt(p*(p-a)*(p-b)*(p-c))

class Cube(Figure):
    sides_count = 12
    name = "Cube"

    def __init__(self, color, *sides):
        if len(sides) == 1:
            side = sides[0]
        else:
            side = 1
        super().__init__(color, side)

    def get_volume(self):
        return self.get_sides()[0] ** 3

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
tr1 = Triangle((167,34,88), 2,7,8)
print()

print("Исходные параметры:")
circle1.info()
cube1.info()
tr1.info()
print()

print("Проверка на изменение цветов:")
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())
tr1.set_color(53,9,0)
print(tr1.get_color())
print()

print("Проверка на изменение сторон:")
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())
tr1.set_sides(3,4,5) #Изменится
print(tr1.get_sides())
print()

print("Проверка периметра:")
print(len(circle1))
print(len(cube1))
print(len(tr1))
print()

print("Проверка площади:")
print(circle1.get_square())
print(tr1.get_square())
print()

print("Проверка объёма (куба):")
print(cube1.get_volume())
print()

print("Изменённые параметры:")
circle1.info()
cube1.info()
tr1.info()

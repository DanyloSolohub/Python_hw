# 1)
# создать класс Human(имя и возраст)
# и два класса Prince и Cinderella которые наследуются от Human
# у принца должен быть размер туфельки и  метод который принимает
# лист золушек и выводит какой золушки подошла туфелька

"""class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Cinderella(Human):
    def __init__(self, name, age, feet_size):
        super().__init__(name, age)
        self.feet_size = feet_size

    def lost(self):
        return self.feet_size


Nastya = Cinderella('Nastya', 18, 38)
Ivanka = Cinderella('Ivanka', 19, 37)
Sofia = Cinderella('Sofia', 20, 38)
Dora = Cinderella('Dora', 18, 36)

lg = [Nastya, Ivanka, Sofia, Dora]


class Prince(Human):
    def __init__(self, name, age, found_size):
        super().__init__(name, age)
        self.found_size = found_size

    def find(self, girls):
        for girl in girls:
            if girl.feet_size == self.found_size:
                print(f'{self.name} and {girl.name}')
                break


Danylo = Prince('Danylo', 18, 36)
Danylo.find(lg)
"""


# 2)
# Создать класс Rectangle:
# -конструктор принимает две стороны x,y
# -описать арифметические методы:
#   + сума площадей двух экземпляров класса
#   - разница площадей
#   == или площади равны
#   != не равны
#   >, < меньше или больше
#   при вызове метода len() подсчитывать сумму сторон


class Rectangle:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def area(self):
        return self.__y * self.__x

    def perimeter(self):
        return 2 * (self.__y * self.__x)

    def __len__(self):
        return self.__x + self.__y

    def __add__(self, other):
        return self.area() + other.area()

    def __sub__(self, other):
        return self.area() - other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __lt__(self, other):
        return self.area() < other.area()


first = Rectangle(3, 4)
second = Rectangle(5, 6)
print(first + second)
print(first - second)
print(first == second)
print(first > second)
print(first < second)
print(first != second)
print(len(first))

"""l1 = []


class Letter:
    _count = 0

    def __init__(self, text):
        self._text = text
        self._count += 1

    def get_text(self):
        return self._text

    def set_text(self, text):
        self._text = text

    def get_count(self):
        return self._count

    def add_to_list(self):
        l1.append(self._text)


letter = Letter('edw')
letter1 = Letter('edw')
letter2 = Letter('edw')
letter.add_to_list()
print(letter.get_count())
print(l1)
"""
"""from abc import ABC, abstractmethod


class Transportation(ABC):
    @abstractmethod
    def time(self):
        pass


class Fly(Transportation):
    def __init__(self, price, check_in, time, clas):
        self.price = price
        self.check_in = check_in
        self.time = time
        self.clas = clas

    def time(self):
        return self.time

    def price(self):
        return self.price

    def class_of_fly(self):
        return self.clas

    def check_in(self):
        return self.check_in

    def time_in(self):
        return self.check_in - self.time


class Car(Transportation):
    def __init__(self, time, fuel_price, length, num_of_pass):
        self.time = time
        self.fuel_price = fuel_price
        self.length = length
        self.num_of_pass = num_of_pass

    def time(self):
        return self.time

    def num_of(self):
        return self.num_of_pass

    def length_road(self):
        return self.length

    def fuel_price(self):
        return self.fuel_price

    def price_to_road(self):
        return self.length / self.fuel_price


class Train(Transportation):
    def __init__(self, time, price, place):
        self.time = time
        self.price = price
        self.place = place

    def time(self):
        return self.time

    def price(self):
        return self.price

    def place(self):
        return self.price

    def __gt__(self, other):
        return self.time() > other.time()

    def __lt__(self, other):
        return self.time() < other.time()


Fly(1000, 12, 4, 1)
Car(10, 30, 500, 4)
Train(3, 500, 'sw')"""

"""
def func(str1: str):
    i = ''
    l1 = []
    for num in str1:
        if num.isdigit():
            i += num
        else:
            if i != '':
                l1.append(i)
                i = ''
    if i != '':
        l1.append(i)
    print(l1)


func('1 12 eg6rf 544')"""


















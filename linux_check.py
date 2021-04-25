# a = {'q': 'a',
#      'y': 1,
#      't': 1,
#      'r': 1,
#      'e': 1,
#      'w': 1
#      }
# print(*a.values())

# Это простое упражнение на использование упаковок.
#
# Определите функцию print_given, которая для каждого переданного аргумента
# будет распечатывать на отдельной строке через пробел имя аргумента
# (если таковое имеется), значение аргумента, тип аргумента.
#
# Аргументы без имени должны быть распечатаны раньше именованных.
# Порядок печати аргументов без имени важен: он должен совпадать с порядком
# , в котором аргументы передаются. Порядок печати аргументов с именем неважен.

"""def print_given(*args, **kwargs):
    l = [*args]
    for i in range(len(l)):
        print(l[i], type(l[i]))

    for k, v in kwargs.items():
        print(k, v, type(v))


print_given(1, 2, [1, 3], 5, 1, 'one', zero=0, one=1, two=2)
"""
# Это простое упражнение (а заодно и распространённый пример)
# на использование распаковок.
#
# На вход подаётся строка, содержащая некоторое количество
# (не больше сотни) записанных через пробел целых чисел.
#
# Распечатайте каждое целое число, приведённое к типу float, на отдельной с
# троке в том же порядке, в котором они были переданы.

input_data = input()


def foo(string: str):
    num_list = []
    num = ''
    for i in string:
        if i.isdigit():
            num += i
        else:
            if num:
                num_list.append(num)
                num = ''
    if num:
        num_list.append(num)
    print(*num_list, sep=',')


foo(input_data)
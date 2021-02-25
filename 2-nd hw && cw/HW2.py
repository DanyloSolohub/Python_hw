# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
"""
def checkstr(string):
    string = [i for i in string if i.isdigit()]
    my_string = ','.join(string)
    print(my_string)


checkstr('as 23 fdfdg544 34')
"""

# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
"""
def func(st):
    num_list = []
    num = ''
    for i in st:
        if i.isdigit():
            # print(i, end=',')
            num += i
            # print(num)
        else:
            if num != '':
                num_list.append(num)
                num = ''
    if num != '':
        num_list.append(num)
    final_num = ','.join(num_list)
    # print(num_list)
    print(final_num)

func('as 23 fd6fdg544 34')
"""
# записать каждый символ в лист поменяв его на верхний регистр
'''
greeting = 'Hello, world'
upper = greeting.upper()
l1 = [i for i in upper]
print(l1)
'''
#  с диапазона от 0-50 записать в лист только не парные числа, при этом возвести их в квадрат
'''
n1 = [pow(i, 2) for i in range(50) if i % 2 != 0 or i == 0]
print(n1)
'''

# - створити функцію яка виводить ліст
'''
def func(lst):
    print(list(lst))
func('vecdwx')
'''

# - створити функцію яка приймає три числа та виводить та повертає найменьше.
'''
def minNum(a, b, c):
    l1 = [a, b, c]
    return min(l1)


print(minNum(1, 2, 3))
'''

# - створити функцію яка приймає три числа та виводить та повертає найбільше.
'''
def maxNum(a, b, c):
    l1 = [a, b, c]
    return max(l1)


print(maxNum(1, 2, 3))
'''

# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше,
# а виводить найбільше
'''
def func(*args):
    print(max(args))
    return min(args)


func(-1, 10, 123, 555)
print(func(-1, 10, 123, 555))
'''

#  створити функцію яка повертає найбільше число з ліста
'''
def lfunc(*args):
    l = list(args)
    print(max(l))


lfunc(1, 2, 3, 4, 6)
'''

# - створити функцію яка повертає найменьше число з ліста
'''
def lfunc(*args):
    l = list(args)
    print(min(l))

lfunc(1, 2, 3, 4, 6)
'''

# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.
'''
def sumList(*args):
    l1 = list(args)
    return sum(l1)


print(sumList(1, 2, 3, 4, 5, 6, 7, 8, 9))
'''

# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.
'''
def sumList(*args):
    l1 = list(args)
    return sum(l1) / len(l1)


print(sumList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
'''

# decorators
# - є функція:
# def pr():
#     return 'Hello_boss_!!!'
#  написати декоратор до цієї функції,
#  який замінює нижні підчеркування на пробіли і повертає це значення

'''
def decor(func):
    def wrap():
       return func().replace('_', ' ')
    return wrap


@decor
def pr():
   return 'Hello_boss_!!!'


print(pr())
'''

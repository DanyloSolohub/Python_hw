# создать функцию которая принимает число и возвращает
# текст как в примере:
# 3275  —>  "3000 + 200 + 70 +5"
#
# Доп 1
#
"""
def func(num):
    num = str(num)
    l1 = []
    for i in range(len(num)):
        l1.append(str(num[i]) + ('0' * (len(num) - (i + 1))))
    res = ' + '.join(l1)
    return res


print(func(948576))
"""
# _______________________
#
#
# Количество единиц
# Дана последовательность натуральных чисел  в строке, завершающаяся
# двумя числами 0 подряд. Определите, сколько раз в этой
# последовательности встречается число 1. Числа, идущие после двух
# нулей, необходимо игнорировать.
#
# 2176491947586100 -> 3
# Доп 3
"""
def find_1(num):
    count = 0
    num = str(num)
    for i in range(len(num)):
        if num[i] == '1':
            count += 1
        elif num[i] == '0' and num[i + 1] == '0':
            break
    return count


print(find_1(112301111111111148))
print(find_1(1123001111111111148))
"""

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
# прога, що виводить кількість кожного символа з введеної строки
"""
def func(st):
    count = 1
    l1 = list(st)
    l1.sort()
    i = len(l1)
    while i > 0:
        i -= 1
        if l1[i] == l1[i - 1]:
            count += 1
        else:
            print(l1[i], ' = ', count)
            count = 1


func('bbbqwertyytrewqbbbbbaaabbbb321bbbbbbb,,,```bbbbbbbbbbbb1')
"""
# 1)  есть лист:
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# создать новый лист и записать в него 'GT' если элемент
# в numbers больше 4 и 'LT' если элемент меньше или равен 4
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
copy = numbers.copy()
copy = ['GT' if i > 4 else 'LT' for i in copy]
print(copy)
"""
# 2) есть два листа:
# list1 = [1, 2, 3, 4, 5]
# list2 = [-1, 7, 10, -5, -2]
#

# записать в лист тюплы (x,y) если x+y == 0
# пример:
# [(1, -1), (2, -2), (5, -5)]
"""
list1 = [1, 2, 3, 4, 5]
list2 = [-1, 7, 10, -5, -2]
res = [(x, y) for x in list1 for y in list2 if x + y == 0]
print(res)
"""
#
"""
for x in list1:
    for y in list2:
        if x + y == 0:
            res.insert(len(res), (x, y))
print(res)
"""
# 1) Точная степень двойки.
# Дано натуральное число N.
# Выведите слово YES , если число N является точной степенью двойки,
# или слово NO в противном случае.
# Операцией возведения в степень пользоваться нельзя!
"""
inputData = int(input())


def check_pow(number):
    if number == 1:
        return print('No')

    while number > 1:
        number /= 2
    if number < 1:
        return print('NO')
    else:
        return print('Yes')


check_pow(inputData)
"""


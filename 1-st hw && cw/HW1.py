numList = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]

#  - найти min число в листе


minV = min(numList)

#  - удалить все одинаковые значения

copy2 = numList.copy()
copy2.sort()
i = len(copy2)
while i > 0:
    i -= 1
    if copy2[i] == copy2[i - 1]:
        copy2.remove(copy2[i])
        copy2.remove(copy2[i - 1])

# - заменить каждое четвертое значение на "Х"
copy3 = numList.copy()
i = len(copy3)
while i > 0:
    i -= 1
    if i % 4 == 0:
        del copy3[i]
        copy3.insert(i, 'X')

#  - вывести элемент листа, значение которого ближе всего к среднему арифметическому
#  всех элементов этого же листа

i = len(numList)
average = sum(numList) / i
diff = max(numList)
minus = 0
number = 0
while i > 0:
    i -= 1
    minus = numList[i] - average
    if abs(minus) < abs(diff):
        diff = minus
        number = numList[i]

# print(diff)
# print(number)

# 2)вывести на экран пустой квадрат из "*" сторона которого указана в переменой:

"""
a = 7
for i in range(a):
    if i == 0 or i == a - 1:
        for j in range(a):
            print('*', end=' ')
    else:
        print('*', end=' ')
        for j in range(1, a - 1):
            print(' ', end=' ')
        print('*', end=' ')
    print()
"""

# 3) переделать первое задание под меню с помощью цикла

"""
for i in range(10):
    print('1. Найти min число в листе', '2. Удалить все одинаковые значения',
          '3. Заменить каждое четвертое значение на "Х"',
          '4. Вывести элемент листа, значение которого ближе всего к среднему арифметическому всех элементов',
          '5. Exit',
          sep='\n')
    print()
    choose = input('Your choose:')
    if choose == "1":
        print(numList)
        print('min:', minV)
    elif choose == "2":
        print(numList)
        print('result:', copy2)
    elif choose == "3":
        print(numList)
        print('result:', copy3)

    elif choose == '4':
        print(numList)
        print('result:', number)
    elif choose == '5':
        break
    else:
        print('Не понимаю, введите числа от 1 до 6')
"""

#  вывести табличку умножения с помощью цикла while
"""
for i in range(1, 10):
    for j in range(1, 10):
        print(i * j, end='\t')
    print()


i = 0
j = 0
while i < 9:
    i += 1
    while j < 9:
        j += 1
        print(i * j, end='\t')
    j = 0
    print()
"""

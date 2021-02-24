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

list1 = [1, 2, 3, 4, 5]
list2 = [-1, 7, 10, -5, -2]
res = []
for x in list1:
    for y in list2:
        if x + y == 0:
            res.insert(0, (x, y))
print(res)

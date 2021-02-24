itemList = []
itemSum = 0
k = 0
while k == 0:
    print('Оберіть пункт:')
    print('1. Створити запис', '2. Список записів', '3. Загальна сума записів', '4. Пошук по назві', '5. Вихід',
          sep='\n')
    Choose = input('Your choose:')
    if Choose == "1":
        print('Зробіть запис:')
        itemName = input('Назва:')
        itemPrice = int(input('Ціна:'))
        itemList.insert(len(itemList), {'name': itemName, 'price': itemPrice})
        for j in range(len(itemList)):
            print('Назва:', itemList[j].get('name'), end='\t')
            print('Ціна:', itemList[j].get('price'))
    elif Choose == "2":
        for j in range(0, len(itemList)):
            print('Назва:', itemList[j].get('name'), end='\t')
            print('Ціна:', itemList[j].get('price'))
    elif Choose == "3":
        for j in range(len(itemList)):
            itemSum += int(itemList[j].get('price'))
        print('Сума всіх товарів:', itemSum)
        itemSum = 0
    elif Choose == '4':
        inputValue = input('Введіть назву товару:')
        for i in range(len(itemList)):
            if inputValue == itemList[i].get('name'):
                print(itemList[i].get('name'), itemList[i].get('price'), sep='\t')
            else:
                print('Не знайшов такий запис')
    elif Choose == '5':
        break
    else:
        print('Не можу зрозуміти команду, оберіть число від 1 до 5')

#1 Создайте программу, хранящую информацию о великих баскетболистах. Нужно хранить ФИО баскетболиста и
#его рост. Требуется реализовать возможность добавления,
#удаления, поиска, замены данных. Используйте словарь
#для хранения информации
data1 = {'Height': ' 2,06 meters', 'Weight': ' 2,06 meters', 'Age': ' 2,06 meters'}

data2 = {'Height': ' 1,88 meters'}

data3 = {'Height': ' 1,98 meters'}

data4 = {'Height': ' 1,93 meters'}

data5 = {'Height': ' 1,91 meters'}

data6 = {'Height': ' 1,88 meters'}

data7 = {'Height': ' 1,16 meters'}

data8 = {'Height': ' 2,08 meters'}

dictionaryNames = {'Леброн Джеймс': data1, 'Стефен Карри': data2, 'Майкл Джордан': data3, 'Дуэйн Уэйд': data4,
                   'Рассел Уэстбрук': data5, 'Кайри Ирвинг': data6, "Шакил О'Нил": data7, 'Кевин Дюрант': data8}


def funk_add():
    name = str(input("Имя"))

    height = float(input("Height"))

    data = {'Height': height}

    dictionaryNames.update({name: data})

    print(dictionaryNames)


def funk_delete():
    print('Что вы хотите удалить: 0 - все данные, 1 - часть данных')

    answer = int(input('Выберите действие: '))

    if answer == 0:
        name = str(input('Имя: '))

        dictionaryNames.pop(name)

    print(dictionaryNames)

    if answer == 1:

        name = str(input('Имя: '))

        count = 0

        for key in dictionaryNames[name]:
            count += 1

            print(count, ' - ', key, ' - ', dictionaryNames[name][key])

        index = int(input('Значение которое хотите удалить : '))

        key = ''

        count = 0

        for i in dictionaryNames[name]:

            count += 1

            if count == index: key = i

        dictionaryNames[name].pop(key)

        print(dictionaryNames)


list = ['Height', 'Weight', 'Age'];


def funk_edit():
    print(dictionaryNames)

    print('Что вы хотите изменить: 0 - все данные, 1 - часть данных')

    answer = int(input('Выберите действие: '))

    if answer == 0:

        old_name = str(input('Старое Имя: '))

        new_name = str(input('Новое Имя: '))

        data = {}

        for item in list:
            value = float(input(item + ' : '))

            data.update({item: value})

        dictionaryNames.pop(old_name)

        dictionaryNames.update({new_name: data})

    if answer == 1:

        name = str(input('Имя: '))

        count = 0

        for key in dictionaryNames[name]:
            count += 1

            print(count, ' - ', key, ' - ', dictionaryNames[name][key])

        index = int(input('Значение которое хотите изменить : '))

        value = int(input('Введите новое значение : '))

        key = ''

        count = 0

        for iKey in dictionaryNames[name]:

            count += 1

            if count == index:
                key = iKey

        dictionaryNames[name].update({key: value})

        print(dictionaryNames)


def funk_find():
    print(dictionaryNames)

    name = (input('Введите имя для поиска : '))

    print(dictionaryNames[name])


def funk_output():
    for player in dictionaryNames:

        print(player, ' - ', end='')

        for item in dictionaryNames[player]:
            print(item, '-', dictionaryNames[player][item], end=' ')

        print()


while True:

    menu = ('Добавить', 'Удалить', 'Изменить', 'Найти', 'Вывести всех баскетболистов')

    count = 0

    print('-------------------------------------------------------------------------------')

    for i in menu:
        count += 1

        print(count, " - ", i)

    print()

    x = int(input('Выберите действие которое вы хотите выполнить: '))

    if x == 1:

        funk_add()

    elif x == 2:

        funk_delete()

    elif x == 3:

        funk_edit()

    elif x == 4:

        funk_find()

    elif x == 5:

        funk_output()

    else:

        break

#2 Создайте программу «Англо-французский словарь».
#Нужно хранить слово на английском языке и его перевод
#на французский. Требуется реализовать возможность добавления, удаления, поиска, замены данных. Используйте
#словарь для хранения информации.
dict = {
    'apple': 'Pomme',
    'snake': 'serpent',
    'foot cream': 'crème pour les pieds'
}
print("=" * 10, "Словарь v.1.0", "=" * 10)
help = """
s = Искать слово
a = Добнуть слово
r = Делитнуть слово
k = Вывод всех ключей в словаре
d = Вывод всего словаря
q = Завершить
"""
choice = ""
while choice != "q":
    choice = input("(h - Словарь >>) ")
    if choice == "s":
        word = input("Введите слово:")
        res = dict.get(word, "Чо за слово? Нет такого")
        print(res)
    elif choice == "a":
        world = input("Введите слово: ")
        value = input("Введите перевод: ")
        dict[word] = value
        print("Слово добавлено!")
    elif choice == "r":
        word = input("Введите слово:")
        del dict[world]
        print("Слово", world, "Удалено")
    elif choice == "k":
        print(dict.keys())
    elif choice == "d":
        for i in dict:
            print(i, ":", dict[i])
    elif choice =="h":
        print(help)
    elif choice == "q":
        continue
    else:
        print("Нет такой команды, введите h для вывода меню")


#3 Создайте программу «Фирма». Нужно хранить информацию о человеке: ФИО, телефон, рабочий email,
#название должности, номер кабинета, skype. Требуется
#реализовать возможность добавления, удаления, поиска, замены данных. Используйте словарь для хранения
#информации.
mydict = {
    'Артем Геннадьевич Никитин': ['+3809488764', 'artemnikitin@gmail.com', '№1', 'Бухгалтер', '@artem']
}

print("=" * 10, "Словарь v.1.0", "=" * 10)
commands = """0 = Добавить работника или изменить его данные
1 = Удаление информации
2 = Поиск
h = Вывести данное сообщение
q = Завершить"""
print(commands)
while True:
    choice = input(">> ")
    if choice == "0":
        word = input("Введите фио работника: ")
        values = input("Введите номер, E-Mail, номер кабинета, должность и скайп работника через пробел:\n>>").split()
        mydict[word] = values
        print("Успешно!")
    elif choice == "1":
        word = input("Введите фио работника: ")
        if word in mydict.keys():
            del mydict[word]
            print("Успешно")
        else:
            print("Работник не найден")
    elif choice == "2":
        word = input("Кого ищем?: ")
        if word in mydict.keys():
            print("""Работник {}:
Номер телефона: {}
E-Mail: {}
Номер кабинета: {}
Должность: {}
Skype: {}""".format(word, *mydict[word]))
        else:
            print("Работник не найден")
    elif choice == "h":
        print(commands)
    elif choice == "q":
        exit()
    else:
        print("Нет такой команды, введите h для вывода меню")


#4 Создайте программу «Книжная коллекция». Нужно
#хранить информацию о книгах: автор, название книги,
#жанр, год выпуска, количество страниц, издательство.
#Требуется реализовать возможность добавления, удаления, поиска, замены данных. Используйте словарь для
#хранения информации.


mydict = {
    'Копирайтинг в алгоритмах': ['Ирина Костюченко', 'скетч','2021', '450', 'IPIO']
}

print("=" * 10, "Словарь v.1.0", "=" * 10)
commands = """0 = Добавить книгу или изменить данные
1 = Удаление информации
2 = Поиск
h = Вывести данное сообщение
q = Завершить"""
print(commands)
while True:
    choice = input(">> ")
    if choice == "0":
        word = input("Введите название: ")
        values = input("Введите, название, автора, жанр и год выпуска книги через пробел:\n>>").split()
        mydict[word] = values
        print("Успешно!")
    elif choice == "1":
        word = input("Введите название: ")
        if word in mydict.keys():
            del mydict[word]
            print("Успешно")
        else:
            print("Не найдено")
    elif choice == "2":
        word = input("Кокую книгу ищем?: ")
        if word in mydict.keys():
            print("""Книга {}:
Название книги: {}
Автор: {}
Жанр: {}
Год выпуска: {}
Количество страниц:{}
Издательство:     {}""".format(word, *mydict[word]))
        else:
            print("Работник не найден")
    elif choice == "h":
        print(commands)
    elif choice == "q":
        exit()
    else:
        print("Нет такой команды, введите h для вывода меню")


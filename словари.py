# Есть некоторый словарь, который хранит названия
# стран и столиц. Название страны используется в качестве
# ключа, название столицы в качестве значения. Необходимо
# реализовать: добавление данных, удаление данных, поиск
# данных, редактирование данных, сохранение и загрузку
# данных (используя упаковку и распаковку).

import pickle as french_fries

def add_or_change(dictionary: dict):
    data = input('saved successfully').split()
    dictionary[data[0]] = data[1]

def remove_from(dictionary: dict):
    key = input('Enter the key to delete')
    del dictionary[key]

def search(dictionary: dict):
    key = input('Enter search key')
    if key in dictionary.keys():
        print(f"Столица страны {key}: {dictionary.get(key)}")

def save(dictionary: dict):
    with open('example.txt', 'wb') as file:
        french_fries.dump(dictionary, file)
        print("saved successfully!")

def load(_):
    with open('example.txt', 'rb') as file:
        print(french_fries.load(file))

countries = {'Ukraine': 'Kyiv', 'Poland': 'Warsaw', 'USA': 'Washington'}

print("1 - изменить или добавить данные\n"
      "2 - удалить данные\n"
      "3 - найти данные\n"
      "4 - сохранить данные\n"
      "5 - загрузить данные"
      "6 - выйти")
while True:
    userFunction = input(">> ")
    if userFunction == "1":
        add_or_change(countries)
    elif userFunction == "2":
        remove_from(countries)
    elif userFunction == "3":
        search(countries)
    elif userFunction == "4":
        save(countries)
    elif userFunction == "5":
        load(countries)
    elif userFunction == "6":
        print("bye!")
        exit()
    else:
        print("invalid command.")

# Есть некоторый словарь, который хранит названия
#музыкальных групп(исполнителей) и альбомов. Название группы используется в качестве ключа, название
#альбомов в качестве значения. Необходимо реализовать:
#добавление данных, удаление данных, поиск данных,
#редактирование данных, сохранение и загрузку данных
#(используя упаковку и распаковку).

import pickle as french_friers

def add_or_change(dictionary: dict):
    data = input('Введите ключ, значение через пробел').split()
    dictionary[data[0]] = data[1]

def remove_from(dictionary: dict):
    key = input('Введите ключ для удаления')
    del dictionary[key]

def search(dictionary: dict):
    key = input('Введите ключ чтобы искать')
    if key in dictionary.keys():
        print(f'Музыкальный исполнитель или группа {key}: {dictionary.get(key)}')

def save(dictionary: dict):
    with open('example.txt', 'wb') as file:
        french_fries.dump(dictionary, file)
        print("Успешно сохранено!")

def load(_):
    with open('example.txt', 'rb') as file:
        print(french_fries.load(file))

performes = {'Face': 'Liza', 'Cold carti': 'Свет', 'Вышел покурить': 'Память'}

print("1 - изменить или добавить данные\n"
      "2 - удалить данные\n"
      "3 - найти данные\n"
      "4 - сохранить данные\n"
      "5 - загрузить данные"
      "6 - выйти")
while True:
    userFunction = input(">> ")
    if userFunction == "1":
        add_or_change(countries)
    elif userFunction == "2":
        remove_from(countries)
    elif userFunction == "3":
        search(countries)
    elif userFunction == "4":
        save(countries)
    elif userFunction == "5":
        load(countries)
    elif userFunction == "6":
        print("Bye!")
        exit()
    else:
        print("invalid command.")

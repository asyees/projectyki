# Практическая работа 2:
# Задание 1.
# Есть некоторый словарь, который хранит названия
# стран и столиц. Название страны используется в качестве
# ключа, название столицы в качестве значения. Необходимо
# реализовать: добавление данных, удаление данных, поиск
# данных, редактирование данных, сохранение и загрузку
# данных (используя упаковку и распаковку pickle).

import pickle as french_fries


def add_or_change(dictionary: dict):
    data = input('Введите пару ключ-значение через пробел').split()
    dictionary[data[0]] = data[1]


def remove_from(dictionary: dict):
    key = input('Введите ключ для удаления')
    del dictionary[key]


def search(dictionary: dict):
    key = input('Введите ключ для поиска')
    if key in dictionary.keys():
        print(f"Столица страны {key}: {dictionary.get(key)}")


def save(dictionary: dict):
    with open('example.txt', 'wb') as file:
        french_fries.dump(dictionary, file)
        print("Успешно сохранено!")


def load(_):
    with open('example.txt', 'rb') as file:
        print(french_fries.load(file))


countries = {'Ukraine': 'Kyiv', 'Germany': 'Berlin', 'French': 'Parij'}

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
        print("До свидания!")
        exit()
    else:
        print("Неверная команда.")

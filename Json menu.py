
import json

def display_menu(): # Функция для отображения меню 
    print('\nДобро пожаловать в программу Словарь!\n')
    print('1. Добавить слово и его толкование')
    print('2. Заменить толкование слова')
    print('3. Удалить слово или толкование')
    print('4. Найти толкование слова')
    print('5. Экспортировать результаты')
    print('6. Выход \n')  

def add_word_meanings(dictionary): # Функция для добавления слова и его толкования в словарь
    word = input('Введите слово: ')
    meanings = []
    while True:
        meaning = input('Введите толкование слова (или нажмите Enter для завершения): ')
        if meaning == '':
            break
        meanings.append(meaning)
    if word in dictionary:
        dictionary[word] += meanings
    else:
        dictionary[word] = meanings
   
def replace_word_meanings(dictionary): # Функция, чтобы заменить слово или его толкование в словаре
    word = input('Введите слово: ')
    if word in dictionary:
        meanings = []
        for meaning in dictionary[word]:
            replace = input(f'Заменить толкование "{meaning}"? (Д/Н): ')
            if replace.upper() == 'Д':
                m = input('Введите новое толкование: ')
                meanings.append(m)
            else:
                meanings.append(meaning)
        dictionary[word] = meanings
        
def delete_word_meanings(dictionary): # Функция для удаления слова или толкования из словаря
    word = input('Введите слово: ')
    if word in dictionary:
        for meaning in dictionary[word]:
            delete = input(f'Удалить толкование "{meaning}"? (Д/Н): ')
            if delete.upper() == 'Д':
                dictionary[word].remove(meaning)
        if len(dictionary[word]) == 0:
            del dictionary[word]
        
def search_word_meanings(dictionary): # Функция, чтобы найти толкование слова
    word = input('Введите слово: ')
    if word in dictionary:
        print(f'\nТолкование слова "{word}"')
        for meaning in dictionary[word]:
            print('- ' + meaning)
    else:
        print(f'\nТолкование слова "{word}" не найдено.')
        
def export_results(dictionary): # Функция для экспорта словаря в файл результата
    with open('dictionary.json', 'w') as f:
        json.dump(dictionary, f)
    print('\nРезультаты успешно экспортированы в файл "dictionary.json".')

def main(): # Главная функция программы
    dictionary = {} # Создадим словарь 
    while True:
        display_menu() # Отобразить меню 
        choice = input('Выберите действие: ')
        if choice == '1': # Добавить слово и его толкование
            add_word_meanings(dictionary)
        elif choice == '2': # Заменить толкование слова
            replace_word_meanings(dictionary)
        elif choice == '3': # Удалить слово или толкование
            delete_word_meanings(dictionary)
        elif choice == '4': # Найти толкование слова
            search_word_meanings(dictionary)
        elif choice == '5': # Экспортировать результаты
            export_results(dictionary)
        elif choice == '6': # Выход
            break
        else:
            print('Неверный пункт меню!')


if __name__ == '__main__':
    main()








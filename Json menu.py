
import json

def display_menu(): # ������� ��� ����������� ���� 
    print('\n����� ���������� � ��������� �������!\n')
    print('1. �������� ����� � ��� ����������')
    print('2. �������� ���������� �����')
    print('3. ������� ����� ��� ����������')
    print('4. ����� ���������� �����')
    print('5. �������������� ����������')
    print('6. ����� \n')  

def add_word_meanings(dictionary): # ������� ��� ���������� ����� � ��� ���������� � �������
    word = input('������� �����: ')
    meanings = []
    while True:
        meaning = input('������� ���������� ����� (��� ������� Enter ��� ����������): ')
        if meaning == '':
            break
        meanings.append(meaning)
    if word in dictionary:
        dictionary[word] += meanings
    else:
        dictionary[word] = meanings
   
def replace_word_meanings(dictionary): # �������, ����� �������� ����� ��� ��� ���������� � �������
    word = input('������� �����: ')
    if word in dictionary:
        meanings = []
        for meaning in dictionary[word]:
            replace = input(f'�������� ���������� "{meaning}"? (�/�): ')
            if replace.upper() == '�':
                m = input('������� ����� ����������: ')
                meanings.append(m)
            else:
                meanings.append(meaning)
        dictionary[word] = meanings
        
def delete_word_meanings(dictionary): # ������� ��� �������� ����� ��� ���������� �� �������
    word = input('������� �����: ')
    if word in dictionary:
        for meaning in dictionary[word]:
            delete = input(f'������� ���������� "{meaning}"? (�/�): ')
            if delete.upper() == '�':
                dictionary[word].remove(meaning)
        if len(dictionary[word]) == 0:
            del dictionary[word]
        
def search_word_meanings(dictionary): # �������, ����� ����� ���������� �����
    word = input('������� �����: ')
    if word in dictionary:
        print(f'\n���������� ����� "{word}"')
        for meaning in dictionary[word]:
            print('- ' + meaning)
    else:
        print(f'\n���������� ����� "{word}" �� �������.')
        
def export_results(dictionary): # ������� ��� �������� ������� � ���� ����������
    with open('dictionary.json', 'w') as f:
        json.dump(dictionary, f)
    print('\n���������� ������� �������������� � ���� "dictionary.json".')

def main(): # ������� ������� ���������
    dictionary = {} # �������� ������� 
    while True:
        display_menu() # ���������� ���� 
        choice = input('�������� ��������: ')
        if choice == '1': # �������� ����� � ��� ����������
            add_word_meanings(dictionary)
        elif choice == '2': # �������� ���������� �����
            replace_word_meanings(dictionary)
        elif choice == '3': # ������� ����� ��� ����������
            delete_word_meanings(dictionary)
        elif choice == '4': # ����� ���������� �����
            search_word_meanings(dictionary)
        elif choice == '5': # �������������� ����������
            export_results(dictionary)
        elif choice == '6': # �����
            break
        else:
            print('�������� ����� ����!')


if __name__ == '__main__':
    main()








#Есть четыре списка целых. Необходимо объединить
#в пятом списке только те элементы, которые уникальны
#для каждого списка. Полученный результат в зависимости
#от выбора пользователя отсортировать по убыванию или
#возрастанию. Найти значение, введенное пользователем,
#с использованием бинарного поиска.
def binary_search(lst, number):
    mid = len(lst) // 2
    low = 0
    high = len(lst) - 1

    while lst[mid] != number and low <= high:
        if number > lst[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2

    if low > high:
        return -1
    else:
        return mid


list_1 = [2, 50, 50, 50, 2, 6, 7]
list_2 = [5, 5, 6, 50]
list_3 = [5, 8, 12, 24, 50]
list_4 = [3, 10, 5, 7, 50]
list_5 = list(set(tuple(set(list_1) ^ set(list_2)) + tuple(set(list_2) ^ set(list_3)) + tuple(set(list_3) ^ set(list_4))))
print(list_5)
useritem = int(input("Какое число найти в списке?: "))
result = binary_search(list_5, useritem)
if result == -1:
    print("Элемент не найден")
else:
    print(f"Число: {list_5[result]}. Его индекс: {result}")

#Есть четыре списка целых. Необходимо их объединить
#в пятом списке. Полученный результат в зависимости от
#выбора пользователя отсортировать по убыванию или
#возрастанию. Найти значение, введенное пользователем,
#с использованием линейного поиска.

ef linear_search(lst, search_item):
    for i in range(len(lst)):
        if lst[i] == search_item:
            return lst[i]
    return -1


list_a = [10, 40, 30, 20]
list_b = [50, 60, 70, 80]
list_c = [90, 100, 200, 300]
list_d = [400, 500, 600, 700]
list_i = list_a + list_b + list_c + list_d
print(list_i)

print("0 - отсортировать по возрастанию, 1 - по убыванию")
select = input()
if select == "0":
    print(sorted(list_i))
elif select == "1":
    print(sorted(list_i, reverse=True))

print("Введите число, которое хотите найти в списке")
selected_item = int(input())
result = linear_search(list_i, selected_item)
if result == -1:
    print('Элемент не найден')
else:
    print(f'Элемент {result} найден. Его индекс: {list_i.index(result)}')
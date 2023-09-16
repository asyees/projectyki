
#Дан текстовый файл. Необходимо переписать его
# строки в другой файл. Порядок строк во втором файле
# должен совпадать  с порядко строк в заданном файле.
with open('testAlise.txt') as file:
    lines = [line.rstrip()[::-1] + '\n' for line in file.readlines()]

#Дан текстовый файл. Необходимо переписать его
# строки в другой файл. Порядок строк во втором файле
#должен быть обратным по отношению к порядку строк  # в заданном файле.
with open("testAlise.txt", "r", encoding="utf-8") as f1, open("test.txt", "w+", encoding="utf-8") as f2:
    for i in reversed(f1.readlines()):
        f2.write(i)



#дан текстовый файл. Добавить в него строку из двенадцати звездочек (************), поместив ее после последней
# из строк, в которых нет запятой. Если таких строк нет,
# то новая строка должна быть добавлена после всех строк
# имеющегося файла. Результат записать в другой файл.
with open("testAlise.txt", "r", encoding="utf-8") as f1, open("test.txt", "w+", encoding="utf-8") as f2:
    for i in f1.readlines():
        if "," not in i and i != "\n":
            f2.write(i + "************\n")
        else:
            f2.write(i)
    f1.seek(0)
    if "," not in f2.read():
        f2.write("\n************")

#Дан текстовый файл. Подсчитать количество слов,
# начинающихся с символа, который задаёт пользователь.
char = input("С какого символа должно начинаться слово?: ")
with open("testAlise.txt", "r", encoding="utf-8") as file:
    result = len(re.findall(r"\b{}\w+".format(char), file.read()))
    print("Слова на букву", char, "встречаются в строке", result, "раз"
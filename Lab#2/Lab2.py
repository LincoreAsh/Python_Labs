"""
Гайнутдинов Ильдар ИСТбд-12
Вариант 21. Написать программу, которая читая последовательность чисел из файла,
выводит на экран четные числа на нечетных местах(индексы начинаются с нуля).
После каждого числа выводится, номер символа в последовательности (цифры, а не числа),
с которого начинается число и количество цифр в нем.
"""
import time
buffer_len = 1  # размер буфера чтения
number = ""
digit = ""
index_count, digits_num, index, posledov_num = 0, [], [], []
print("-----Результат работы программы-----\n -----Локальное время", time.ctime(), "-----")
start = time.time()
with open("text.txt", "r") as file:   # открываем файл
    buffer = file.read(buffer_len)   # читаем первый блок
    if not buffer:  # если файл пустой
        print("\nФайл text.txt в директории проекта пустой.\nДобавьте не пустой файл в директорию или переименуйте существующий *.txt файл.")
    while buffer: # пока файл не пустой
        while (buffer < '0' or buffer > '9')  and buffer:  #ищем цифры
            buffer = file.read(buffer_len)   # читаем очередной блок
        while (buffer >= '0' and buffer <= '9' or buffer == " " or buffer == ".") and buffer:  #обрабатываем цифры
            number += buffer
            digit += number
            buffer = file.read(buffer_len)  # читаем очередной блок
            number = ""  # готовим переменные для нового цикла
    text = digit.split()
    for value in text:
        try:
            try:
                value = int(value)
            except:
                value = float(value)
        except:
            print("Во входном файле при обработке числа встретился лишний символ точки. Возможна неоднозначная интерпретация. Откорректируйте входной файл")
            quit()
        digits_num.append(len(str(abs(value)).replace(".","")))  #Количество цифр в числе
        posledov_num.append(value)
        index.append(index_count)  # Подсчет номера символа, с которого начинается число
        index_count = index_count + len(str(abs(value)).replace(".","")) + 1
    for x in range(len(text))[::-1]:  # Удаление нечетных чисел на четных местах
        try:
            text[x] = int(text[x])
        except:
            text[x] = float(text[x])
        if not (x % 2 and not text[x] % 2):
            del (text[x], posledov_num[x], digits_num[x], index[x])
    if len(text) > 0:
        for i in range(len(text)):
            print("Число =", posledov_num[i], "; Номер символа в последовательности, с которого начинается число =",index[i], "; Количество цифр в числе =", digits_num[i])
    else:
        print("В файле нет чисел")
print("Program time: {:>.10f}".format(time.time() - start) + " seconds.")

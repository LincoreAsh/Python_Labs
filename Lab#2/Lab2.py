"""Написать программу, которая читая последовательность чисел из файла, выводит на экран четные числа на нечетных
местах. После каждого числа выводится, номер символа в последовательности (цифры, а не числа), с которого начинается
число и количество цифр в нем. """
import time, json, random
from random import randint
start = time.time()
rnd_length = [10, 100, 1000, 10000, 100000]  # Массив для случайной длины числа
text = [randint(1, random.choice(rnd_length)) for i in range(1000)]  # Заполнение массива случайными числами
with open('input.txt', 'w') as fw:  # Запись случайных чисел в файл, если его нету, он создаётся
    json.dump(text, fw)
with open("input.txt", 'r') as fr:  # Читаем файл
    text = json.load(fr)
print("Исходная последовательность:", *text, "\nПолученная последовательность: ")
count, index_count, digits_num, index, posledov = 0, 0, [], [], []
for value in text:
    sum = 0
    v = value
    posledov.append(v)
    while v:  # Подсчет количества цифр в числе
        sum += 1
        v //= 10
    digits_num.append(sum)
    index.append(index_count)  # Подсчет номера символа, с которого начинается число
    index_count = index_count + sum + 1
for x in range(len(text))[::-1]:  # Удаление нечетных чисел на четных местах
    if not (not text[x] % 2 and x % 2):
        del (text[x], posledov[x], digits_num[x], index[x])
for x in text:
    print("Число =", posledov[count], "; Номер символа в последовательности, с которого начинается число =",
          index[count],
          "; Количество цифр в числе =", digits_num[count])
    count += 1
print("Program time: {:>.10f}".format(time.time() - start) + " seconds.")

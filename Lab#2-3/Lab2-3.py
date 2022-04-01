"""
Гайнутдинов Ильдар ИСТбд-12
Вариант 21. Написать программу, которая читая последовательность чисел из файла,
выводит на экран четные числа на нечетных местах(индексы начинаются с нуля).
После каждого числа выводится, номер символа в последовательности (цифры, а не числа),
с которого начинается число и количество цифр в нем.
"""
import time
import cProfile
def task():
    buffer_len = 1  # размер буфера чтения
    number = ""
    digit = ""
    count, index_count, digits_num, index, posledov_num = 0, 0, [], [], []
    print("-----Результат работы программы-----\n -----Локальное время", time.ctime(), "-----")
    start = time.time()
    try:
        with open("input.txt", "r") as file:   # открываем файл
            buffer = file.read(buffer_len)   # читаем первый блок
            if not buffer:  # если файл пустой
                print("\nФайл input.txt в директории проекта пустой.\nДобавьте не пустой файл в директорию или переименуйте существующий *.txt файл.")
            while buffer: # пока файл не пустой
                while (buffer < '0' or buffer > '9' or buffer == " ") and buffer:  #ищем цифры
                    buffer = file.read(buffer_len)   # читаем очередной блок
                while (buffer >= '0' and buffer <= '9' or buffer == " ") and buffer:  #обрабатываем цифры
                    number += buffer
                    digit += number
                    buffer = file.read(buffer_len)  # читаем очередной блок
                    number = ""  # готовим переменные для нового цикла

            text = list(map(int, digit.split()))
            print(*text)
            for value in text:
                sum = 0
                v = value
                posledov_num.append(v)
                while v:  # Подсчет количества цифр в числе
                    sum += 1
                    v //= 10
                digits_num.append(sum)
                index.append(index_count)  # Подсчет номера символа, с которого начинается число
                index_count = index_count + sum + 1
            for x in range(len(text))[::-1]:  # Удаление нечетных чисел на четных местах
                if not (x % 2 and not text[x] % 2):
                    del (text[x], posledov_num[x], digits_num[x], index[x])
            if len(text) > 0:
                for i in range(len(text)):
                    print("Число =", posledov_num[count], "; Номер символа в последовательности, с которого начинается число =",index[x], "; Количество цифр в числе =", digits_num[x])
            else:
                print("В файле нет чисел")
    except FileNotFoundError:
        print("Error \nФайл input.txt в директории проекта не обнаружен. \nДобавьте файл в директорию или переименуйте существующий *txt файл")
        quit()
    print("Program time: {:>.10f}".format(time.time() - start) + " seconds.")

def main():
    task()
if __name__ == '__main__':
    cProfile.run('main()')

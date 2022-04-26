""" 21.	Формируется матрица F следующим образом: если в В количество нулей в нечетных столбцах в области 3 больше,
чем сумма чисел в четных строках в области 1, то поменять в С симметрично области 2 и 3 местами, иначе В и Е поменять
местами несимметрично. При этом матрица А не меняется. После чего вычисляется выражение: A*F-K*F T . Выводятся по мере
формирования А, F и все матричные операции последовательно.
"""
import random
import time


def print_matrix(M, matr_name, tt):
    print("матрица " + matr_name + " промежуточное время = " + str(format(tt, '0.2f')) + " seconds.")
    for i in M:  # делаем перебор всех строк матрицы
        for j in i:  # перебираем все элементы в строке
            print("%5d" % j, end=' ')
        print()


print("\n-----Результат работы программы-------")
try:
    row_q = int(input("Введите количество строк (столбцов) квадратной матрицы в интервале от 6 до 100:"))
    while row_q < 6 or row_q > 100:
        row_q = int(input(
            "Вы ввели неверное число\nВведите количество строк (столбцов) квадратной матрицы в интервале от 6 до 100:"))
    K = int(input("Введите число К="))
    start = time.time()
    A, F, AF, FT = [], [], [], []  # задаем матрицы
    for i in range(row_q):
        A.append([0] * row_q)
        F.append([0] * row_q)
        AF.append([0] * row_q)
        FT.append([0] * row_q)
    time_next = time.time()
    print_matrix(F, "F", time_next - start)

    for i in range(row_q):  # заполняем матрицу А
        for j in range(row_q):
            #A[i][j] = random.randint(-5,5)
            if i < j and j < row_q - 1 - i:
                A[i][j] = 1
            elif i < j and j > row_q - 1 - i:
                A[i][j] = 2
            elif i > j and j > row_q - 1 - i:
                A[i][j] = 3
            elif i > j and j < row_q - 1 - i:
                A[i][j] = 4

    time_prev = time_next
    time_next = time.time()
    print_matrix(A, "A", time_next - time_prev)
    for i in range(row_q):  # F
        for j in range(row_q):
            F[i][j] = A[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(F, "F", time_next - time_prev)

    B = []  # задаем матрицу B
    size = row_q // 2
    for i in range(size):
        B.append([0] * size)

    for i in range(size):  # формируем подматрицу B
        for j in range(size):
            B[i][j] = F[i][size + row_q % 2 + j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(B, "B", time_next - time_prev)

    count3 = 0
    count1 = 0
    for i in range(size):  # обрабатываем подматрицу B
        for j in range(i + 1, size, 1):
            if j % 2 == 1 and j < size - 1 - i and B[i][j] == 0:
                count3 += 1
            elif j % 2 != 0 and i > j and j > size - 1 - i:
                count1 += B[i][j]

    if count3 > count1:
        for i in range(1, size // 2, 1):  # меняем подматрицу С
            for j in range(size - 1, i, -1):
                B[i][j], B[j][i] = B[j][i], B[i][j]
        for i in range(size // 2, size, 1):
            for j in range(size // 2, i, 1):
                B[i][j], B[j][i] = B[j][i], B[i][j]
        print_matrix(B, "B6", time_next - time_prev)
        for i in range(size):  # формируем матрицу F
            for j in range(size):
                F[i][size - row_q % 2 + j] = B[i][j]
        print_matrix(F, "F!", time_next - time_prev)

    else:
        for j in range(row_q // 2):
            for i in range(row_q // 2):
                F[i][j], F[row_q // 2 + row_q % 2 + i][row_q // 2 + row_q % 2 + j] = F[row_q // 2 + row_q % 2 + i][row_q // 2 + row_q % 2 + j], F[i][j]

    time_prev = time_next
    time_next = time.time()
    print_matrix(F, "F", time_next - time_prev)
    print_matrix(A, "A", 0)

    for i in range(row_q):  # A*F
        for j in range(row_q):
            s = 0
            for m in range(row_q):
                s = s + A[i][m] * F[m][j]
            AF[i][j] = s
    time_prev = time_next
    time_next = time.time()
    print_matrix(AF, "A*F", time_next - time_prev)

    for i in range(row_q):  # FT
        for j in range(i, row_q, 1):
            FT[i][j], FT[j][i] = F[j][i], F[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(FT, "F^T", time_next - time_prev)

    for i in range(row_q):  # K*AT
        for j in range(row_q):
            A[i][j] = K * FT[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(F, "K*F^T", time_next - time_prev)

    for i in range(row_q):  # (F*A)-(K*AT)
        for j in range(row_q):
            AF[i][j] = AF[i][j] - A[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(AF, "A*F-K*FT", time_next - time_prev)

    finish = time.time()
    result = finish - start
    print("Program time: " + str(result) + " seconds.")

except ValueError:
    print("\nэто не число")

except FileNotFoundError:
    print(
        "\nФайл text.txt в директории проекта не обнаружен.\nДобавьте файл в директорию или переименуйте существующий *.txt файл.")

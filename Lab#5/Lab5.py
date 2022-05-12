import numpy as np
import random
import time

print (time.ctime())

N = int(input("Введите N > 3\n"))
while N < 4:
    N = int(input("Недопустмое значение N\nВведите N > 3\n"))
size = N // 2
K = int(input("Введите K\n"))

start = time.time()

A = np.zeros((N, N), dtype = int) #Задаём матрицы А и Ф = 0
F = np.zeros((N, N), dtype = int)

for i in range (N): #Задаём матрицу А
    for j in range (N):
        A[i][j] = random.randint(-10,10)

print ("\nMatrix A:")
for i in A:
    for j in i:
        print ("%5d" % j, end = ' ')
    print () #

for i in range (N): #Задаём матрицу Ф = А
    for j in range (N):
        F[i][j] = A[i][j]

print ("\nMatrix F:")
for i in F:
    for j in i:
        print ("%5d" % j, end = ' ')
    print ()

B = np.zeros((size, size), dtype = int) #Задаём матрицу B
null_count = 0
summ = 0

for i in range (size):
    for j in range (size):
        if N % 2 == 0:
            B[i][j] = F[i][j + size]
        else:
            B[i][j] = F[i][j+size+1]
        if j % 2 != 0 and B[i][j] == 0:
            null_count += 1
        if (i+1) % 2 == 0:
            summ += B[i][j]

print ("\nMatrix B:")
for i in B:
    for j in i:
        print ("%5d" % j, end = ' ')
    print ()
print ("\nКол-во нулей в нечетных столбцах =", null_count, "\nСумма чисел в четных строках =", summ)

if null_count < summ:
    for i in range (size):
        for j in range (size):
            F[i][j + size + N % 2], F[N - 1 - i][j + size + N % 2] = F [N - 1 - i][j + size + N % 2], F[i][j + size + N % 2]
else:
    for i in range (size):
        for j in range (size):
            F[i][j+size], F[i][j] = F[i][j], F[i][j+size]

print ("\nMatrix F(modified):")
for i in F:
    for j in i:
        print ("%5d" % j, end = ' ')
    print ()

if np.linalg.det(A) == 0 or np.linalg.det(F) == 0:
    print ("Матрица A или F вырождена. Вычисления невозможны")
    quit()

elif np.linalg.det(A) > np.trace(F):
    Matrix = (((np.linalg.inv(A)).dot(np.transpose(A))) - (np.transpose(F) * K))  # A-1*AT – K * FТ
else:
    Matrix = (np.transpose(A) + np.tril(A) - np.linalg.inv(F)-1) * K #(AТ +G-F-1)*K



print ("\nCalculations Matrix:")
for i in Matrix:
    for j in i:
        print ("%5d" % j, end = ' ')
    print ()

finish = (time.time() - start)
print ("\n", "Time", finish, "seconds")

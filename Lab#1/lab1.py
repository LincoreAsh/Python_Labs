from random import randint
n,m = 4,5
mas = [[randint(1, 9) for i in range(n)] for j in range(m)]
max = mas[0][0]
vec = []
print(mas)

for i in range (m):
    s=0
    for j in range (n):
        if mas[i][j] > max and mas[i][j] % 2 == 1:
            max = mas[i][j]
        s+=mas[i][j]
    vec.append(s)

print("Максимальное нечетное число =", max)
print("Вектор D =", vec)

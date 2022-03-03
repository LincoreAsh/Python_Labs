with open("input.txt") as file:
  n = file.read().split()
  n = list(map(int, n))
  print(*n)
l, ind = len(n), 0

for x in range(len(n))[::-1]:
  if not (not n[x] % 2 and x%2):
    del(n[x])

print("Полученная последовательность чисел =", *n)

for value in n:
    s = 0
    v = value
    while v:
        s += 1
        v //= 10
    print(value, "- Номер символа в последовательности, с которого начинается число =", ind, "- Количество цифр в числе =", s)
    ind = ind+s+1

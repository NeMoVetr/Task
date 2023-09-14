# Задача 22 можно использовать пересечение или объединение

# Задача 24 1 2 3 4 если надо зацепить 1 то так как оин стоят по кругу то надо захвататить и 4

# максимум из всех подряд идущих троек

mass1 = []
mass2 = []
print("Введите числа m и n:")
n = int(input())
m = int(input())
print("Введите значения 1 го массива:")
for i in range(n):
    mass1.append(int(input()))
print("Введите значения 2 го массива:")
for i in range(m):
    mass2.append(int(input()))
mass1 = set(mass1)
mass2 = set(mass2)
print(*sorted(mass1.intersection(mass2)))

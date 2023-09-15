print("Введите кол-во кустов:")
n = int(input())
print("Введите кол-во ягод:")
mass = []
mass1 = []
sum = 0
summ = []
for i in range(n):
    mass.append(int(input()))

for i in range(n):
    mass1.append(mass[i:i + 3])

for i in mass1:
    if len(i) == 3:
        for j in i:
            sum += j
        summ.append(sum)
        sum = 0
    if len(i) == 2:
        sum = mass1[0][0]
        for j in i:
            sum += j
        summ.append(sum)
        sum = 0
    if len(i) == 1:
        sum = mass1[0][1]+mass1[0][0]
        for j in i:
            sum += j
        summ.append(sum)
        sum = 0
print(max(summ))

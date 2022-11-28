#2. В данной действительной квадратной матрице порядка n найти наибольший по модулю элемент. Получить квадратную матрицу порядка 
#n — 1 путем отбрасывания из исходной матрицы строки и столбца, на пересечении которых расположен элемент с найденным значением.

import random as rd
import math

a=int(input("Введите значение квадратной матрицы: "))
mas=[] 
for i in range(a):
    mas.append([0]*a) 

for i in range(len(mas)): 
    for j in range(len(mas[i])):
        mas[i][j]=rd.randint(-50,50)

print("Массив: ")
for i in range(a): 
    for j in range(a):
        print(mas[i][j], end = ' ')
    print()

max=math.fabs(mas[0][0]) 
for i in range(len(mas)): 
    for j in range(len(mas[i])):
       if math.fabs(max)<math.fabs(mas[i][j]):
        max=(mas[i][j])
        stroka=i
        stolbec=j
print("Номер строки: %s " %stroka, end='\n')
print("Номер столбца: %s " %stolbec, end='\n')
print("Максимальное значение в матрице по модулю: %s"  %max)

mas1=[[0 for x in range(a-1)] for y in range(a-1)]


del mas[stroka] 
for i in range(len(mas)):
    del mas[i][stolbec]


print("Массив: ")
for i in range(a-1): 
    for j in range(a-1):
        print(mas[i][j], end = ' ')
    print()

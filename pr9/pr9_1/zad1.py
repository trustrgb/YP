n=int(input("Введите значение квадратной матрицы: ")) 
with open('vvod.txt', 'r') as file: 
    mas1 = []
    for mas1_line in file.readlines():
        line = mas1_line.split()
        mas1 += line
    mas1 = list(map(int, mas1))

mas = []
for l in range(n):
    line = [mas1.pop(0) for l in range(n)]
    mas.append(line)
    
print(mas)

print("Массив: ")
for i in range(n): 
    for j in range(n):
        print(mas[i][j], end = ' ')
    print()

max=mas[0][0] 
for i in range(len(mas)): 
    for j in range(len(mas[i])):
       if max<mas[i][j]:
        max=mas[i][j]
print("Максимальное значение в матрице: %s"  %max)

k=int(input('Введите кратное число "k": '))
l=0
for i in range(len(mas)): 
    for j in range(len(mas[i])):
            if mas[i][j]%k==0:
                l+=1
print("Кол-во чисел кратных k: %s" %l)

file2 = open('vivod.txt', 'w') 
for i in range(n):
    for j in range(n):
        a = str(mas[i][j])
        file2.write(a)
        file2.write(' ')
file2.close()
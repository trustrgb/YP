#Даны массивы A и B одинакового размера 10. Вывести исходные массивы. 
#Поменять местами их содержимое и вывести в начале элементы 
#преобразованного массива A, а затем — элементы преобразованного массива B
a=[77, 35, 18, 7, 1, 11, 74, 98, 90, 10];
b=[123, 73, 98, 1, 2, 3, 4, 5, 6, 76];
print(a);
print(b);
a, b = b, a;
print(a);
print(b);

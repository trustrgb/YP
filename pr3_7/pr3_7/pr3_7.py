a = int(input())
b = int(input())
x = 0;
if a < b and b > 4:
    x = a + b
    print(x)
elif a > b:
    x = a - b
    print(x)
else:
    x = pow(a,2)
    print(x)
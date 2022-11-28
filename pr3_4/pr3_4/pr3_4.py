a = int(input())
b = int(input())
C = 0
if a < b:
    C = a + b
    print(C)
elif a > b and a > 3:
    C = pow(b, 2) - b
    print(C)
else: 
    C = pow(b, 2) - 1
    print(C)

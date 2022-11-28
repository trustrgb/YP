a = int(input())
b = int(input())

if a < 2 and b > 3:
    print(a + pow(b,2))
elif a > b and a > 3:
    print(pow(b,2) + 2)
else:
    print(b)

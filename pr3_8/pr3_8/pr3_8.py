v = int(input())
k = int(input())
B = 0
if v < 2 and k == 1:
    B = v - k + 1
    print(B)
elif k > v:
    B = pow(k,2) + pow(v, 2)
    print(B)
else:
    B = pow(k, 2) + v
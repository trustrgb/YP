v = int(input())
k = int(input())
Z = 0
if v < k:
    Z = v - k - 1
    print(Z)
elif k > v:
    Z = (pow(k,2)) - (pow(v,2))
    print(Z)
else:
    Z = pow(k,2) - 2
    print(Z)
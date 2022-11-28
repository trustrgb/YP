f = int(input())
k = int(input())
R = 1;
if f < 5 and k > 2:
    R = f + k - 1
    print(R)
elif k < 2:
    R = pow(k,2)
    print(k)
elif k == 2:
    print(R) 

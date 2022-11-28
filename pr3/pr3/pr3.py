a = int(input())
b = int(input())
c = int(input())
beg_int = int(input())
en_int = int(input())
if beg_int > en_int:
    beg_int, en_int = en_int, beg_int
if a >= beg_int and a <= en_int:
    print(a)
if b >= beg_int and b <= en_int:
    print (b)
if c >= beg_int and c <= en_int:
    print (c)

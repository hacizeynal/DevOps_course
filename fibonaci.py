"""
0 = a=1 =1 =2 =3 =5
1 = b =1 =2 =3 =5 =8
1 = c =2 =3 =5 =8 =13
2 =
3
5
8
13
21
34

"""


def fibo(n):
    a = 0
    b = 1
    # print(a)
    # print(b)

    for i in range(2, n):
        c = a + b
        a = b
        b = c
    return c

print(fibo(9))

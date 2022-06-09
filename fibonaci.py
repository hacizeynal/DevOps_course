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


# def fibo(n):
#     global c
#     a = 0
#     b = 1
#     # print(a)
#     # print(b)
#
#     for i in range(2, n):
#         c = a + b
#         a = b
#         b = c
#     return c
#
#
# print(fibo(9))


def fib(number_of_terms):
    counter = 0
    first = 0
    second = 1
    temp = 0

    while counter <= number_of_terms:
        print(first)
        temp = first + second
        first = second
        second = temp
        counter = counter + 1
# Driver Code
fib(9)


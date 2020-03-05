import sys


def fib (n):
    if  n == 0 : return 1
    a = 0
    b = 1
    if n >= 2:
        i = 2
        while (i != n):
            c = a + b
            a = b
            b = c
            i = i + 1
        return a+b


input  =int(sys.argv[1])
print(fib(input))

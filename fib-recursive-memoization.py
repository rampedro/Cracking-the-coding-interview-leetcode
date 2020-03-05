import sys

# using meozation (caching we reduce the runing time from 2^n to n 

#cache = {}


#when I use lsit instead of dictionary I will ahve problem in indexing
def fib(n, cache = {}):
    if n == 1 or n == 0: return 1
    if n in cache:
        return cache[n]
    value = fib(n-1) + fib(n-2)
    
    #put the calculated value in cache
    cache[n] = value

    return value




input = int(sys.argv[1])
print(fib(input))

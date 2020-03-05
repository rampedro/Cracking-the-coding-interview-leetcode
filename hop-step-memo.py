import sys

#8.1
# hopping 1,2,3 steps , how many ways for n steps
# using memo ( memoization ) reduced the 3^n time complexity to 
# O(n)

cache = {}


def func(n):
    if n == 0: return 1
    if n < 0 : return 0
    # considering the last step, can happen from n-1 n-2 or n-3
    if n in cache:
        return cache[n]

    value = func(n-1) + func(n-2) + func(n-3)
    cache[n] = value
    return value




input = int(sys.argv[1])
print(func(input))

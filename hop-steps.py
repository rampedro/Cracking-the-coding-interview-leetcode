import sys

#8.1
# hopping 1,2,3 steps , how many ways for n steps

def func(n):
    if n == 0: return 1
    if n < 0 : return 0
    # considering the last step, can happen from n-1 n-2 or n-3
    return func(n-1) + func(n-2) + func(n-3)




input = int(sys.argv[1])
print(func(input))

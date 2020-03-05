import sys

def fastFib(n, memo = []):
    if n == 0 or n == 1 : return 1
    print 'fib1 called with', n
    if not n in memo:
        memo[n] = fastFib(n-1, memo) + fastFib(n-2, memo)
    #this should be outside of the if clause:
    return memo[n] #<<<<<< THIS

input = int(sys.argv[1])
print(fastFib(input))

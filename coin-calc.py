import sys
def coin(n,p):
    if n<=0 : return 0
    
    p += coin(n-0.01,p)
    return p


input = float(sys.argv[1])

print(coin(input,0))

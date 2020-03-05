# this works, but generating the duplicate and then not counting them in our solution takes long time. we are doing the alg in O(n!) time which is pretty large in size.

import sys

def p(n):
    s = []
    if n == 1 : return ["()"]

    for i in p(n-1):
        s.append("(" + i + ")")
        s.append( "()" + i)
        g = i+"()"
        if g not in s:
            s.append(g)
    return set(s)
    
input = int(sys.argv[1])

#print(p(input))
print(len(p(input)))

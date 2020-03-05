# this works, but generating the duplicate and then not counting them in our solution takes long time. we are doing the alg in O(n!) time which is pretty large in size.

import sys

def p(n):
    s = []
    if n == 1 : return ["()"]

    for i in p(n-1):
        #s.append("()")
        s.append( "("+i+")" )
        s.append(i+"()")
        #if n>2:
        s.append("()"+i)
        
        #for g in i:
        #    if g != ")" and g!="":
        #        s.append("()")
        #if g not in s:
            #    s.append(g)
    return set(s)
    
input = int(sys.argv[1])

print(p(input))
print(len(p(input)))

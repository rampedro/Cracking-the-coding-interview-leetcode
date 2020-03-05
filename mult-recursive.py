
def mult (a,b,sum):
    if a>b:
        end = a-b+1
    else:
        end = b-a+1
    if a == end or b == end:
        sum += a+b-1
        print(sum)
        return
    sum += a+b-1
    
    mult(a-1,b-1,sum)


mult(223,3000,0)

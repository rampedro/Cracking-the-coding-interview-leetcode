


def mult(a,b):
    
    if a == 1:
        return b

    
    sum = mult(a>>1,b)

    if a% 2 == 0:
        return sum + sum
    else:
        return sum + sum + b

# as long as finst number is larger than the second
print(mult(4000,2123123))


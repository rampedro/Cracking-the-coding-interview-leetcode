def minPro(a,b):
    if a<b:
        bigger = a
        smaller = b
    else:
        smaller = a
        bigger = b
    return minProHelp(smaller,bigger)

def minProHelp(small,big):
    if small == 0: return 0
    elif small == 1 : return big

    s = small >> 1
    halfProd = minProHelp(s,big)

    if small % 2 == 0:
        return halfProd + halfProd
    else:
        return halfProd + halfProd + big


print(minPro(1992,1993))

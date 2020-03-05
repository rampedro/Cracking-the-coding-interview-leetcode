

def magic(A,i):
    if len(A) == i : 
        print("not there")
        return
    if A[i] == i : 
        print("magic is %s" %(str(i)))
        return
    return magic (A,i+1)


A = [-40,-20,-1,1,2,3,5,7,9,12,13]

magic(A,0)

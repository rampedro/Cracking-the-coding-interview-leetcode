



def toh(n,src,des,spare):
    if n<=0:
        return
    else:
        toh(n-1,src,spare,des)
        print(" move form {} --to--> {}".format(src,des))
        toh(n-1,spare,des,src)

toh(5,1,2,3)

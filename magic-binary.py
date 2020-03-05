import time

#find the magic index, no duplicatae ( taking O(logn) )

def magic(A,x,y):
    
    middle = (y+x)/2
    #midVal = A[middle]
    
    if A[middle] == middle : 
        print("magic is %s" %(str(middle)))
        return
    if A[middle]<middle:
        magic(A,middle+1,y)

    if A[middle] > middle:
        magic(A,x,middle-1)




#A = [-10,-5,2,2,2,3,4,7,9,12,13]
A = [-40,-20,2,4,6,8,10,11,12,14,15]


start = time.time()


magic(A, 0, len(A)-1)

end = time.time()



print("Took {} secs".format(end-start))

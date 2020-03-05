#finding the magic index, with duplicate, time : O(n) 

import time
def magic(A,x,y):
    
    middle = (y+x)/2
    #midVal = A[middle]
    if y < x : return -1
    if A[middle] == middle : 
        print("magic is %s" %(str(middle)))
        return
    #if A[middle]<middle:
    #magic(A,middle+1,y)

    #if A[middle] > middle:
    #magic(A,x,middle-1)

    magic(A,x,middle-1)
    magic(A,middle+1,y)



#A = [-10,-5,2,2,2,3,4,7,9,12,13]
A = [-40,-20,2,4,6,8,10,11,12,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]

start = time.time()

magic(A, 0, len(A)-1)

end = time.time()


print("Took {} secs".format(end-start))

import numpy as np

u = np.array([[1,0,0,0], [1,1,0,0,],[0,1,1,0] , [0,0,1,1] , [0,0,0,1]])
r,c = u.shape

def func(matrix, y , x , a,b):
    # base case if we get to the end point
    if ( y-1 == a and x-1 ==b):
        print("robot is there")
    # check if not end of row or down is limmited -> go right
    if (a+1 == x and b != x-1) or a+1 < y and (matrix[a+1][b+0] == 0):
        print("right-")
        return func(matrix,y,x,a,b+1)
    # check if not end of the column or right is limmited -> go down
    if (b+1 == x and a != y-1)or (b+1<x and (matrix[a][b+1] == 0)) :
        print("down-")
        return func(matrix,y,x,a+1,b)
    if ((a != y-1 and b != x-1) and (matrix[a+1][b+1] == 0)):
        print("right-")
        return func(matrix,y,x,a,b+1)
    if ((a != y-1 and b != x-1) and (matrix[a+1][b+1] == 1)):
        print("down-")
        return func(matrix,y,x,a+1,b)
func(u,r,c,0,0)

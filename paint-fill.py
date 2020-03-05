def paint(A,i,j,color=3,p=None):
    if  i<0 or i>len(A) or j<0  or j>len(A[0]):
        print("***")
        return A
    else:
        A[i][j] = 3
        if  A[i-1][j] == p:
            paint(A,i-1,j,color=3,p=p)
        if i+1 < len(A) and A[i+1][j] == p:
            paint(A,i+1,j,color=3,p=p)
        if  A[i][j-1] == p:
            paint(A,i,j-1,color=3,p=p)
        if j+1 < len(A[0]) and A[i][j+1] == p:
            paint(A,i,j+1,color=3,p=p)
    



    return A


A = [[1,1,1,1,1,1],[1,1,2,2,1,1],[1,1,2,2,1,1],[2,2,2,2,2,2]]
s = ""

# A is the matric
# next integer is the row position of the selected point
# next integer is the column posiiton of the selected point
#color : is the color we want at the end
#p : indicates the current color/value of the selected point


A = paint(A,1,2,color=3,p=2)
for i in range(len(A)):
    for j in range(len(A[i])):
        s += str(A[i][j])
        if j != len(A[i])-1:
            s += ","
    print(s)
    s=""

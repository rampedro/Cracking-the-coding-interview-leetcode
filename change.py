import sys

def count(S, m, n): 
    # m is the number if coins that we have 
    # and n is the amount we are trying to break down.
    # we do n+1 rows as we need it for the base case. (bottom-up_


    table = [[0 for x in range(m)] for x in range(n+1)] 
  
    # Fill the entries for 0 value case (n = 0) 
    for i in range(m): 
        table[0][i] = 1
    
    
    
    for row in range(1,n+1):
        for col in range(m):
            first = table[row-S[col]][col] if row-S[col] >= 0 else 0
            sec = table[row][col-1] if col-1 >= 0 else 0

            table[row][col] = first + sec
    
    
    
    
    
    #return table[n][m-1]
    return table

    


S = [1,2,3]
input = int(sys.argv[1])
print(count(S,len(S),input))


class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data


# print in pre order style , DFS pattern 
s = "" 
def print_tree(t,s):
    if t != None:
        
        print(s+str(t.data))
        print_tree(t.left,s[:len(s)/2])
        print_tree(t.right,s*2)

def makeTree(L,a,b):
    if b < a : return
    mid = (a+b)/2
    n = Node(L[mid])
    n.left = makeTree(L,a,mid-1)
    n.right = makeTree(L,mid+1,b)
    return n


tree = makeTree([1,2,3,4,5,6,7],0,6)
print_tree(tree,s)




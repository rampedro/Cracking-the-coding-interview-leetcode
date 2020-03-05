
class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data


# another tre implimentation
#root = Node(4)
#root_l = Node(2)
#root_r = Node(4)
#root.left = root_l
#root.right = root_r

# print in pre order style , DFS pattern 
s = "" 
def print_tree(t):
    if t != None:
        
        print(s+str(t.data))
        print_tree(t.left)
        print_tree(t.right)

def makeTree(L,a,b):
    if b < a : return
    mid = (a+b)/2
    n = Node(L[mid])
    n.left = makeTree(L,a,mid-1)
    n.right = makeTree(L,mid+1,b)
    return n


tree = makeTree([1,2,3,4,5,6,7,8,9],0,8)
#print_tree(tree)


def isBST(T):
    res = False
    if T != None:
        if T.left != None:
            res = T.data >= T.left.data
            if res == False:
                return res
        if T.right != None:
            res = T.data <= T.right.data
            if res == False:
                return res
    else:
        return True
    
    return isBST(T.left) and isBST(T.right)


print(isBST(tree))

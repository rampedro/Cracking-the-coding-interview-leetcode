# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

def isSameTree(p, q):
    if p == None and q == None : return True
    if p == None and q != None or p != None and q == None: # if not p or not q
        return False
    if p.val != q.val :
        return False
        
    return isSameTree(p.left,q.left) and isSameTree(p.right,q.right)

p = TreeNode(1)
q = TreeNode(1)

pleft = TreeNode(2)
qright = TreeNode(2)


p.left = pleft
q.right = qright


print(isSameTree(p,q))

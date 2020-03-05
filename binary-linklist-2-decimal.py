class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

def getDecimalValue(head):
        A = []
        
        while(head.next != None):
            A.append(head.val)
            head = head.next
        A.append(head.val)
        

        
        m = len(A)-1
        n=0
        for idx,i in enumerate(A):
            n += i*(1 << (m-idx))                
        return n



# testing 

head = ListNode(1)
headnext = ListNode(0)
headnextnext = ListNode(1)

head.next = headnext
headnext.next = headnextnext


print(getDecimalValue(head))

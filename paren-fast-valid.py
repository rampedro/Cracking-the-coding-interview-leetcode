import sys

def paren(left,right,string):
    if(left == 0 and right == 0):
        print (string)
    if(left>right):
        return
    if (left > 0):
        paren(left-1,right,string+"(")
    if (right > 0):
        paren(left,right-1,string+")")


input = int(sys.argv[1])
paren(input,input,"")

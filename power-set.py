
# tiem complexity is 2^n and due to the for loops it would be total of O(n2^n)

myset = [1,2,3]

def powerset(mylist, memo):

    if mylist == []:
        return [memo]
    else:
        result = []
        for s in powerset(mylist[1:],memo + [mylist[0]]):
           result.append(s)
        for s in powerset(mylist[1:],memo):
            result.append(s)

    return result


print(powerset(myset,[]))



def powerset2(mylist):
    result = [[]]
    for s in mylist:
        newlist = [previously_constructed + [s] for previously_constructed in result]
        result.extend(newlist)
    return result


print(powerset2(myset))


#this will not work well with string that have duplicates.
# time cpmplexity : O(n*n!) 
# this algorith m does not work great with long instances,
# altouhgh an example like baaaaaaaaaaaa , despite its large size, but can only 
#produce 13 unique permuatation, that should not nommarly take too long.
# the reason for it taking too long is that the alg is trying to generate all permuatations and 
# then remove those that are identical.

# how can we generate non-identical ones only.

def allPermutations(strng):
    if len(strng) ==1:
        return [strng]
    perm_list = []
    #for i in set(strng):
        # smallerStr = strng.replace(i,"")
    for idx, i in enumerate(strng):
        if strng.count(i) == len(strng):
            perm_list = [strng]
            continue
           
            
        #smallerStr = strng.replace(i,"",1)
        #smallerStr = strng[:idx] + strng[idx+1:]
        #print(smallerStr)
        smallerStr = strng[:idx]+strng[idx+1:]
        z = allPermutations(smallerStr)
        for t in z:
            if not  (i+t) in perm_list:
                perm_list.append(i+t)
    
    return perm_list

print(allPermutations("baaaaa"))

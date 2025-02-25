# selection sort to find the least number in a given list 
l = [1,2,-1,5,0,-1]
for ind1 in range(1):
    li = ind1
    for ind2 in range(ind1+1,len(l)):
        if l[ind2] <l[li]:
            li = ind2
            l[ind1],l[li] = l[li],l[ind1]
print(l)
print(l[0])
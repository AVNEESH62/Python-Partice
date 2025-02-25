# in b ubble sort find the  second highest number
l = [1,4,5,-2,0,3]
for ind1 in range(2):
    for ind2 in range(len(l)-1-ind1):
        if l[ind2] > l[ind2+1]:
            l[ind2],l[ind2+1] = l[ind2+1], l[ind2]
print(l)
print(l[-2])
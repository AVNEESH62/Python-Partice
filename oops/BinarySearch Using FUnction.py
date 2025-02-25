def binary(num):
    user = 4
    low = 0
    high = len(l)-1
    while low<=high:
        mid = (low+high)//2
        if l[mid]>user:
            high = mid-1
        elif l[mid]<user:
            low = mid+1
        elif l[mid]== user:
            return mid
    return -1
l= [1,2,3,4,5,6,7,8,10]
print(binary(l))
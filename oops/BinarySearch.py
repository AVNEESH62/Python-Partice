l = [1,2,3,4,5,6,7,8,9]
user = 8
low = 0
high = len(l)-1
while low <= high:
    mid = (low + high)//2
    if l[mid] > user:
        high = mid-1
    elif l[mid] < user :
        low = mid+1
    elif l[mid] == user:
        print(mid)
        break
else:
    print(-1)
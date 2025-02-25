def interpolation(s):
    low=0
    high=len(s)-1
    user = 19
    while low<=high and s[low]<=user<=s[high]:
        mid =low+int((high-low)/(s[high]-s[low])*(user-s[low]))
        if s[mid]>user:
            high = mid-1
        elif s[mid]<user:
            low = mid+1
        elif s[mid]== user:
            return mid
    return -1
s = [-4,2,5,6,7,11,19,24]
print(interpolation(s))
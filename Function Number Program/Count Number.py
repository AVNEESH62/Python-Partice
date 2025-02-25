# write a program to count the given number
def count(num,res= 0):
    while num!=0:
        rem = num%10
        res +=1
        num = num//10
    return res
num = 32113
print(count(num))
        
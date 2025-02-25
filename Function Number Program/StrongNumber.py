#write a program to print the give number is strong number or not ?
def strong(num,dup,res= 0):
    while num != 0:
        rem=num%10
        fact = 1
        for val in range(1,rem+1):
            fact = fact*val
        res = res+fact
        num = num//10
    if dup == res:
        return 'it is a strong number'
    return 'not a strong number'
num = 145
print(strong(num,num))
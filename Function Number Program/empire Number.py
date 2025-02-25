# write a program to check the given num ber is empire number or not ?
def prime(num):
    if num >1:
        for val in range(2,num//2+1):
            if num%val == 0:
                return False
        return True
    return False
def rev(num,res=0):
    while num != 0:
        rem = num%10
        res = res*10+rem
        num = num//10
    return res
def empire(num):
    if prime(num) and rev(num):
        return 'its a empire number '
    return 'its not a empire number'
num = 37
print(empire(num))
        
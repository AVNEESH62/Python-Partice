def rev(num,res =0):
    dup = num
    while num !=0:
        rem = num%10
        res = res*10+rem
        num = num //10
    if dup == res:
        return True 
def prime(num):
    if num >1:
        for val in range(2,num//2+1):
            if num%val == 0:
                return False
        return True
    return False
def paliprime(num):
    if prime(num) and rev(num):
        return 'its a paliprime number'
    return 'it not a paliprime number'
num = 11
print(paliprime(num))
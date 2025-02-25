def  rev(num,res=0):
    while num!=0:
        power = len(str(num))
        rem=num%10
        res=res+rem*(10**power-1)
        num = num//10
    return res
num =123
print(rev(num))
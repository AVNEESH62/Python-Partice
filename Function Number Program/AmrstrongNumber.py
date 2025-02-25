def arm(num,dup,res=0):
    power = len(str(num))
    while num != 0:
        rem = num%10
        res = res+rem**power
        num = num//10
    if dup == res:
        return 'its a aramstrong number'
    return 'its not a armstrong number'
num = 153
print(arm(num,num))
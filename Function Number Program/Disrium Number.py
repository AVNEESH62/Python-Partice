# write a program to print given number is disaram number or not
def disaram(num,dup,res=0):
    power = len(str(num))
    while num != 0:
        rem = num%10
        res = res+rem**power
        power = power-1
        num =  num//10
    if dup == res:
        return 'its a disaram number'
    return 'not a disaram number'
num = 135
print(disaram(num,num))    

        
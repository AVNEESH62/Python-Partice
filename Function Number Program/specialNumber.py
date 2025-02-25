# write a program to print given number is  a special number or not ?
def special(num,dup,res=0):
        for val in range(1,num//2+1):
            if num%val == 0:
                res = res+val
        if dup == res:
            return 'its a special number'
        else:
            return 'not a special number'
num = 6
print(special(num,num))
        
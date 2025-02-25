#Write a progran to add the given sequence 
def digit(num,res=0):
    while num != 0:
        rem = num%10
        res = res+rem
        num = num//10
    return res
print(list(map( digit, [12,42,52,62])))
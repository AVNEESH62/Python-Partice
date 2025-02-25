def binary(num,res=0):
    pos =1
    while num!=0:
        rem = num%10
        res = res+rem*pos
        pos = pos*2
        num = num//10
    return res
num = 1101
print(binary(num))
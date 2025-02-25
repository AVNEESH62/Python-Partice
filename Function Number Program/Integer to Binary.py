# weite a code to convert the given number from binary to intger?
def integer(num,res=0):
    pos = 1
    while num !=0:
        rem = num%2
        res= res+rem*pos
        pos = pos*10
        num = num//2
    return res
num = 13
print(integer(num))
        
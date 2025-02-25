def binary(num,res= 0):
    pos = 1
    while num != 0:
        rem = num%2
        res = res+rem*pos
        pos = pos*10
        num = num//2
    return res
for num in range(20,30):
    print(f'{num}--{binary(num)}')
    
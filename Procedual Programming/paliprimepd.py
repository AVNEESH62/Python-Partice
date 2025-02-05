num =131
dup = num
res = 0
if num>1:
    while num != 0:
        rem = num%10
        res = res*10+rem
        num = num//10
    for val in range(2,num//2+1):
        if dup%val == 0:
            print('not a paliprime')
            break
    if dup == res:
        print('paliprime')
    else:
        print('not a paliprime')
else:
    print('not a paliprime')
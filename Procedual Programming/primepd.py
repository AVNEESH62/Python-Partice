num = 13
if num >1:
    for val in range(2,num//2+1):
        if num%val == 0:
            print('not prime')
            break
    else:
        print('prime no')
else:
    print('not prime')
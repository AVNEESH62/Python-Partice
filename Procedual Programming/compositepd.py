num = 1
res = 0
if num>3:
    for val in range(2,num//2+1):
        if num%val == 0:
            print('its composite number')
            break
    else:
        print('not a composite number')
else:
    print('its not a composite number')
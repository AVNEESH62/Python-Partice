num = 81
val = 0
while val*val<=num:
    if val*val==num:
        print('pass')
        break
    val+=1
else:
    print('not pass')
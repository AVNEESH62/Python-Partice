num =2025
if len(str(num))%2 == 0:
    mid = len(str(num))//2
    lh = int(str(num)[:mid])
    rh = int(str(num)[mid:])
    if (lh+rh)**2 == num:
        print('tech number')
    else:
        print('not a tech number')
else:
    print('not a tech number')
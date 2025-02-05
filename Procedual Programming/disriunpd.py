num = 145
dup = num
power = len(str(num))
res = 0
while num != 0:
    rem = num%10
    res = res+rem**power
    num = num//10
    power -=1
if dup == num:
    print('its a disrium number')
else:
    print('not a disrium number')
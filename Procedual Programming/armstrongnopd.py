num = 153
dup = num
res = 0
power = len(str(num))
while num != 0:
    rem = num%10
    res = res+rem**power
    num = num//10
if dup == res:
    print('its armstrong number')
else:
    print('its not a armstrong number')
num = 123
sum = 0
mul = 1
while num != 0:
    rem = num%10
    sum = sum+rem
    mul = mul*rem
    num = num//10
if sum == mul:
    print('spy number')
else:
    print('not a spy number')
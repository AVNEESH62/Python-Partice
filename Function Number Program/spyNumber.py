def spy(num):
    sum = 0
    mul = 1
    while num != 0:
        rem = num %10
        sum = sum+rem
        mul = mul*rem
        num = num//10
    if sum == mul:
        return 'its a spy number'
    return 'it not a spy number'
num = 123
print(spy(num))
        
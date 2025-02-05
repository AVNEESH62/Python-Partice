num = 3
res = 0
fact = 1
while num != 0:
    rem = num%10
    for val in range(1,rem+1):
        fact = fact*val
    res = res+fact
    num = num//10
print(res)
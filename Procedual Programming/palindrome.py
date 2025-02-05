num = 12
dup = num
res = 0
while num != 0:
    rem = num%10
    res = res*10+rem
    num  = num//10
if dup == res:
    print('palindrome')
else:
    print('not a palindrome')
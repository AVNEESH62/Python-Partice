num1 = 12
num2 = 14
gcd = min(num1,num2)
while True:
    if num1%gcd == 0 and num2%gcd == 0:
        print(gcd)
        break
    gcd -=1
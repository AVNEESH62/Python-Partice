def gcd(num1,num2):
    gcd = max(num1,num2)
    while True:
        if num1%gcd == 0 and num2%gcd == 0:
            return gcd
        gcd -=1
num1= 12
num2 = 16
print(gcd(num1,num2))
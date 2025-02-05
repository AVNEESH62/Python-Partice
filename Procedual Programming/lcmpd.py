num1 = 12
num2 = 16
lcm = max(num1,num2)
while True:
    if lcm%num1 == 0 and lcm%num2 == 0:
        print(lcm)
        break
    lcm +=1
    
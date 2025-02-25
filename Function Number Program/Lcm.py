#write a program to find the lcm of given two number 
def lcm(num1,num2):
    lcm = max(num1,num2)
    while True:
        if lcm%num1 == 0 and lcm%num2 == 0:
                return lcm
         
        lcm +=1
num1 = 2
num2 = 4
print(lcm(num1,num2))

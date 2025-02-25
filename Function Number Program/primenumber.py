# write a program to print given number is prime or not 
def prime(num):
    if num >1:
        for val in range(2,num//2+1):
            if num%val == 0:
                return 'not prime'
        return 'prime'
    return 'not prime'
num = 11
print(prime(num))
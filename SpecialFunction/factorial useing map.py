def factorial(num,fact=1):
    for val in range(1,num+1):
        fact = fact*val
    return fact
print(list(map(factorial,range(1,6))))
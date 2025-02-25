def prime(num):
    if num>1:
        for val in range(2,num//2+1):
            if num%2==0:
                return (f'{num} is not a prime number')
        return (f'{num} is  a prime number')
    return (f'{num} is  a prime number')
    print()

print(list(map(prime,range(1,21))))
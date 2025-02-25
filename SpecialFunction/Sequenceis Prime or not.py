def prime(num):
    if num>1:
        for val in range(2,num//2+1):
            if num%val == 0:
                return (f'{num} = not a prime number')
        return (f'{num} = is a prime number')
    return (f'{num} = not a prime number')
#
for l in map(prime,range(1,21)):
    print(l)
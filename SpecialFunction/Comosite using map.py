# Write a program to check the number from 1 to 20 which are compostite number or not using map functhion 
def comp(num):
    if num>3:
        for val in range(2,num//2+1):
            if  num%val == 0:
                return (f'{num} = is a compostite number')
        return (f'{num} = is a not compostite number')
    return (f'{num} = is not a compostite number')
for l in map(comp,range(20,41)):
    print(l)
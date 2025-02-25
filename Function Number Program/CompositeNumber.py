# wirte a program to check the given number is composite or not ?
def comp(num):
    if num>3:
        for val in range(2,num//2+1):
            if num%val == 0:
                return 'composite number'
        return 'Not composite number'
    return 'not composite number'
num = 13
print(comp(num))
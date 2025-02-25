# Write a program to check the given number is tech or not 
def tech(num):
    if len(str(num))%2 == 0: 
        mid = len(str(num))//2
        lh = int(str(num)[:mid])
        rh = int(str(num)[mid:])
        if (lh+rh)**2 ==num:
            return 'it is a tech number'
        return 'it is not a tech number'
    return 'it is not a tech number'
num = 2025
print(tech(num))
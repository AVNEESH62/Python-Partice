#write a programe to check the number is palindrome or not ?
def palindrome(num,dup,res=0):
    while num != 0:
        rem = num%10
        res = res*10+rem
        num = num//10
    if dup == res:
        return 'it is a palindrome number'
    else:
        return 'its not a palindrome number'
num = 121
print(palindrome(num,num))
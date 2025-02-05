def sample(num):
    if num == 0:
        return
    print(num)
    sample(num-1)
num = 5
sample(num)
    
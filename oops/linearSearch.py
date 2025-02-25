l = [1,5,9,-4,6,3,-1]
user = 3
for ind in range(len(l)):
    if user == l[ind]:
        print(ind)
        break
else:
    print(-1)
        
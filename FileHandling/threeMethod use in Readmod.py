# here we are going to see how we use three method to acces the file in read access mode 
avi = open('sunday.text','r')
print(avi.read(5))
print('---------------------')
print(avi.tell())
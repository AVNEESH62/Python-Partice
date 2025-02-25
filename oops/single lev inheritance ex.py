# example of single level inheritance 
class parent():
    var1 = 100
    var2 = 200
    def __init__(self):
        print('parent is excuted')
class child(parent):
    var2 = 300
    var3 = 500
    
obj = child()
obj = parent()
print(obj.var2)
print(obj.var2)
print(obj.var1)
print('-----------------------')
# accessing using class refrences
print(parent.var2)
print(child.var3)
print('-----------------')
# mdifying using class refrence 
child.var2= 800
print(child.var2)
print('------------------------')
# mdifying using class object refrence 
obj.var3 = 1000
print(obj.var3)
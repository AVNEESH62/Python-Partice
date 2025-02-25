# in this example we are showing the how class attributes are created and how it can acess by class refrence as well as object refrence
class jsp():
    name = 'jpython'
    place = 'marathali'
    
avneesh = jsp()
suman   = jsp()
print(jsp.name,jsp.place)
#acessing using boject refrence 
print(avneesh.name,avneesh.place)
    
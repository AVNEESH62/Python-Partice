class resto():
    brand = 'taj'
    place = 'mumbai'
    star  = '5star'
    
    def __init__(self,enteryno,name,mobno,gmail):
        self.enteryno  = enteryno
        self.name      = name
        self.mobno     = mobno
        self.gmail     = gmail
    def details(self):
        print(f'enter no = {self.enteryno}')
        print(f'Name = {self.name}')
        print(f'Mobno = {self.mobno}')
        print(f'gmail = {self.gmail}')
    def modify(self):
        self.name = 'shankar'
person1 = resto(1,'avneesh',6200386144,'avneeshbgp@gmail.com')
person2 = resto (2,'sara',34989832487,'sara12@gmail.com')
#acessing using object refrence
person1.details()
# acessing using class refrence 
resto.details(person2)
# using object attributes we can modify only object attributyes
person1.modify()
person1.details()

class bike():
    company ='RoyalEnfeild'
    model   = 'classice 350'
    def __init__(self):
        print('constructor is executed')
        print(self)
owner1 = bike()
print(owner1)
    
    
    
    
    
print('------------------------------------------')
class bank():
    branch = 'SBI'
    place = 'Pkaur'
    ifcs  = 'SBI0001'
    def __init__(self,Name,mobno,Email,account):
        self.Name  = Name
        self.mobno = mobno
        self.Email = Email
        self.account = account
cust1 = bank('avnessh',6200386144,'avneeshbgp@gamil.com',3213233232123)
cust2 = bank('suman','7834678666','sumanraj@gmail.com',23187272718)
print('----------------------------------------------------------------------------------') 
#acessing using object attributes
print( cust1.branch, cust1.Name, cust1.mobno, cust1.Email, cust1.account)
#acesing using class refrence 
print(bank.branch,bank.place)
print('------------------------------------------------------')
#modifying using class refrence 
cust1.Name = 'shankar'
print(cust1.Name)




        
    
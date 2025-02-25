#Creating class attributes using and modifying using both refrence class as well as object 
class bank():
    stud = 'jpython'
    place = 'pakur'
# creating object 
suman = bank()
avi   = bank()
kin   = bank()
# acessing using class refrence 
print(bank.stud,bank.place)
print('---------------------')
# acessing using object refrence 
print(kin.stud)
print(avi.stud,avi.place)
print('------------------------')
# modifying  using class refrence 
bank.stud = 'j java'
print(bank.stud)
print('------------------')
#modifying using object refrence
suman.stud = 'math'
print(suman.stud,suman.place)
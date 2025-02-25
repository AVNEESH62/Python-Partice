class bank():
    branch = 'SBI'
    place  = 'Pakur'
    IFSC  = 'SBI00001'
    
    def __init__(self,Name,Gender,AccoNo,MobNo,Gmail,pin,Bal):
        self.Name     = Name
        self.Gender   = Gender
        self.AccoNo   = AccoNo
        self.MobNo    = MobNo
        self.Gmail    = Gmail
        self.pin      = pin
        self.Bal      = Bal
    def details(self):
        print(f'customer Name   = {self.Name}')
        print(f'customer gender = {self.Gender}')
        print(f'customer AccoNo = {self.AccoNo}')
        print(f'Customer MobNo  = {self.MobNo}')
        print(f'customer Gmail  = {self.Gmail}')
        print(f'Customer pin    = {self.pin}')
        print(f'Customer Bal    = {self.Bal}')
    @staticmethod
    def checkpin():
        key = int(input('enter the 4- digit pin = '))
        return key
    def withdraw(self):
        if self.pin == self.checkpin():
            amount = int(input('enter the amount to withdraw: '))
            if 0<amount<=20000:
                if amount<= self.Bal:
                    self.Bal -= amount
                    print('amount debited successfully.....')
                    print(f'remanining Bal is {self.Bal}')
                else:
                    print('Insufficent funds......')
            else:
                print('be in your limite')
        else:
            print('incorrect pin')
    def deposit(self):
        if self.pin == self.checkpin():
            amount = int(input('enter the amount to deposite: '))
            if 100<= amount<= 500000:
                self.Bal += amount
                print('amounbt credited successfully.......')
            else:
                print('i cannot take that much amount')
    
        else:
            print(' incorrect pin...')
    def checkBal(self):
        if self.pin == self.checkpin():
            print(f'Avilable blance is {self.Bal}')
        else:
            print('incorrect pin......')
    @classmethod
    def changeIFSC(cls):
        cls.IFSC = 'SBI000009'
cust1 = bank('avneesh','male',32987837432,6200386144,'avneeshbgp@gmail.com',1234,100000)
cust2 = bank('sara','female',327474642544,1234223311,'saratiwary@gmail.com',1111,100000)
cust2.deposit()
cust2.checkBal()


        
            
        
        
        
        
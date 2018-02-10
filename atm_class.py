class ATM(object):
    """docstring for ATM"""
    def __init__(self, bankName, balance):
        super(ATM, self).__init__()
        self.bankName = bankName
        self.balance = balance

    def pulling(self, request):
        print self.bankName
        while request > 0:
            if request >= 100:
                request -= 100
                self.balance -= 100
                print ("give 100")
            elif request >= 50:
                request -= 50
                self.balance -= 50
                print ("give 50")
            elif request >= 10:
                request -= 10
                self.balance -= 10
                print ("give 10")
            elif request >= 5:
                request -= 5
                self.balance -= 5
                print ("give 5")
            else:
                request = 0
        return self.balance

                    
        return self.balance
    def withdraw(self, request):
        if   request > self.balance:
            print("your balance is "+str(self.balance)+
                " and we Can't give you all this money because your request is " 
                + str(request)+ " more than your balance")
            return "Your Current Balance is "+ str(self.balance)
        elif request < 0:
            print("More than zero plz!")
        else:
            return "Your Current Balance is "+ str(ATM.pulling(self, request))
        








            



atm1 = ATM("Islamic Bank", 1000)
atm2 = ATM("bemo", 3000)
print atm1.withdraw(500)
print atm1.withdraw(400)
print atm1.withdraw(200)

print atm2.withdraw(500)
print atm2.withdraw(400)
print atm2.withdraw(2000)

class ATM:
    """docstring for ATM"""
    def __init__(self, bankName, balance):
        self.bankName = bankName
        self.balance = balance
        self.withdrawals_list = []

    def pulling(self, request):
        print "=============================================="
        print "your bank is " + self.bankName
        print "your Current Balance is " + str(self.balance)
        print "=============================================="
        self.withdrawals_list.append(request)
        accepted_notes = [100, 50, 10, 5, 2, 1]
        self.balance -= request
        for note in accepted_notes:
            while request >= note:
                request -= note
                print "give " + str(note)
          

        return self.balance


    def show_withdrawals(self):
        i = 1
        print "========================withdrawals================================="
        for withdrawal in self.withdrawals_list:
            print "withdrawal " + str(i)+ ": " + str(withdrawal)
            i += 1
        print "======================================================================="

                    
    def withdraw(self, request):
        if   request > self.balance:
            print "======================================================================="
            print "your bank is " + self.bankName
            print("your balance is "+str(self.balance)+
                " and we Can't give you all this money because your request is " 
                + str(request)+ " more than your balance")
            print "======================================================================="
            return "Your Current Balance is "+ str(self.balance)
            print "======================================================================="
        elif request < 0:
            print "======================================================================="
            print("More than zero plz!")
            print "======================================================================="
        else:
            return "Your Current Balance is "+ str(self.pulling(request))
            print "=============================================="
        








            



atm1 = ATM("Islamic Bank", 1000)
atm2 = ATM("bemo", 3000)
print atm1.withdraw(500)
print atm1.withdraw(400)
print atm1.withdraw(101)

atm1.show_withdrawals()

print atm2.withdraw(500)
print atm2.withdraw(400)
print atm2.withdraw(2000)

atm2.show_withdrawals()

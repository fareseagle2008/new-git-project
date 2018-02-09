

def withdraw(balance, request):
    if   request > balance:
        print("your balance is "+str(balance)+" and we Can't give you all this money because your request is " + str(request)+ " more than your balance")
        return balance
    elif request < 0:
        print("More than zero plz!")
    else:
        while request > 0:

            if request >= 5:
                request -= 5
                balance = balance - 5
            else:
                request = 0
                
        return balance



balance = 500
balance = withdraw(balance, 250)
balance = withdraw(balance, 249)

print balance


def withdraw(balance, request):
    if   request > balance:
        print("your balance is "+str(balance)+" and we Can't give you all this money because your request is " + str(request)+ " more than your balance")
        return balance
    elif request < 0:
        print("More than zero plz!")
    else:
        while request > 0:

            if request >= 100:
                request -= 100
                balance = balance - 100

            elif request >= 50:
                request -= 50
                balance = balance - 50

            elif request >= 10:
                request -= 10
                balance = balance - 10

            elif request >= 5:
                request -= 5
                balance = balance - 5

            elif request < 5:
                request = 0
                
        return balance



balance = 500
balance = withdraw(balance, 400)
balance = withdraw(balance, 400)

print balance
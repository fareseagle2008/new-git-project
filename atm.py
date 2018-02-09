def pulling(b, r):
    while r > 0:
        if r >= 100:
            r -= 100
            b -= 100
            print ("give 100")
        elif r >= 50:
            r -= 50
            b -= 50
            print ("give 50")
        elif r >= 10:
            r -= 10
            b -= 10
            print ("give 10")
        elif r >= 5:
            r -= 5
            b -= 5
            print ("give 5")
        else:
            r = 0

                
    return b


def withdraw(balance, request):
    if   request > balance:
        print("your balance is "+str(balance)+" and we Can't give you all this money because your request is " + str(request)+ " more than your balance")
        return balance
    elif request < 0:
        print("More than zero plz!")
    else:
        return pulling(balance, request)

            



balance = 500
balance = withdraw(balance, 250)
balance = withdraw(balance, 255)

print balance

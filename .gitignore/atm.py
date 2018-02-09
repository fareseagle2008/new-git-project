
def withdraw(balance, request):
    if   request > balance:
        print("Can't give you all this money !!")
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
balance = withdraw(balance, 250)
balance = withdraw(balance, 200)
balance = withdraw(balance, 49)
print balance
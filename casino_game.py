import random
x = True
count = 0
print("> Welcome to the casino")
print("> Enter total balance")
bal = int(input(">"))

while x == True :
    print("> Enter bet amount")
    bet = int(input(">"))
    wl = random.randint(1,2)
    count +=1
    if wl == 1:
        bal = bal - bet
        if bal > 0:
            print("> You lose!")
            print("> Your new total balance is")
            print(bal)
        elif bal <= 0:
            print("> You lost everything you goon!")
            if count == 1:
                print("> You played for")
                print(count)
                print('rounds')
            elif count > 1:
                print("> You played for")
                print(count)
                print("> rounds")
            break
    elif wl == 2:
        bal = bal + bet
        print("> You win!")
        print("> Your new total balance is")
        print(bal)
import random
x = True
count = 0
print("> Welcome to the casino")
print("> Enter total balance")
bal = int(input(">"))
bet = (bal * .1)
while x == True :
    wl1 = random.randint(1 , 5)
    wl2 = random.randint(1 , 5)
    count += 1

    #Makes sure you cant go in debt and stops you before hitting negative numbers#
    if bal <= 0:
        print("> You lost everything you goon!")
        if count == 1:
            print("> You played for")
            print(count)
            print('> rounds')
            break
        elif count > 1:
            print("> You played for")
            print(count)
            print("> rounds")
            break
    elif bet > bal:
        print("> Youre broke!")
        if count == 1:
            print("> You played for")
            print(count)
            print('rounds')
            print("> Your final bet was ")
            print(bet)
            print("> dollars!")
        elif count > 1:
            print("> You played for")
            print(count)
            print("> rounds")
            print("> Your final bet was ")
            print(bet)
            print("> dollars!")
        break
    
    elif wl1 == wl2:
        bal = bal - bet
        bet = bet * 2
        print("L")
        print(bal)     
   
    elif wl1 != wl2:
        bal = bal + bet
        print("W")
        print(bal)
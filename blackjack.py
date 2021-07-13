import random
import time
dealer = 0
player = 0
plyrstrtvar = False
aistrtvar = False
ruleLoop = True

print("""> Welcome to blackjack!
> If this is your first time playing, 
> type 1 for the rules.
> If not, type 2 to begin!
""")
while ruleLoop == True:
    x = input("> ")
    if x == 1: 
        print("""
    > The goal of blackjack is to beat the dealer's hand without going over 21.
    > Face cards are worth 10. Aces are worth 1 or 11, whichever makes a better hand.
    > Each player starts with two cards, one of the dealer's cards is hidden until the end.
    > To 'Hit' is to ask for another card. To 'Stand' is to hold your total and end your turn.
    > If you go over 21 you bust, and the dealer wins regardless of the dealer's hand.
    > If you are dealt 21 from the start (Ace & 10), you got a blackjack.
    > Dealer will hit until his/her cards total 17 or higher.
    """)
    else:
        plyrstrtvar = True
        aistrtvar = True
        ruleLoop = False
playerhand =  random.randint(1, 13)
while plyrstrtvar == True:
    print("You have a")
    print(playerhand)
    print("press 1 for hit, or 2 for stand")
    hors = input("> ")
    if hors == 1:
        plyrnewcard = random.randint(1, 13)
        playerhand = plyrnewcard + playerhand
        if playerhand > 21:
            print("You busted!!")
            break
    elif hors == 2:
        plyrstrtvar = False
        print("Dealers turn....")

dealerhand = random.randint(1, 13)
while aistrtvar == True:
    print("dealer has a ")
    print(dealerhand)
    time.sleep(1)
    if dealerhand <= 16:
        dealernewcard = random.randint(1, 13)
        dealerhand = dealernewcard + dealerhand
        if dealerhand > 21:
            if playerhand <= 21:
                print("Dealer busted! You win!")
                break
            elif playerhand > 21:
                print("Both parties busted! Game Over..")
                break
    elif dealerhand >= 17:
        if playerhand <= 21:
            if dealerhand > playerhand:
             print("Dealer Wins! Game Over..")
             break
            elif dealerhand < playerhand:
                print("You Win! ")
                break
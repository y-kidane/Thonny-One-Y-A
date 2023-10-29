import random
from random import randint

#Deck = {1:[("Ace", "Hearts","Ace"),("Ace", "Spades","Ace"),("Ace", "Clubs","Ace"),("Ace", "Diamond","Ace")]}

Deck = {1:[("Ace", "Hearts"),("Ace", "Spades"),("Ace", "Clubs"),("Ace", "Diamond")],2:[(2,"Hearts"),(2,"Spades"),(2,"Clubs"),(2,"Diamond")],3:[(3,"Hearts"),(3,"Spades"),(3,"Clubs"),(3,"Diamond")],4:[(4,"Hearts"),(4,"Spades"),(4,"Clubs"),(4,"Diamond")],5:[(5,"Hearts"),(5,"Spades"),(5,"Clubs"),(5,"Diamond")],6:[(6,"Hearts"),(6,"Spades"),(6,"Clubs"),(6,"Diamond")],7:[(7,"Hearts"),(7,"Spades"),(7,"Clubs"),(7,"Diamond")],8:[(8,"Hearts"),(8,"Spades"),(8,"Clubs"),(8,"Diamond")],9:[(9,"Hearts"),(9,"Spades"),(9,"Clubs"),(9,"Diamond")],10:[(10,"Hearts"),(10,"Spades"),(10,"Clubs"),(10,"Diamond")],11:[("J","Hearts"),("J","Spades"),("J","Clubs"),("J","Diamond")],12:[("Q","Hearts"),("Q","Spades"),("Q","Clubs"),("Q","Diamond")],13:[("K","Hearts"),("K","Spades"),("K","Clubs"),("K","Diamond")]}
# player / dealer hand
playerHand = []
dealerHand = []

playerIn = True #används för att skapa game loopen
dealerIn = True

#deal cards

def dealCard(hand):
    #chosen_key = (randint(1, 13)).choice(Deck)
    random_key = randint(1, 13) #väljer random key i dic
    chosen_card = random.choice(Deck[random_key]) #indexerar en random kort med suit random i guppen av 4 kort
    (N, SU) = chosen_card #tuple matchar 
    view_card = ((N, SU))
    
    hand.append(view_card) #appendar tuple med kort och suit till tom lista för spelare eller dealer
    
    (Deck[random_key]).remove(chosen_card)
    return hand
    


#calculate total of each hand
def calcTotal(hand):
    total = 0 
    for (N, SU) in hand:
        if N in range (1, 11): #tuple matchning där den första elementet används för att räkna poäng
            total += N
        elif N in ["K", "Q", "J"]: #om kortet är ett av dessa tre = +10 poäng
            total += 10
        elif N == "Ace": #Ace ändras beroende på hur mycket poäng spelaren har
            if (total + 11) > 21:
                total += 1
            else:
                total += 11
    return total #returnerar poängen som korten är värda

        
def dealerH(): #avslöjar dealerns kort ett 
    if len(dealerHand) > 1:
        return dealerHand[0]
    elif len(dealerHand) > 2:
        return (dealerHand[0], dealerHand[1])
    

#chack for winner

#game loop

for _ in range(2): #plockar 2 kort var åt dealer och spelare i början av spelet
    dealCard(playerHand)
    dealCard(dealerHand)



while playerIn and dealerIn: #game loopen
    print(f"Dealer had {dealerH()} and X ") #avslöljar dealerns första kort 
    print(f"You had {playerHand} with a total of {calcTotal(playerHand)}") #visar spelarens 2 kort
    
    answer_loop = True #en loop för inputen, break vid valid input annars loopar frågan
    
    while answer_loop:
        if playerIn:
            hitorstay = input("\n1: Stay\n2: Hit\nChoice: ")#ta ett till kort eller stanna
        
        if hitorstay == "1":
            playerIn = False
            break
        
        elif hitorstay == "2":
            dealCard(playerHand)
            break
        
        else:
            print("Invalid choice")
        
    
    if calcTotal(dealerHand) > 16: #här är dealerns taktik, alltså ta ett till kort om den har poäng under 16, om det är över 16 stanna
        dealerIn = False
    else:
        dealCard(dealerHand)
        
    if calcTotal(dealerHand) >= 21: #loopen avslutas när dealer eller spelare fått 21 eller över
        break
    
    if calcTotal(playerHand) >= 21:
        break
    
# villkor för spelet


if calcTotal(playerHand) == 21: #om spelaren får 21
    
    print(f"\nYou have {playerHand} for a total of {calcTotal(playerHand)} and the dealer had {dealerHand} for a total of {calcTotal(dealerHand)}")
    print("BlackJack! You win!")

elif calcTotal(dealerHand) == 21: #om dealer får 21
    
    print(f"\nYou have {playerHand} for a total of {calcTotal(playerHand)} and the dealer had {dealerHand} for a total of {calcTotal(dealerHand)}")
    print("BlackJack! Dealer wins!")

elif calcTotal(playerHand) > 21: #om spelaren får över 21 = bust
    
    print(f"\nYou have {playerHand} for a total of {calcTotal(playerHand)} and the dealer had {dealerHand} for a total of {calcTotal(dealerHand)}")
    print("Bust! Dealer wins!")

elif calcTotal(dealerHand) > 21: #om dealer får över 21 = bust
    
    print(f"\nYou have {playerHand} for a total of {calcTotal(playerHand)} and the dealer had {dealerHand} for a total of {calcTotal(dealerHand)}")
    print("Dealer Bust! You win!")

elif (21 - calcTotal(dealerHand)) < (21 - calcTotal(playerHand)): #jämförelse om dealer är närmre 21 än spelaren, print dealer win
    
    print(f"\nYou have {playerHand} for a total of {calcTotal(playerHand)} and the dealer had {dealerHand} for a total of {calcTotal(dealerHand)}")
    print("Dealer wins!")

elif (21 - calcTotal(dealerHand)) > (21 - calcTotal(playerHand)): # jämförelse om spelaren är närmre 21 än dealern, print you win
    
    print(f"\nYou have {playerHand} for a total of {calcTotal(playerHand)} and the dealer had {dealerHand} for a total of {calcTotal(dealerHand)}")
    print("You win!")









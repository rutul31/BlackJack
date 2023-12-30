#Blackjack game
import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

class Card:

    def __init__(self,suit,rank):
           self.suit = suit
           self.value = values[rank]
           self.rank = rank

    def __str__(self) -> str:
          return self.rank+" of "+self.suit

class Deck:

    def __init__(self):
        self.all_cards = []
        for i in suits:
            for j in ranks:
                new_card = Card(i,j)
                self.all_cards.append(new_card) 
    def shuffle(self):
        random.shuffle(self.all_cards)
    def deal_one(self):
        return self.all_cards.pop()

class Player:

    def __init__(self,name,bank):
        self.name = name
        self.all_cards = []
        self.bank = bank
        self.total = 0
    def place_bet(self):
        while True: 
            self.amount = int(input("Place your bet: "))
            if self.amount <= self.bank:
                self.bank -= self.amount
                return self.amount 
            elif self.amount > self.bank:
                print("You do not have enough money!")
            else:
                print("Sorry did not get that!Try again!")
        
    def add_cards(self,new_cards):
        if type(new_cards)== type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
    def display(self):
        print("Your cards:")
        for i in range(len(self.all_cards)):
            print(self.all_cards[i])
    def total_value(self):
        for i in range(len(self.all_cards)):
            self.total += self.all_cards[i].value
        return self.total
    def ace(self):
        for i in range(len(self.all_cards)):
            if "Ace" == self.all_cards[i].rank:
                return True
            else:
                return False

class Dealer:

    def __init__(self): 
        self.all_cards = []
        self.total = 0

    def add_card(self,new_cards):
        if type(new_cards)== type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
    def add_hidden(self,card):
        self.hidden_card = card
    def unhide(self):
        print(self.hidden_card)
    def display(self):
        for i in range(len(self.all_cards)):
            print(self.all_cards[i])
    def total_value(self):
        for i in range(len(self.all_cards)):
            self.total += self.all_cards[i].value
        self.total += self.total+self.hidden_card.value
        return self.total
    def ace(self):
        for i in range(len(self.all_cards)):
            if "Ace" == self.all_cards[i].rank or "Ace" == self.hidden_card.rank:
                return True
            else:
                return False

#game logic
deck = Deck()
deck.shuffle()
player = Player("Rutul", 1000)
dealer = Dealer() 
again =True
while again: 
    #player bet
    player.place_bet()
    print("Your Balance: ",player.bank)

    #First distribution of cards
    #player
    player.add_cards(deck.deal_one())
    player.add_cards(deck.deal_one())

    #dealer
    dealer.add_card(deck.deal_one())
    dealer.add_hidden(deck.deal_one())

    #Displaying the appropriate cards
    player.display()
    print("\nDealer's cards:")
    dealer.display()

    def check_winp():
        #check 
        global turn,game_on
        if player.total_value()>21:
            turn = False
            game_on = False
            print("Player Burst!")
            print("Your Balance: ",player.bank)
        elif player.total_value()<=21:
            pass
    game_on = True
    turn = True

        
    #asking player choice
    while turn:
        print("1.Hit\n2.Stay")
        temp = int(input("Enter your choice (1 or 2): "))
        if temp == 1 : 
            player.add_cards(deck.deal_one())
            player.display()
            print("\nDealer's cards:")
            dealer.display()
            check_winp()
        elif temp == 2:
            break
        else:
            print("Invalid input!Try again!")
    def check_wind():
        #check 
        global game_on
        if dealer.total_value()>21:
            game_on = False
            print("Dealer Burst! Player wins!")
            player.bank += 2*player.amount
            print("Your Balance: ",player.bank)
        elif dealer.total>player.total:
            game_on = False
            print("Dealer wins player loses!")
            print("Your Balance: ",player.bank)
        else:
            pass

    while game_on:
        print("stay")
        dealer.add_card(deck.deal_one())    
        player.display()
        print("\nDealer's cards")
        dealer.display()
        dealer.unhide()
        check_wind()
    ag =input("Want to Play again?(Y)")
    if ag.upper() == "Y":
        pass
    else:
        again = False
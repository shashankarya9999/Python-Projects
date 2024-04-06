import random

suits = ('hearts','diamonds','spades','clubs')
ranks = ('two','three','four','five','six','seven','eight','nine','ten','jack','queen','king','ace')
values = {'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'jack':10,'queen':10,'king':10,'ace':11}

playing = True

class Card():
    def __init__(self,suit,rank):
        self.suit = suit.lower()
        self.rank = rank.lower()

    def __str__(self):
        return self.rank + " of " + self.suit

class Deck():
    def __init__(self):
        self.deck = []

        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def __str__(self):
        deck_comp = ''

        for card in self.deck:
            deck_comp += '\n' + card.__str__()

        return "The deck has: " + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self): 
        single_card = self.deck.pop()
        return single_card

class Hand:
    def __init__(self):
        self.cards = []      # starts with an empty list
        self.value = 0       # start with zero value
        self.aces = 0        # adds an attribute to keep track of aces

    def add_card(self,card):
        self.cards.append(card)     # card passed in from Deck.deal() --> single Card(suit,rank)
        self.value += values[card.rank]

        # track aces
        if card.rank == 'ace':
            self.aces += 1
            
    def adjust_for_ace(self):
        
        # if total value > 21 and I still have an ace
        # then change my ace to be 1 instead of an 11
         
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1

class Chips:
    def __init__(self,total = 100):
        self.total = total      # can be a default value or supplied by user input
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):
    while True:

        try:
            chips.bet = int(input("How many chips would you like to bet?: "))
            
        except:
            print("Sorry, Please provide an integer!")

        else:
            if chips.bet > chips.total:
                print("Sorry, you do not have enough chips!")
                print("You have: {}".format(chips.total))

            else:
                break

def hit(deck,hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing      # to control an upcoming while loop

    while True:
        x = input("Hit or Stand? Enter 'h' or 's': ")

        if x[0].lower() == 'h':
            hit(deck,hand)

        elif x[0].lower() == 's':
            print("Player Stands, Dealer's Turn")
            playing = False

        else:
            print("Sorry, Please enter h or s only!")
            continue
        break

def show_some(player,dealer):    
    # dealer.cards[1]
    # show only one of the dealer's cards
    
    print("\n Dealer's Hand: ")
    print("First card hidden!")
    print(dealer.cards[1])

    # show all of the player's cards/hand

    print("\n Player's hand:")
    for card in player.cards:
        print(card)

def show_all(player,dealer):
    # show all of dealer's cards
    print("\n Dealer's hand:")
    for card in dealer.cards:
        print(card)

    # calculate and display value(J+k==20)
    print("Value of Dealer's Hand is: {}".format(dealer.value))

    # show all of the player's cards
    print("\n Player's hand:")
    for card in player.cards:
        print(card)

    print("Value of Player's Hand is: {}".format(player.value))

def player_busts(player,dealer,chips):
    print("Bust Player!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player Wins!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Player Wins! Dealer Busted!")
    chips.win_bet()

def dealer_wins(player,dealer,chips):
    print("Dealer Wins!")
    chips.lose_bet()

def push(player,dealer):
    print("Dealer and Player tie! Push!")

# actual game logic
while True:
    print("Welcome to BlackJack")

    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # set up player's chips
    player_chips = Chips()

    # prompt player for their bet
    take_bet(player_chips)

    # show cards(but keep one dealer card hidden)
    show_some(player_hand,dealer_hand)

    while playing:      # this variable is from hit_or_stand function
        
        # prompt for player to hit or stand
        hit_or_stand(deck,player_hand)

        # show cards (but keep one dealer card hidden)
        show_some(player_hand,dealer_hand)

        # if player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break

    # if player hasn't busted, play dealer's hand until dealer reaches 17
    if player_hand.value <= 21:
        while dealer_hand.value < player_hand.value:
            hit(deck,dealer_hand) 
         
        # show all cards
        show_all(player_hand,dealer_hand)

        # run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand, player_chips)
        
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)

        else:
            push(player_hand,dealer_hand)
            
    # Inform Player of their chips total    
    print("\n Player total chips are at: {}".format(player_chips.total))

    # Ask to play again
    new_game = input("Would you like to play again? y/n: ")

    if new_game[0].lower() == 'y':
        playing = True
        continue

    else:
        print("Thank you for playing!")
        break

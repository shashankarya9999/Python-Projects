##################################################################################################################################################################
######################################################################  WAR CARD GAME  ###########################################################################
##################################################################################################################################################################

import random

suits = ('hearts','diamonds','spades','clubs')
rank = ('two','three','four','five','six','seven','eight','nine','ten','jack','queen','king','ace')
values = {'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'jack':11,'queen':12,'king':13,'ace':14}

class Card:       
    def __init__(self,suit,rank):
        self.suit = suit.lower()
        self.rank = rank.lower()
        self.values = values[rank.lower()]

    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:       
    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for ranks in rank:
                created_card = Card(suit,ranks)
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)      # this method does not return anything because this shuffling of list occurs in-place

    def deal_one(self):             # one card is being drawn out from deck and returned
        return self.all_cards.pop() 

class Player:
    def __init__(self,name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)        # for a list of multiple card objects
        else:
            self.all_cards.append(new_cards)        # for a single card object

    def __str__(self):
        return "Player {} has {} cards.".format(self.name,len(self.all_cards))      # f-string did not work in vs code

player_one = Player("One")
player_two = Player("Two")

new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True

round_num = 0

while game_on:
    round_num += 1
    print("Round {}".format(round_num))

    if len(player_one.all_cards) == 0:
        print('Player one, out of cards')
        print('Player two Wins!')
        game_on = False
        break

    if len(player_one.all_cards) == 0:
        print('Player two, out of cards')
        print('Player one Wins!')
        game_on = False
        break

    # Start a new round
    # Card the player leaves on the table

    player_one_cards = []
    player_one_cards.append(player_one.remove_one())      
    
    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    at_war = True
    
    while at_war:
        
        # -1 to make sure the latest card added in one_cards is compared.
        if player_one_cards[-1].values > player_two_cards[-1].values:            
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war = False

        elif player_two_cards[-1].values > player_one_cards[-1].values:        
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            at_war = False

        else:
            print('WAR!')

            if len(player_one.all_cards) < 5:
                print('Player One unable to declare war.')
                print("Player Two Wins!")
                game_on = False
                break

            elif len(player_two.all_cards) < 5:
                print('Player Two unable to declare war.')
                print("Player One Wins!")
                game_on = False
                break

            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())

__author__ = 'ps'
#editted by ps

'''

'''
import math
import random

class Cards:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def show(self):
        print("{} of {}".format(self.rank, self.suit))    
    

class Deck:
    
    def __init__(self):
        self.cards = []
        self.build()

    #Creating a deck of 52 cards
    def build(self):
        self.cards = []
        for suit in ['Spades','Hearts','Diamonds','Clubs']:
            for rank in ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']:
                self.cards.append(Cards(rank, suit))                

    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self, n = 1):        
        #we shuffle using fisher yates algorithm
        lengthOfHand = len(self.cards)
        for _ in range(n):
            for i in range(lengthOfHand-1, 0, -1):
                randi = random.randint(0, i)
                if i == randi:
                    continue
                self.cards[i], self.cards[randi] = self.cards[randi], self.cards[i]
        return self.cards

    def deal(self):
        # we deal the top card
        # c= []
        for i in range(3):
            self.cards.append(self.cards.pop(0))        
        return self

    #to draw top most card
    def drawCard(self):
        return self.cards.pop(0)

# we deal and evaluvate the hand
class Hand:

    def __init__(self):        
        self.cards = []
        self.rankValue = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}        #Look up table for values

    # Updating new hand for the player
    def updateHand(newHand):
        self.cards = newHand

    def showHand(self):
        for c in self.cards:
            c.show()

    def sameRank(self, cardRank):
        count = 0
        for idx in range(3):
            if cardRank == self.cards[idx].rank:
                count+=1
        return count

    def evaluvateHand(self):
        onHand = self.cards

        #Dict for Evaluvating Hand
        pairings  = {'Name': 'None', 'Rank' : "None", 'card': [(card.rank, card.suit, sameRank(card.rank)) for card in onHand]}
        # sorting cards according to values from lookup table
        pairings["card"].sort(key = lambda card: self.rankValue[card[0]], reverse = True)
        return pairings


deck = Deck()
deck.shuffle(4)
card = deck.deal()
print(card.show())

        
    #     cardPairings["cards"].sort(key=lambda card:self.rankValue[card[0]], reverse= True)
    #     # Sort cards according to one amount of same ranks in hand
    #     cardPairings["cards"].sort(key=lambda card:card[2], reverse= True)

    #     if cardPairings["cards"][0][2] == 3:
    #         cardPairings["Category"] = "Three of a kind"
    #     elif cardPairings["cards"][0][2] == 2:
    #         cardPairings["Category"] = "Pair"
    #     else:
    #         cardPairings["Category"] = "One of a kind"
    #     pairing= cardPairings["cards"][0][2] 
    #     rank = cardPairings["cards"][0][0]


    #     cardPairings["Value"] = pow(10, pairing) * self.rankValue[rank]
    #     return cardPairings
    
    # # Print out the result
    # def countSameRank(self, cardRank):
    #     counter = 0
    #     for cardIndex in range(3):
    #         if cardRank == self.cards[cardIndex].rank:
    #             counter+=1
    #     return counter


from Lab1_Agents_Task2_Deck import Deck

# The cards here are dealth in namedTuple, so we can use the namedTuple.rank and namedTuple.suit for card infomation.

class Hand:

    def __init__(self):
        self.deck = Deck()
        self.hand = []

    def updateHand(self, cards):
        self.hand = cards

    def sameRank(self, card):  # returns the number of cards with same rank        
        count = 0        
        for idx in range(3):
            if card.rank == self.hand[idx].rank:
                count+=1
        return count


    def identifyHand(self):
        handType = {"category": " ","rank": [(card.rank,card.suit, self.deck.card_rank(card)) for card in self.hand],\
            "cards": [(card.rank,card.suit, self.sameRank(card)) for card in self.hand]}        
        if handType["cards"][0][2] == 2:
            handType["category"] = "pair"
        elif handType["cards"][0][2] == 3:
            handType["category"] = "three of a kind"
        else:
            handType["category"] = "high card" 
        return handType

'''
#doctest
deck = Deck()
player = Hand()
# player.updateHand(deck.deal_cards())
player.updateHand([Card(rank='J', suit='clubs'), Card(rank='J', suit='spades'), Card(rank='J', suit='hearts')])
result = player.identifyHand()
print('Player 1: ', result)
print(sorted(result['rank'], reverse = True))
'''


#########################
#      Game flow        #
#########################


#########################
# phase 1: Card Dealing #
#########################


#########################
# phase 2:   Bidding    #
#########################


#########################
# phase 2:   Showdown   #
#########################




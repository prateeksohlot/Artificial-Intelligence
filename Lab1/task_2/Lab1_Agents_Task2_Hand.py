from collections import namedtuple
from Lab1_Agents_Task2_Deck import Deck


Card = namedtuple('Card', ['rank', 'suit'])

# we deal and evaluvate the hand
class Hand(Deck):

    def __init__(self):
        Deck.__init__(self)
        self.hand = []

    def update_hand(self, new_hand):
        self.hand = new_hand
    
    def identify_hand(self):
        
        # If there is no pairing
        high_card = [self.card_rank(card) for card in self.hand].sort()[0]
        
        pass

    def sameRank(self, cardRank):
        count = 0
        for idx in range(3):
            if cardRank == self.cards[idx].rank:
                count+=1
        return count


    

'''



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
'''
# __author__ = 'fyt'

# identify if there is one or more pairs in the hand

# Rank: {2, 3, 4, 5, 6, 7, 8, 9, T, J, Q, K, A}
# Suit: {s, h, d, c}

# 2 example poker hands
CurrentHand1 = ['10d', '10s', '2c']
CurrentHand2 = ['5s', '5c', '5d']

# identify hand category using IF-THEN rule
def identifyHand(Hand_):
    for c1 in Hand_:
        for c2 in Hand_:
            if (c1[0] == c2[0]) and (c1[1] < c2[1]):
                yield dict(name='pair',rank=c1[0],suit1=c1[1],suit2=c2[1])

# Print out the result
def analyseHand(Hand_):
    HandCategory = []

    functionToUse = identifyHand

    for category in functionToUse(Hand_):
        print('Category: ')
        for key in "name rank suit1 suit2".split():
            print (key,"=",category[key])

# identifyHand(CurrentHand1)
analyseHand(CurrentHand1)
# analyseHand(CurrentHand2)








































# import random as rand

# # Building a card dealer for 2 players

# class cardDealer(list):    
    
#     # The class deals 3 cards to two players/agents for poker game
#     # We initialise a deck, build one and then deal it to 2 players
    
#     # We initialise the deck and players here
     
#     def __init__(self):
#         self.deck = []
#         self.Deck()
#         self.agent1 = []
#         self.agent2 = []
        
#     # We create a deck from 13 different values and four different deck.
#     def Deck(self):
#         card_rank = ['2','3','4','5','6','7','8','9','10','J','Q','K','A'] #here, A is considered as higherst card
#         card_suit = ['S','H','D','C'] #Spades, hearts, diamonds and clubs

#         for suit in card_suit:
#             for rank in card_rank:
#                 self.deck.append(f'{rank}{suit}')


#     #We deal the deck to the players
#     def deal(self):
#         for i in range(3):
#             a = rand.choice(self.deck)
#             self.deck.remove(a)
#             self.agent1.append(a)

#             b = rand.choice(self.deck)
#             self.deck.remove(b)
#             self.agent2.append(b)

#         return self.agent1, self.agent2

# '''
# The hands we have in lab are 
# - Three of a kind
# - Two pairs
# - Pair
# - High Card

# if we have a tie in rank, we suit suits as tie breaker where clubs(lowest),
# Diamonds, hearts and Spades(Highest)
# '''


# class scoring(object):

#     def __init__(self):
#         self.cards = cards
        
#     def pair(self):
#         pairs = []

#         for i in range(len(self.cards)):
#             for j in range(len(self.cards)):
#                 if j <= i:
#                     continue
                
#                 if self.cards[i][0] == self.cards[j][0]:
#                     count += 1
#                     hand.append([self.cards[i], self.cards[j]])

#         return pairs

#     def threeKind(self):

#         if self.cards[0][0] == self.cards[1][0] and self.cards[0][0] == self.cards[2][0]:
#             return True

#     def highCard(self):
        
#         card = []
#         for i in self.cards:
#             card.append(int(i[0]))

#         return max(card)


# if __name__ == "__main__" :
    
#     cd = cardDealer()
#     sc = scoring()
#     player1, player2 = cd.deal()
#     # print(player1)

#     analyse(player1)
#     analyse(player2)
#     print(player1, player2)




#     # hand.analyse(player1)
#     # for i in player1:
#     #     print(i.values)

#     # print(player1, player2)

    
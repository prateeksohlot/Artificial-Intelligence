__author__ = 'Prateek Sohlot' 

from collections import namedtuple
import random

Card = namedtuple('Card', ['rank', 'suit'])
    

class Deck:

    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    suit_value = dict(spades=3, hearts=2, diamonds=1, clubs=0)
    
    def __init__(self):  
        #creating a 52 card deck using nested for loop      
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]        
        self.shuffle()        

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def card_rank(self, Card):
        rank_value = self.ranks.index(Card.rank) #returns first index of rank
        return rank_value * len(self.suit_value) + self.suit_value[Card.suit]

    def shuffle(self, n = 3):        
    #we shuffle using fisher yates algorithm
        lengthOfHand = len(self._cards)
        for _ in range(n):
            for i in range(lengthOfHand-1, 0, -1):
                randi = random.randint(0, i)
                if i == randi:
                    continue
                self._cards[i], self._cards[randi] = self._cards[randi], self._cards[i]
        return self._cards

    def top_card(self):        
        return self._cards.pop(0)

'''
#doctest

deck = Deck()
a = random.choice(deck)
print("Size of Deck :", len(deck))         S
print("draw random card :", random.choice(deck))  
print("using shuffle", deck[0])
print("random card rank:", a, deck.card_rank(a))  

'''

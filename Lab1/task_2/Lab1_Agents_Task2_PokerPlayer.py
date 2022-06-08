
# __author__ = 'Prateek'
import math, random
from Lab1_Agents_Task2_Deck import Cards, Deck, Hand

class pokerplayer:
    def __init__(self, name = None):
        self.name = name
        self.playerHand = []
        self.lastOpponentHand = None
        

    def draw(self, deck, num = 1):
        for i in range(num):
            self.playerHand.append(deck.drawCard())        
        

    def showHand(self):
        print("{} has cards: \n".format(self.name))
        for card in self.playerHand:
            card.show()
        
    def lastopponentHand(self):
        self.lastOpponentHand = opponentHand
        

deck = Deck()
deck.shuffle()

yun = pokerplayer('yun')
yun.draw(deck, num = 3)
yun.showHand()




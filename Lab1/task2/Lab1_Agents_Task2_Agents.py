__author__ = 'Prateek Sohlot'

import random
from Lab1_Agents_Task2_Hand import Hand

class randomAgent(Hand):
    '''
    Random Poker playing Agent
    '''
    def __init__(self, name):
        super().__init__()   
        self.name = name
        self.type = 'Random'

    def calculateBid(self):
        return random.randint(1,50)

    def __str__(self) -> str:
        f'{self.name}'

class reflexAgent(Hand):
    '''
    Reflex Poker playing Agent
    '''
    ranks = [str(n) for n in range(2,11)] + list('JQKA')

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.type = 'Reflex'

    def calculateBid(self):
        amount = (self.sameRank(self.hand[0]) - 1)*19 + self.ranks.index(self.hand[0].rank)-2
        return amount

class fixedAgent(Hand):
    '''
    Fixed Poker playing Agent
    '''
    ranks = [str(n) for n in range(2,11)] + list('JQKA')

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.stepValue = 1
        self.type = 'Fixed'

    def calculateBid(self):
        amount = 9 * self.stepValue
        self.stepValue +=1
        if self.stepValue == 5:
            self.stepValue = 1
        return amount






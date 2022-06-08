
import math, random

class randomAgent:
    def __init__(self):
        super.__init__()
        self.type = "Random"

    def calculateBid(self):
        return random.randint(0,50)


class fixedAgent:
    def __init__(self):
        super.__init__()
        self.type = "Fixed"

    def calculateBid(self):
        return random.randint(0,50)
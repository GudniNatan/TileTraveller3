class Player(object):
    def __init__(self):
        self.xcord = 1
        self.ycord = 1
        self.coins = 0
        self.name = ""

    def move(self):
        pass

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def AddCoin(self):
        pass
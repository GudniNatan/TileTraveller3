class Tile(object):
    def __init__(self, x: int, y: int, coins: int,
                 win_tile: bool):
        self.x = x
        self.y = y
        self.neighbors = list()
        self.coins = coins
        self.win_tile = win_tile

    def set_neighbors(self, neighbors):
        self.neighbors = neighbors
    
    def has_lever(self):
        if self.coins > 0:
            return True
        else:
            return False


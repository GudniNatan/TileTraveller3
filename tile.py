class Tile(object):
    def __init__(self, x: int, y: int, neighbors: dict,
                 coins: int, win_tile: bool):
        self.x = x
        self.y = y
        self.neighbors = neighbors
        self.coins = coins
        self.win_tile = win_tile

    def set_neighbors(self, neighbors):
        self.neighbors = neighbors

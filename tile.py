class Tile(object):
    def __init__(self, x: int, y: int, coins: int,
                 win_tile: bool):
        self.x = x
        self.y = y
        self.neighbors = set()
        self.coins = coins
        self.win_tile = win_tile

    def set_neighbors(self, neighbors):
        self.neighbors = neighbors

    def get_neighbor(self, coordinates: tuple):
        for tile in self.neighbors:
            if (tile.x, tile.y) == coordinates:
                return tile
        return self

    def has_lever(self):
        return self.coins > 0

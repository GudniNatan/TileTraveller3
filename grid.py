from tile import Tile


class Grid(object):
    def __init__(self, width, height, walls, coins,
                 player_location=(0, 0), player_coins=0):
        self.tiles = tiles = list()
        self.width = width
        self.height = height
        self.walls = walls
        self.coins = coins
        self.player_location = player_location
        self.player_coins = player_coins
        for x in range(width):
            for y in range(height):
                pass
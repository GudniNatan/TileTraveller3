from tile import Tile
from player import Player


class Grid(object):
    def __init__(self, width, height, walls, coins,
                 player_location=(1, 1), player_coins=0):
        self.tiles = dict()
        self.width = width
        self.height = height
        self.walls = walls
        self.coins = coins
        self.make_tiles()
        self.player = Player(self.tiles[player_location], player_coins)

    def make_tiles(self):
        width = self.width
        height = self.height
        walls = self.walls
        tiles = self.tiles
        for x in range(1, width + 1):
            for y in range(1, height + 1):
                wintile = (x, y) == (width, 1)
                tile = Tile(
                    x, y, self.coins[(x, y)]
                )
                tiles[(x, y)] = tile
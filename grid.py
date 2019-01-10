from tile import Tile


class Grid(object):
    def __init__(self, width, height, walls, coins,
                 player_location=(0, 0), player_coins=0):
        self.tiles = list()
        for x in range(width)
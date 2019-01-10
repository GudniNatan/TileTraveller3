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
        self.make_walls()

    def make_tiles(self):
        width = self.width
        height = self.height
        walls = self.walls
        tiles = self.tiles
        for x in range(1, width + 1):
            for y in range(1, height + 1):
                wintile = (x, y) == (width, 1)
                tile = Tile(
                    x, y, self.coins.get((x, y), 0), wintile
                )
                tiles[(x, y)] = tile

    def make_walls(self):
        for tile in self.tiles.values():
            proposed_neighbors = [
                (tile.x-1, tile.y), (tile.x + 1, tile.y),
                (tile.x, tile.y-1), (tile.x, tile.y+1)
            ]
            for neighbor in proposed_neighbors:
                if neighbor in self.tiles:
                    for wall in self.walls:
                        if (tile.x, tile.y) not in wall and neighbor not in wall:
                            tile.neighbors.add(self.tiles[neighbor])
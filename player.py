class Player(object):
    def __init__(self, start_tile, coins):
        self.tile = start_tile
        self.coins = 0

    def move(self, direction):
        direction = direction.lower()
        x = self.tile.x
        y = self.tile.y
        if direction == "n":
            prospect = (x, y + 1)
        elif direction == "s":
            prospect = (x, y - 1)
        if direction == "e":
            prospect = (x + 1, y)
        elif direction == "w":
            prospect = (x - 1, y)
        self.tile = self.tile.get_neighbor(prospect)

    def look(self):
        neighbors = self.tile.neighbors
        coordinates = (self.tile.x, self.tile.y)
        directions = list()
        for tile in neighbors:
            if tile.y > self.tile.y:
                directions.append("(N)orth")
            if tile.y < self.tile.y:
                directions.append("(S)outh")
            if tile.x > self.tile.x:
                directions.append("(E)ast")
            if tile.x < self.tile.x:
                directions.append("(W)est")
        return " or ".join(directions)

    def add_coins(self, amount):
        self.coins += amount

    def get_location(self):
        return (self.x, self.y)
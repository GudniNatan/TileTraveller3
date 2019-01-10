from grid import Grid


def load_game(filename):
    with open(filename) as a_file:
        file_content = [line.strip() for line in a_file]
    # [width height,[walls], [coins],[playerlocation],[playercoins]]
    width, height = [int(x) for x in file_content[0]]
    walls = eval(file_content[1])
    coins = eval(file_content[2])
    playerlocation = eval(file_content[3])
    playercoins = int(file_content[4])
    return Grid(width, height, walls, coins, playerlocation, playercoins)


def save_game(filename):
    pass


def main():
    # read game file location and load game
    filename = input('Enter filename: ') 

    grid = load_game(filename)

    player = grid.player
    # game loop goes here
    win = False
    while player.tile.win_tile == False:
        # print lever info
        if player.tile.has_lever():
            pull_lever = input("Pull a lever (y/n): ")
            if pull_lever.lower() == "y":
                coins = player.tile.coins
                player.tile.coins = 0
                player.coins += coins
                print("You received {} coins, your total is now {}.".format(coins, player.coins))
        print("You can travel: ", player.look())
        direction = input("Direction: ")
        old_tile = player.tile
        player.move(direction)
        if player.tile is old_tile:
            print("Not a valid direction!")
    print("Victory!")


main()

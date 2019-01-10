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


    # game loop goes here
    win = False
    while win == False:
        # do something
        # print lever info
        
        pass

main()

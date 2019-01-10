from grid import Grid


def load_game(filename):
    with open(filename) as a_file:
        file_content = [line.strip() for line in a_file]
    # [width height,[walls], [coins],[playerlocation],[playercoins]]
    width, height = file_content[0].split()
    walls = file_content[1]
    coins = file_content[2]
    playerlocation = file_content[3]
    playercoins = file_content[4]


def save_game(filename):
    pass


def main():
    # read game file location and load game
    filename = input('Enter filename: ')
    load_game(filename)
    

            


    # game loop goes here
    pass

main()

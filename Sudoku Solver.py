import math

board = {}


# Start?
def start():
    loadBoard(3, 3)

    # Top Left 0,0
    preloadNumbers(0, 0, 5)
    preloadNumbers(1, 0, 3)
    preloadNumbers(0, 1, 6)
    preloadNumbers(1, 2, 9)
    preloadNumbers(2, 2, 8)
    preloadNumbers(4, 0, 7)

    displayBoard()


# Create an empty board
def loadBoard(width, height):
    for x in range(width * 3):
        for y in range(height * 3):
            board[str(x) + "-" + str(y)] = 0


# Preload the Numbers in the Board
def preloadNumbers(x, y, num):
    board[str(x) + "-" + str(y)] = num


# Display the board
def displayBoard():
    lineNum = int((int(math.sqrt(len(board.values())))) + ((int(math.sqrt(len(board.values())))) / 3) + 1)

    seperator = ""
    for sep in range(int(lineNum)):
        seperator = seperator + "- "
    print(seperator)

    line = "| "
    for y in range(int(math.sqrt(len(board.values())))):
        for x in range(int(math.sqrt(len(board.values())))):
            seperator = " "
            if (x + 1) % 3 == 0:
                seperator = " | "
            line = line + str(board[str(x) + "-" + str(y)]) + seperator
        print(line)
        if (y + 1) % 3 == 0:
            seperator = ""
            for sep in range(int(len(line) / 2)):
                seperator = seperator + "- "
            print(seperator)
        line = "| "


start()

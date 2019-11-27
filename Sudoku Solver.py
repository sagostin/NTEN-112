import math

board = {}


# Start?
def start():
    loadBoard(3, 3)

    # 0,0
    preloadNumbers(0, 0, 5)
    preloadNumbers(1, 0, 3)
    preloadNumbers(0, 1, 6)
    preloadNumbers(1, 2, 9)
    preloadNumbers(2, 2, 8)

    # 0,1
    preloadNumbers(4, 0, 7)
    preloadNumbers(3, 1, 1)
    preloadNumbers(4, 1, 9)
    preloadNumbers(5, 1, 5)

    # 0,2
    preloadNumbers(7, 2, 6)

    # 1,0
    preloadNumbers(0, 3, 8)
    preloadNumbers(0, 4, 4)
    preloadNumbers(0, 5, 7)

    # 1,1
    preloadNumbers(4, 3, 6)
    preloadNumbers(3, 4, 8)
    preloadNumbers(5, 4, 5)
    preloadNumbers(4, 5, 2)

    # 1,2
    preloadNumbers(8, 3, 3)
    preloadNumbers(8, 4, 1)
    preloadNumbers(8, 5, 6)

    # 2,0
    preloadNumbers(1, 6, 6)

    # 2,1
    preloadNumbers(3, 7, 4)
    preloadNumbers(4, 7, 1)
    preloadNumbers(5, 7, 9)
    preloadNumbers(4, 8, 8)

    # 2,2
    preloadNumbers(6, 6, 2)
    preloadNumbers(7, 6, 8)
    preloadNumbers(8, 7, 5)
    preloadNumbers(7, 8, 7)
    preloadNumbers(8, 8, 9)

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

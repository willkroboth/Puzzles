from math import sqrt, floor



def amountOf1s(list):
    amount = 0
    for value in list:
        if value == 1:
            amount += 1
    return amount


def is_int(input):
  try:
    num = int(input)
  except ValueError:
    return False
  return True


def spreadList(list):
    newList = []
    for x in list:
        for y in x:
            newList.append(y)
    return newList


def changeSquares(squaresTochange, howToChange):
    global board
    for square in squaresTochange:
        x = square[0]
        y = square[1]
        for valueChanging in range(len(howToChange)):
            value = howToChange[valueChanging]
            if value == 0 or value == 1:
                board[y][x][valueChanging] = value


def checkForNewChanges():
    global board
    for y in range(len(board)):
        for x in range(len(board[y])):
            for valuePos in range(len(board[y][x])):
                value = board[y][x][valuePos]
                if value == 1:
                    sameRow = [[i, y] for i in range(board_length)]
                    sameColumn = [[x, i] for i in range(board_length)]
                    sameBox = chooseBox(x, y)
                    if countAmountOfN(sameRow, valuePos, 1) == 1 or countAmountOfN(sameColumn, valuePos, 1) == 1 \
                            or countAmountOfN(sameBox, valuePos, 1) == 1 or amountOf1s(board[y][x]) == 1:
                        toChange = []
                        number = valuePos + 1
                        for _ in range(number - 1):
                            toChange.append(2)
                        toChange.append(0)
                        for _ in range(board_length - number):
                            toChange.append(2)
                        changeSquares(spreadList([sameRow, sameColumn, sameBox]), toChange)

                        toChange = []
                        for _ in range(number - 1):
                            toChange.append(0)
                        toChange.append(1)
                        for _ in range(board_length - number):
                            toChange.append(0)
                        changeSquares([[x, y]], toChange)


def countAmountOfN(squaresToCheck, posToCheck, valueToVerify):
    global board
    amount = 0
    for square in squaresToCheck:
        x = square[0]
        y = square[1]
        if board[y][x][posToCheck] == valueToVerify:
            amount += 1
    return amount


def chooseBox(x, y):
    box_x = int(x/sqrt(board_length))
    box_y = int(y/sqrt(board_length))
    box = [[int(sqrt(board_length) * box_x + i), int(sqrt(board_length) * box_y + j)]
           for i in range(int(sqrt(board_length))) for j in range(int(sqrt(board_length)))]
    return box


def printBoard():
    global board
    for row in board:
        rowPrint = ''
        for square in row:
            rowPrint += '['
            if amountOf1s(square) == 1:
                value = str(square.index(1) + 1)
                while len(value) < len(str(board_length)):
                    value = "0" + value
                rowPrint += str(value)
            else:
                rowPrint += ' ' * len(str(board_length))
            rowPrint += '] '
        print(rowPrint)


def emptySpacesInBoard():
    global board
    for y in board:
        for x in y:
            if amountOf1s(x) != 1:
                return True
    return False

'''
def done():
    global board
    result = True
    for row in board:
        for square in row:
            amount = 0
            for value in square:
                if value == 1:
                    amount += 1
            if amount != 1:
                result = False
    return result
'''
print("How many squares across is your board?")
while True:
    board_length = input()
    if is_int(board_length):
        board_length = int(board_length)
        if sqrt(board_length) == floor(sqrt(board_length)):
            break

board = []

for _ in range(board_length):
    toAdd = []
    for _ in range(board_length):
        toAddToAdd = []
        for _ in range(board_length):
            toAddToAdd.append(1)
        toAdd.append(toAddToAdd)
    board.append(toAdd)

ineput = 0
while ineput != "d":
    printBoard()
    print("Press n for a new entry\nPress r to remove an entry")
    # print("Press o to enter a row\nPress c to enter a column")
    print("Press g to go through all of the coordinates")
    print("Press d when your done entering numbers")
    ineput = input()
    if ineput == 'n':
        while True:
            print("What is the x coordinate? (The top-left corner is 0-0)")
            x = input()
            if is_int(x):
                x = int(x)
                if 0 <= x <= board_length - 1:
                    break

        while True:
            print("What is the y coordinate? (The top-left corner is 0-0)")
            y = input()
            if is_int(y):
                y = int(y)
                if 0 <= y <= board_length - 1:
                    break
        while True:
            print("What is it's number")
            number = input()
            if is_int(number):
                number = int(number)
                if 1 <= number <= board_length:
                    break

        toChange = []
        for _ in range(number-1):
            toChange.append(0)
        toChange.append(1)
        for _ in range(board_length - number):
            toChange.append(0)

        changeSquares([[x, y]], toChange)
    elif ineput == 'r':
        while True:
            print("What is the x coordinate? (The top-left corner is 0-0)")
            x = input()
            if is_int(x):
                x = int(x)
                if 0 <= x <= board_length - 1:
                    break

        while True:
            print("What is the y coordinate? (The top-left corner is 0-0)")
            y = input()
            if is_int(y):
                y = int(y)
                if 0 <= y <= board_length - 1:
                    break
        changeSquares([[x, y]], [1] * board_length)
    elif ineput == 'g':
        for y in range(board_length):
            for x in range(board_length):
                while True:
                    print("What is the number in square x: " + str(x) + " y: " + str(y) + "? (The top-left corner is 0-0 and click 0 for a blank)")
                    value = input()
                    if is_int(value):
                        value = int(value)
                        if 0 <= value <= board_length:
                            break
                if value != 0:
                    toChange = []
                    for _ in range(value - 1):
                        toChange.append(0)
                    toChange.append(1)
                    for _ in range(board_length - value):
                        toChange.append(0)
                    changeSquares([[x, y]], toChange)
                printBoard()
        print()
    """ not working
    elif ineput == 'o':

        while True:
            print("What is the y coordinate of the row?(0,0 is the top left corner)")
            rowY = input()
            if is_int(rowY):
                rowY = int(rowY)
                if 0 <= rowY <= board_length - 1:
                    break

        while True:
            print("What are the values of the row going from left to right?(blank spaces are 0)"
                  "(make sure each value has " + str(len(str(board_length))) + " digits long)")
            rowValues = input()
            if is_int(rowValues):
                rowValuesCheck = int(rowValues)
                if 0 <= rowValuesCheck <= int(str(board_length) * board_length):
                    break

        for valuePos in range(int(rowValues)):
            value = int(rowValues[valuePos])
            toChange = []
            for _ in range(value - 1):
                toChange.append(0)
            toChange.append(1)
            for _ in range(board_length - value):
                toChange.append(0)
            changeSquares([[valuePos, rowY]], toChange)

    elif ineput == 'c':
        while True:
            print("What is the x coordinate of the column?(0,0 is the top left corner)")
            columnX = input()
            if is_int(columnX):
                columnX = int(columnX)
                if 0 <= columnX <= board_length - 1:
                    break
        while True:
            print("What are the values of the row going from left to right?(blank spaces are 0)(make sure value is "
                  + str(len(str(board_length))) + " digits long)")

            columnValues = input()
            if is_int(columnValues):
                columnValuesCheck = int(columnValues)
                if 0 <= columnValuesCheck <= int(str(board_length) * board_length):
                    break

        for valuePos in range(int(columnValues)):
            value = int(columnValues[valuePos])
            toChange = []
            for _ in range(value - 1):
                toChange.append(0)
            toChange.append(1)
            for _ in range(board_length - value):
                toChange.append(0)
            changeSquares([[columnX, valuePos]], toChange)
"""

for _ in range(10):
    if emptySpacesInBoard():
        checkForNewChanges()
        while True:
            savedBoard = board
            checkForNewChanges()
            if savedBoard == board:
                break
        print()
        printBoard()

while True:
    print("Do you need to know a value?")
    print("c for check\nd for done")
    answer = input()
    if answer == "c":
        print("what is the x")
        x = int(input())
        print("what is the y")
        y = int(input())
        print(board[y][x])
    else:
        break

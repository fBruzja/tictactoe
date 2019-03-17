import random

def printBoard(board):
    print("   |   |   ")
    print(" " + board[1] + " |" + " " + board[2] + " |" + " " + board[3])
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" " + board[4] + " |" + " " + board[5] + " |" + " " + board[6])
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" " + board[7] + " |" + " " + board[8] + " |" + " " + board[9])
    print("   |   |   ")
    print("\n")

def askForXorO():
    choices = []
    letter = ''
    
    while not (letter == "X" or letter == "Y"):
        letter = input("Do you want to start with 'X' or 'Y'?").upper()
        
    if letter == 'X':
        return [ letter, "O" ]
    else:
        return [ letter, "X" ]

def whoGoesFirst():
    return random.randint(0, 1)

def isSpaceFree(board, move):
    return board[move] == " "

def playerMoves(board):
    move = " "
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        move = input("Choose your tile: (1-9)")

    return int(move)

def executeMove(board, letter, move):
    board[move] = letter

def isTheBoardFull(board):
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

def checkIfWon(board, letter):
    return ((board[1] == letter and board[4] == letter and board[7] == letter) or
            (board[1] == letter and board[2] == letter and board[3] == letter) or
            (board[3] == letter and board[6] == letter and board[9] == letter) or
            (board[7] == letter and board[8] == letter and board[9] == letter) or
            (board[1] == letter and board[5] == letter and board[9] == letter) or
            (board[3] == letter and board[5] == letter and board[7] == letter) or
            (board[4] == letter and board[5] == letter and board[6] == letter) or
            (board[2] == letter and board[4] == letter and board[7] == letter))

def getBoardCopy(board):
    return board.copy()


def chooseRandomMoveFromList(board, moveList):
    possibleMoves = []
    for i in moveList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):
    if computerLetter == "X":
        playerLetter = "O"
    else:
        playerLetter = "X"

    # AI Algorithm

    # Can it win?
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            executeMove(boardCopy, computerLetter, i)
            if checkIfWon(boardCopy, computerLetter):
                return i

    # Can the player win on the next move?
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            executeMove(boardCopy, playerLetter, i)
            if checkIfWon(boardCopy, playerLetter):
                return i

    # Take one of the corners.
    move = chooseRandomMoveFromList(board, [1,3,7,9])
    if move != None:
        return move

    # Take center if free
    if isSpaceFree(board, 5):
        return 5

    # Lastly move on one of the sides
    return chooseRandomMoveFromList(board, [2,4,6,8])

def playAgain():
    print("Do you want to play again? (y or n)")
    return input().lower().startswith('y')

def start():
    theBoard = {1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ",8: " ", 9: " "}
    gameOver = False
    
    playerLetter, computerLetter = askForXorO()
    turn = whoGoesFirst()

    while not gameOver:
        printBoard(theBoard)
        if turn == 0:
            #player's turn
            move = playerMoves(theBoard)
            executeMove(theBoard, playerLetter, move)
            
            if checkIfWon(theBoard, playerLetter):
                printBoard(theBoard)
                print("You won! Congrats!")
                gameOver = True
            
            else:
                if isTheBoardFull(theBoard):
                    printBoard(theBoard)
                    print("The game is a tie!")
                else:
                    turn = 1
        else:
            # computer's turn
            move = getComputerMove(theBoard, computerLetter)
            executeMove(theBoard, computerLetter, move)
            if checkIfWon(theBoard, computerLetter):
                printBoard(theBoard)
                print("The computer has won!")
                gameOver = True
            else:
                if isTheBoardFull(theBoard):
                    printBoard(theBoard)
                    print("The game is a tie!")
                else:
                    turn = 0

    if playAgain():
        start()
        
start()

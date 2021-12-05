#Written by Brandon Reid

import random, sys, os
DEBUG = True
numInputs = 0

#Boards


#take difficulty level
#def bombPlacer(board, difficulty)
def bombPlacer(board, difficulty):    
    #variables
    rows = len(board)
    cols = len(board[0])
    area = rows * cols    
    numBombsPlaced = 0    
    bombBoard = board[:]
    
    numBombs = int(area / 4)

    
    if difficulty == "Easy" or difficulty == "easy":
        numBombs = int(area / 8)
    elif difficulty == "Medium" or difficulty == "medium":
        numBombs = int(area / 6)
    else:
        numBombs = int(area / 4)


    if DEBUG:
        print("Num rows: ", rows)
        print("Num cols: ", cols)
        print("Area = ", area)
        print("Number of bombs = ", numBombs)  

    #places bombs
    while numBombsPlaced < numBombs:
        r = random.randint(1, rows)
        c = random.randint(1, cols)
        if DEBUG:
            print("Random row: ", r)
            print("Random col: ", c)
        if not bombBoard[r - 1][c - 1] == "|B|":
            bombBoard[r - 1][c - 1] = "|B|" 
            numBombsPlaced += 1
        if DEBUG:
            print("Num of bombs placed: ", numBombsPlaced)

    #problem here
    
    for i in range (numBombs):
        r = random.randint(1, rows)
        c = random.randint(1, cols)
        if DEBUG:
            print("Random row: ", r)
            print("Random col: ", c)
        if not bombBoard[r - 1][c - 1] == "|B|":
            bombBoard[r - 1][c - 1] = "|B|"    


    if DEBUG:
        print("*******This is your bomb board*********")        
        boardPrinter(bombBoard) 

    #print("Bomb board")
    #boardPrinter(board[:]) 

    return bombBoard      


#*******************Prompts*********************
def mainMenu(): 
    print( '''
    MAIN MENU
    =========
    Instructions: Enter the coordinate that you would like to uncover.
    ''')

#Function to prompt and check row input
def rowPrompt():
    check = False
    numRows = 0
    while check == False:
        numRows = input("How many rows would you like? (2-30): ")
        try:
            val = int(numRows)
            if val >= 2 and val <=30:
                break
            else:
                print("Error! Invalid Output. Try Again.")
        except ValueError:
            print("Error! Not a valid integar. Try Again.")
    return int(numRows)

#Function to prompt and check column input
def colPrompt():
    check = False
    numCols = 0
    while check == False:
        numCols = input("How many columns would you like? (2-30): ")
        try:
            val = int(numCols)
            if val >= 2 and val <=30:
                break
            else:
                print("Error! Invalid Output. Try Again.")
        except ValueError:
            print("Error! Not a valid integar. Try Again.")
    return int(numCols)

def diffPrompt():
    check = True
    choice = ''
    while check == True:
        choice = input('What difficulty level would you like to play at?: ' )
            
        if choice == 'Easy' or choice == 'easy' or choice == 'Medium'  or choice == 'medium' or choice == 'Hard' or choice == 'hard':
            break
        else:  
            print("Erorr! Not a valid string  ")   

    return choice

#Function to gather player column choice
def xPrompt(col):
    check = False
    colChoice = 0
    while check == False:
        colChoice = input("Which column would you like to select: ")
        try:
            val = int()
            val = int(colChoice)
            if val > 0 and val <= col:
                break
            else:
                print("Error! Invalid Output. Try Again.")
        except ValueError:
            print("Error! Not a valid integar. Try Again.")
    return int(colChoice)

#Function to gather player row choice
def yPrompt(row):
    check = False
    rowChoice = 0
    while check == False:
        rowChoice = input("Which row would you like to select: ")
        try:
            val = int(rowChoice)
            if val > 0 and val <= row:
                break
            else:
                print("Error! Invalid Output. Try Again.")
        except ValueError:
            print("Error! Not a valid integar. Try Again.")
    return int(rowChoice)

#Function to check continue or new game input
def menuPrompt():
    check = False
    choice = 'g'
    while check == False:
        choice = input("Would you like to start a new game or continue a past game? (n,c): ")
        if (choice == 'n' or choice == 'N' or choice == 'C' or choice == 'c'):
            break
        else:
            print("Error! Invalid Output. Try Again.")
    return choice

def savePrompt():
    check = False
    choice = 'g'
    while check == False:
        choice = input('''Save game and quit. (s)
Quit. (q)
Continue. (c): ''')
        if (choice == 's' or choice == 'S' or choice == 'q' or choice == 'Q' or choice == 'c' or choice == 'C'):
            break
        else:
            print("Error! Invalid Output. Try Again.")
    return choice


def numBombs(displayBoard, bombBoard, xChoice, yChoice):
    #variables
    neighborCoords = []
    bombCount = 0
    length = len(bombBoard[0])
    width = len(bombBoard)
    
    if DEBUG:
        print("Length is: ", length)
        print("Width is: ", width)
    
    if hasBeenExposed(displayBoard, xChoice, yChoice):
        if DEBUG:
            print("We've already seen", xChoice, " ", yChoice)
        return -1

    #keeps recursion from going out of range
    if ((xChoice == 0) or (xChoice == length + 1) or (xChoice == -1) or (yChoice == 0) or (yChoice == width + 1) or (yChoice == -1)):
        return 0

    #check if player lost
    if bombBoard[yChoice - 1][xChoice - 1] == "|B|":
        print("You hit a bomb!. Game Over :(")
        sys.exit()      
  
    #handling special cases (edges)
    if xChoice == 1 and yChoice == 1: #top left corner
        midRow = bombBoard[0]
        bottomRow =bombBoard[1]
        neighborCoords.append([2, 1]) #rightCoords
        neighborCoords.append([2, 2]) #botRightCoords
        neighborCoords.append([1, 2]) #botCoords
        if midRow[1] == "|B|":
            bombCount += 1
        if bottomRow[0] == "|B|":
            bombCount += 1
        if bottomRow[1] == "|B|":
            bombCount += 1             
    elif xChoice == length and yChoice == 1: #top right corner
        midRow = bombBoard[0]
        bottomRow = bombBoard[1]
        neighborCoords.append([length - 2, 1]) #leftCoords
        neighborCoords.append([length - 2, 2]) #bottomLeftCoords
        neighborCoords.append([length - 1, 2]) #bottomCoords
        if midRow[length - 2] == "|B|":
            bombCount += 1
        if bottomRow[length - 2] == "|B|":
            bombCount += 1
        if bottomRow[length - 1] == "|B|":
            bombCount += 1
    elif xChoice == 1 and yChoice == width: #bottom left corner
        topRow = bombBoard[width - 2]
        midRow = bombBoard[width - 1]
        neighborCoords.append([1, width - 2]) #topCoords
        neighborCoords.append([2, width - 2]) #topRightCoords
        neighborCoords.append([2, width - 1]) #rightCoords
        if topRow[0] == "|B|":
            bombCount += 1
        if topRow[1] == "|B|":
            bombCount += 1
        if midRow[1] == "|B|":
            bombCount += 1
    elif xChoice == length and yChoice == width: #bottom right corner
        topRow = bombBoard[width - 2]
        midRow = bombBoard[width - 1]
        neighborCoords.append([length - 1, width - 2]) #topCoords
        neighborCoords.append([length - 2, width - 2]) #topLeftCoords
        neighborCoords.append([length - 2, width - 1]) #leftCoords
        if topRow[length - 2] == "|B|":
            bombCount += 1
        if topRow[length - 1] == "|B|":
            bombCount += 1
        if midRow[length - 2] == "|B|":
            bombCount += 1
    elif xChoice == 1 and (1 < yChoice < (width - 1)): #left side
        topRow = bombBoard[yChoice - 2]
        midRow = bombBoard[yChoice - 1]
        bottomRow = bombBoard[yChoice]
        neighborCoords.append([xChoice, yChoice - 1]) #topCoords
        neighborCoords.append([xChoice + 1, yChoice - 1]) #topRightCoords
        neighborCoords.append([xChoice + 1, yChoice]) #rightCoords
        neighborCoords.append([xChoice + 1, yChoice + 1]) #botRightCoords
        neighborCoords.append([xChoice, yChoice + 1]) #botCoords
        if topRow[0] == "|B|":
            bombCount += 1
        if topRow[1] == "|B|":
            bombCount += 1
        if midRow[1] == "|B|":
            bombCount += 1
        if bottomRow[1] == "|B|":
            bombCount += 1
        if bottomRow[0] == "|B|":
            bombCount += 1
    elif (xChoice == length and (1 < yChoice < width)): #right side
        topRow = bombBoard[yChoice - 2]
        midRow = bombBoard[yChoice - 1]
        bottomRow = bombBoard[yChoice]
        neighborCoords.append([xChoice, yChoice - 1]) #topCoords
        neighborCoords.append([xChoice - 1, yChoice - 1]) #topLeftCoords
        neighborCoords.append([xChoice - 1, yChoice]) #leftCoords
        neighborCoords.append([xChoice - 1, yChoice + 1]) #botLeftCoords
        neighborCoords.append([xChoice, yChoice + 1]) #botCoords
        if topRow[length - 2] == "|B|":
            bombCount += 1
        if topRow[length - 1] == "|B|":
            bombCount += 1
        if midRow[length - 2] == "|B|":
            bombCount += 1
        if bottomRow[length - 2] == "|B|":
            bombCount += 1
        if bottomRow[length - 1] == "|B|":
            bombCount += 1
    elif (1 < xChoice < length) and yChoice == 1: #top side
        midRow = bombBoard[0]
        bottomRow = bombBoard[1]
        neighborCoords.append([xChoice - 1, yChoice]) #leftCoords
        neighborCoords.append([xChoice - 1, yChoice + 1]) #botLeftCoords
        neighborCoords.append([xChoice, yChoice + 1]) #botCoords
        neighborCoords.append([xChoice + 1, yChoice + 1]) #botRightCoords
        neighborCoords.append([xChoice + 1, yChoice]) #rightCoords
        if midRow[xChoice - 2] == "|B|":
            bombCount += 1
        if midRow[xChoice] == "|B|":
            bombCount += 1
        if bottomRow[xChoice - 2] == "|B|":
            bombCount += 1
        if bottomRow[xChoice - 1] == "|B|":
            bombCount += 1
        if bottomRow[xChoice] == "|B|":
            bombCount += 1
    elif (1 < xChoice < length) and yChoice == width: #bottom side 
        topRow = bombBoard[yChoice - 2]
        midRow = bombBoard[yChoice - 1]
        neighborCoords.append([xChoice - 1, yChoice]) #leftCoords
        neighborCoords.append([xChoice - 1, yChoice - 1]) #topLeftCoords
        neighborCoords.append([xChoice, yChoice - 1]) #topCoords
        neighborCoords.append([xChoice + 1, yChoice - 1]) #topRightCoords
        neighborCoords.append([xChoice + 1, yChoice]) #rightCoords
        if midRow[xChoice - 2] == "|B|":
            bombCount += 1
        if midRow[xChoice] == "|B|":
            bombCount += 1
        if topRow[xChoice - 2] == "|B|":
            bombCount += 1
        if topRow[xChoice - 1] == "|B|":
            bombCount += 1
        if topRow[xChoice] == "|B|":
            bombCount += 1
    else: #normal cases
        topRow = bombBoard[yChoice - 2]
        midRow = bombBoard[yChoice - 1]
        bottomRow = bombBoard[yChoice]
        neighborCoords.append([xChoice - 1, yChoice]) #leftCoords
        neighborCoords.append([xChoice - 1, yChoice - 1]) #topLeftCoords
        neighborCoords.append([xChoice, yChoice - 1]) #topCoords
        neighborCoords.append([xChoice + 1, yChoice - 1]) #topRightCoords
        neighborCoords.append([xChoice + 1, yChoice]) #rightCoords
        neighborCoords.append([xChoice - 1, yChoice + 1]) #botLeftCoords
        neighborCoords.append([xChoice, yChoice + 1]) #botCoords
        neighborCoords.append([xChoice + 1, yChoice + 1]) #botRightCoords
        if topRow[xChoice - 2] == "|B|":
            bombCount += 1
        if topRow[xChoice - 1] == "|B|":
            bombCount += 1
        if topRow[xChoice] == "|B|":
            bombCount += 1
        if midRow[xChoice - 2] == "|B|":
            bombCount += 1
        if midRow[xChoice] == "|B|":
            bombCount += 1
        if bottomRow[xChoice - 2] == "|B|":
            bombCount += 1
        if bottomRow[xChoice - 1] == "|B|":
            bombCount += 1
        if bottomRow[xChoice] == "|B|":
            bombCount += 1    
    boardUpdater(displayBoard, bombCount, xChoice, yChoice) #updates board
    if bombCount == 0:
        for i, coords in enumerate(neighborCoords): #enumerates over neighbors to check the number of bombs around them
            if DEBUG:
                print("We have checked", i, "neighbors.")
                print("About to recurse", coords)
            numBombs(displayBoard, bombBoard, coords[0], coords[1])
    return bombCount

#function to update points on the board one at a time 
def boardUpdater(displayBoard, numBombs, x, y):
    #variables
    global numInputs 
    if numBombs == 0:
        val = "| |"
    else:   
        val = " " + str(numBombs) + " "     
    displayBoard[y - 1][x - 1] = val
    numInputs += 1
    if DEBUG:
        print("Board updated", x, y, val)
        print("There has been", numInputs, "spaces uncovered.")

#board simply to print numbered board to console
def boardPrinter(board):
    #variables
    x = len(board[0])
    y = len(board)
    print("******This is your board*******")
    #numbers columns
    for i in range(x):
        if i < 10:
            print("  ", i + 1, end = '')
        else:
            print(" ", i + 1, end = '')

    #print new line
    print(" ")

    #prints boards adds it to board list        
    for j in range(y): 
        row = board[j]
        print(j + 1, end = '')
        for i in range(x):
            if j >= 0 and j < 9:
                print("", row[i], end = '')
            elif j <= 30:
                print(row[i], "", end = '') 
        print(" ")  

#board to return a list of the board depending on the user input
def boardMaker(rows, cols):
    #variables
    emptyGrid = "|-|"
    board = []

    #loop to create regular board
    for j in range(rows): 
        row = []
        for i in range(cols):
            row.append(emptyGrid)
            
        print(" ") 
        board.append(row)

    return board

#function that returns if a certain point has been uncovered or not
def hasBeenExposed (displayBoard, xChoice, yChoice):
    if DEBUG:
        result = True
        print("Testing for exposure", xChoice, yChoice, displayBoard[yChoice - 1][xChoice - 1])
        result = (displayBoard[yChoice - 1][xChoice - 1] != "|-|") #possible fix
        print("Exposed?: ", result)
    return displayBoard[yChoice - 1][xChoice - 1] != "|-|"

#function to check if a player won
def isWinner (board):
    #variables
    rows = len(board)
    cols = len(board[0])
    area = rows * cols 
    if DEBUG:
        print("The area is ", area, "and the number of inputs is", numInputs)
    if numInputs == (area - 1):
        print("You won the game!")
        return True
    else:
        return False
        
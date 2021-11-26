#Written by Brandon Reid

import functions, sys, pickle
SEE_BOMBBOARD = False

#variables
numRows = 0
numCols = 0
rowChoice = 0
colChoice = 0
board = []
bombBoard = []
bombs = 0
menuChoice = 'F'
menuChoice2 = 'g'

#Welcome
print('''Welcome to MineSweeper v 1.0!

When playing for the first time, create a new game. If you have played already, you can continue where you left off.''')
#Prompt for new game or continue
menuChoice = functions.menuPrompt()  
if (menuChoice == 'n' or menuChoice == 'N'):
    print("New game created!")
    functions.mainMenu()
    numRows = functions.rowPrompt()
    numCols = functions.colPrompt()
    board = functions.boardMaker(numRows, numCols)
    bombBoard = functions.boardMaker(numRows, numCols)
    bombBoard = functions.bombPlacer(bombBoard)
    functions.boardPrinter(board)
    if SEE_BOMBBOARD:
        functions.boardPrinter(bombBoard)
    with open('savegame.txt', 'wb') as file:  #exports display board to file
        pickle.dump(board, file)
    with open('saveBombBoard.txt', 'wb') as file: #exports bombBoard to file
        pickle.dump(bombBoard, file)        
else:
    print("Welcome back!")
    functions.mainMenu()
    with open('savegame.txt', 'rb') as file: #imports display board from file
        board = pickle.load(file)
    with open('saveBombBoard.txt', 'rb') as file: #imports bombBoard from file
        bombBoard = pickle.load(file)
    numCols = len(bombBoard[0])
    numRows = len(bombBoard)
    functions.boardPrinter(board)  
    if SEE_BOMBBOARD:
        functions.boardPrinter(bombBoard)
while(True):
    if functions.isWinner(board) == False:
        colChoice = functions.xPrompt(numCols)
        rowChoice = functions.yPrompt(numRows)
        bombs = functions.numBombs(board, bombBoard, colChoice, rowChoice)
        functions.boardPrinter(board)
        menuChoice2 = functions.savePrompt()
        if (menuChoice2 == "s" or menuChoice2 == "S"):
            with open('savegame.txt', 'wb') as file: 
                pickle.dump(board, file)
            with open('saveBombBoard.txt', 'wb') as file:
                pickle.dump(bombBoard, file)
            sys.exit()
        elif (menuChoice2 == "q" or menuChoice2 == "Q"):                
            sys.exit()                    
    else:
        functions.boardPrinter(bombBoard)
        functions.boardPrinter(board)
        sys.exit()
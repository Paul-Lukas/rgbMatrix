from Plugins.Plugin import Plugin

#from tkinter import *
import math
from threading import Thread
import random
import time
class BootPlugin(Plugin):
    def __init__(self, app, matrix):
        super().__init__(app, matrix)


    #Run wird beim start ausgeführt und muss den Code enthalten, der im endeffekt ausgeführt werden soll
    def run(self):
        
        boardMode = False
        dummyTester = True
        heuselMode = True
        randomRotations = True
        # --------------- game Size
        game_width = 15
        game_height = 30

        pixelBoard_xLength = game_width + 2
        pixelBoard_yLength = game_height + 2
        pixelBoard = [[0 for i in range(pixelBoard_yLength)] for j in range(pixelBoard_xLength)]
        alreadyPainted = [[0 for i in range(pixelBoard_yLength)] for j in range(pixelBoard_xLength)]

        game_board_xLength = game_width + 2
        game_board_yLength = game_height + 2
        game_board_xPos = 0
        game_board_yPos = 0
        game_board = [[0 for i in range(game_board_yLength)] for j in range(game_board_xLength)]

        game_run = True
        game_speed = 1.0
        game_level = random.randint(1,6)
        game_lines = 0
        game_score = 0

        tetromino = [[0 for i in range(4)] for j in range(4)]
        tetromino_number = 0
        nextTetromino = [[0 for i in range(4)] for j in range(4)]
        nextTetromino_number = 0
        tetromino_startPos = int(game_board_xLength/2) - 2
        tetromino_xPos = 0
        tetromino_yPos = 0

        size = 2
        yDowner = 20
        leldassiehtcoolaus = 10


        """
        ---------------canvas Functions--------------------------------------------
        """


        def deleteTetromino():
            canvas.delete("tag1")


        def deleteFixedTetrominos():
            canvas.delete("tag2")


        def lG(index):
            returnEr = (0, 0, 0)
            if game_level == 1:
                returnEr = (255,               int(255/7*index),  0)
            if game_level == 2:
                returnEr = (255,               0,                 int(255/7*index))
            if game_level == 3:
                returnEr = (int(255/7*index),  255,               0)
            if game_level == 4:
                returnEr = (0,                 255,               int(255/7*index))
            if game_level == 5:
                returnEr = (int(255/7*index),  0,                 255)
            if game_level == 6:
                returnEr = (0,                 int(255/7*index),  255)
            return returnEr


        def getColor(x):
            """
            Creates Color Values for a specific Tetromino

            Parameters
            ----------
            x : int
                the Tetromino index

            Returns
            -------
            tuple
                r,g,b values

            """

            TetrominoColors = [0 for i in range(9)]

            # Numbers are mixed, to see better difference between equal looking tetrominos
            if heuselMode == False:
                TetrominoColors[1] = lG(7)
                TetrominoColors[2] = lG(1)
                TetrominoColors[3] = lG(3)
                TetrominoColors[4] = lG(5)
                TetrominoColors[5] = lG(2)
                TetrominoColors[6] = lG(4)
                TetrominoColors[7] = lG(6)
            else:
                TetrominoColors[1] = (14, 74, 191)
                TetrominoColors[2] = (179, 65, 161)
                TetrominoColors[3] = (64, 211, 229)
                TetrominoColors[4] = (221, 236, 89)
                TetrominoColors[5] = (232, 118, 43)
                TetrominoColors[6] = (220, 52, 40)
                TetrominoColors[7] = (69, 179, 88)

            return TetrominoColors[x]


        def paint():
            """
            (re-)paints the canvas of the falling tetromino
            """
            if BoardMode:
                self.matrix.set_matrix(pixelBoard)
                self.matrix.submit_all()
            else:
                global alreadyPainted
                deleteTetromino()
                for x in range(1, pixelBoard_xLength-1):
                    for y in range(1, pixelBoard_yLength-1):
                        if pixelBoard[x][y] > 0:
                            canvas.create_rectangle(size*(5+(x-1)*10), size*(5+(y-1)*10+yDowner), size*(5+9+(x-1)*10), size*(5+9+(y-1)*10+yDowner), fill = "#%02x%02x%02x" % (getColor(abs(pixelBoard[x][y]))[0],getColor(abs(pixelBoard[x][y]))[1],getColor(abs(pixelBoard[x][y]))[2]),tag = "tag1")


        def paintLanding():
            """
            paints a landed Tetromino.
            The list "already painted" will be updated. It stores where canvas
                of landed tetrominos are already painted.
            """
            if BoardMode:
                self.matrix.set_matrix(pixelBoard)
                self.matrix.submit_all()
            else:
                global alreadyPainted
                deleteTetromino()
                for x in range(1, pixelBoard_xLength-1):
                    for y in range(1, pixelBoard_yLength-1):
                        if pixelBoard[x][y] < 0 and pixelBoard[x][y] > -8:
                            if alreadyPainted[x][y] == 0:
                                canvas.create_rectangle(size*(5+(x-1)*10), size*(5+(y-1)*10+yDowner), size*(5+9+(x-1)*10), size*(5+9+(y-1)*10+yDowner), fill = "#%02x%02x%02x" % (getColor(abs(pixelBoard[x][y]))[0],getColor(abs(pixelBoard[x][y]))[1],getColor(abs(pixelBoard[x][y]))[2]),tag = "tag2")
                                alreadyPainted[x][y] =1


        def paintFullRow():
            """
            deletes all canvas of fallen tetrominos and repaints them.
            Function is triggered when a row (or multiple) is/are removed
            """
            if BoardMode:
                self.matrix.set_matrix(pixelBoard)
                self.matrix.submit_all()
            else:
                global alreadyPainted
                deleteFixedTetrominos()
                alreadyPainted = [[0 for i in range(pixelBoard_yLength)] for j in range(pixelBoard_xLength)]
                for x in range(1, pixelBoard_xLength-1):
                    for y in range(1, pixelBoard_yLength-1):
                        if pixelBoard[x][y] < 0 and pixelBoard[x][y] > -8:
                            canvas.create_rectangle(size*(5+(x-1)*10), size*(5+(y-1)*10+yDowner), size*(5+9+(x-1)*10), size*(5+9+(y-1)*10+yDowner), fill = "#%02x%02x%02x" % (getColor(abs(pixelBoard[x][y]))[0],getColor(abs(pixelBoard[x][y]))[1],getColor(abs(pixelBoard[x][y]))[2]),tag = "tag2")
                            alreadyPainted[x][y] = 1


        def get_tetromino(x):
            """
            Returns the Tetromino structure in the Array
            different array values for different tetromino colors.

            Parameters
            ----------
            x : int
                Tetromino index

            Returns
            -------
            4x4 Field
                The Tetromino structure
            x : int
                The Tetromino Number (probably needed somewhere, idk where)
            """
            Tetrominos = [[[0 for i in range(4)] for j in range(4)] for k in range(8)]

            # L
            Tetrominos[1][0][1] = 1
            Tetrominos[1][1][1] = 1
            Tetrominos[1][2][1] = 1
            Tetrominos[1][0][2] = 1

            # Lr
            Tetrominos[2][0][1] = 2
            Tetrominos[2][1][1] = 2
            Tetrominos[2][2][1] = 2
            Tetrominos[2][2][2] = 2

            # Z
            Tetrominos[3][0][1] = 3
            Tetrominos[3][1][1] = 3
            Tetrominos[3][1][2] = 3
            Tetrominos[3][2][2] = 3

            # Zr
            Tetrominos[4][0][2] = 4
            Tetrominos[4][1][2] = 4
            Tetrominos[4][1][1] = 4
            Tetrominos[4][2][1] = 4

            # Square
            Tetrominos[5][1][1] = 5
            Tetrominos[5][1][2] = 5
            Tetrominos[5][2][1] = 5
            Tetrominos[5][2][2] = 5

            # Bar
            Tetrominos[6][0][1] = 6
            Tetrominos[6][1][1] = 6
            Tetrominos[6][2][1] = 6
            Tetrominos[6][3][1] = 6

            # T
            Tetrominos[7][0][1] = 7
            Tetrominos[7][1][1] = 7
            Tetrominos[7][1][2] = 7
            Tetrominos[7][2][1] = 7

            return Tetrominos[x], x


        """
        ---------------print Functions (for debugging)-----------------------------
        """


        def print_pixelBoard():
            for y in range(1, pixelBoard_yLength - 1):
                for x in range(1, pixelBoard_xLength - 1):
                    if(pixelBoard[x][y] >= 0):
                        print(" " + str(pixelBoard[x][y]), end="")
                    else:
                        print(str(pixelBoard[x][y]), end="")
                print("")


        def print_pixelBoard_wBoarder():
            for y in range(pixelBoard_yLength):
                for x in range(pixelBoard_xLength):
                    if(pixelBoard[x][y] >= 0):
                        print(" " + str(pixelBoard[x][y]), end="")
                    else:
                        print(str(pixelBoard[x][y]), end="")
                print("")


        def print_array(xD: int, yD: int, inp: []):
            for y in range(yD):
                for x in range(xD):
                    if(inp[x][y] >= 0):
                        print(" " + str(inp[x][y]), end="")
                    else:
                        print(str(inp[x][y]), end="")
                print("")
            print("")


        def print_tetromino():
            for y in range(4):
                for x in range(4):
                    print(str(tetromino[x][y]) + " ", end="")
                print("")


        """
        ---------------pixelBoard/game_board Functions(gui)------------------------
        """


        def sync_pixelBoard():
            """
            syncs the game_board with the pixelBoard.
            The code is generated, to difference between this two Fields,
                to show additional information on the Board (like next Tetromino, etc)
            """
            for x in range(game_board_xLength):
                for y in range(game_board_yLength):
                    pixelBoard[game_board_xPos+x][game_board_yPos+y] = game_board[x][y]

        def game_refresh():
            sync_pixelBoard()
            paint()


        def game_setBorder():
            """
            Sets the Border of the game to (-8)
            """
            game_board = [[-8 for i in range(game_board_yLength)] for j in range(game_board_xLength)]
            for x in range(1, game_board_xLength - 1):
                for y in range(1, game_board_yLength - 1):
                    game_board[x][y] = 0


        """
        ---------------game / tetromino Functions----------------------------------
        """


        def tetromino_fix():
            """
            Marks the moving Tetromino as landed Tetromino (*-1)
            """
            for x in range(4):
                for y in range(4):
                    if x+tetromino_xPos < game_board_xLength and y+tetromino_yPos < game_board_yLength:
                        if game_board[x+tetromino_xPos][y+tetromino_yPos] > 0:
                            game_board[x+tetromino_xPos][y+tetromino_yPos] = game_board[x+tetromino_xPos][y+tetromino_yPos]*(-1)


        def tetromino_rewrite():
            """
            Deletes the Tetrino in the game_board and places it new 
                (at new coordinates)
            """
            for x in range(1, game_board_xLength - 1):
                for y in range(1, game_board_yLength - 1):
                    if game_board[x][y] > 0:
                        game_board[x][y] = 0
            for x in range(4):
                for y in range(4):
                    if(tetromino[x][y] > 0):
                        game_board[tetromino_xPos + x][tetromino_yPos + y] = tetromino[x][y]


        def game_place_nextTetromino():
            """
            After the landed tetromino, the next starts at the top.
                nextTetromino will be created
            """
            tetromino = nextTetromino
            tetromino_number = nextTetromino_number

            Temp = get_tetromino(random.randint(1, 7))
            nextTetromino = Temp[0]
            nextTetromino_number = Temp[1]

            tetromino_xPos = tetromino_startPos
            tetromino_yPos = 0
            if randomRotations:
                for x in range(random.randint(0, 3)):
                    tetromino = list(reversed(list(zip(*tetromino))))
            tetromino_rewrite()


        def game_start():
            """
            Creates tetromino and nextTetromino and places it at the top
            """
            game_setBorder()
            sync_pixelBoard()
            # paintStartScreen()

            Temp = get_tetromino(random.randint(1, 7))
            tetromino = Temp[0]
            if randomRotations:
                for x in range(random.randint(0, 3)):
                    tetromino = list(reversed(list(zip(*tetromino))))
            tetromino_number = Temp[1]

            Temp = get_tetromino(random.randint(1, 7))
            nextTetromino = Temp[0]
            nextTetromino_number = Temp[1]

            tetromino_xPos = tetromino_startPos
            tetromino_yPos = 0
            tetromino_rewrite()


        """
        ---------------event actions-----------------------------------------------
        """


        def game_pause(event):
            
            if game_run:
                game_run = False
            else:
                game_run = True


        def game_restart(event):
            
            pixelBoard = [[0 for i in range(pixelBoard_yLength)] for j in range(pixelBoard_xLength)]
            alreadyPainted = [[0 for i in range(pixelBoard_yLength)] for j in range(pixelBoard_xLength)]
            game_board = [[0 for i in range(game_board_yLength)] for j in range(game_board_xLength)]
            game_setBorder()
            game_run = True
            sync_pixelBoard()
            deleteTetromino()
            deleteFixedTetrominos()
            game_level = random.randint(1,6)
            game_lines = 0
            game_speed = 1.0
            var.set("Lines: "+str(game_lines))
            var2.set("ColorType: " + str(game_level))
            tkFenster.update_idletasks()
            restart.place_forget()
            
            game_start()
            game_refresh()


        def game_over():
            
            game_run = False
            var2.set("Game Over")
            tkFenster.update_idletasks()
            restart.place(x=80, y=yDowner+340-20, width=160, height=size*20)


        def game_delete_fullRows():
            """
            Deletes all full Lines and drops the lines above

            Returns
            -------
            counter : int
                Number of deleted Lines

            """
            counter = 0
            for y in range(1, game_board_yLength - 1):
                full = True
                for x in range(1, game_board_xLength - 1):
                    if game_board[x][y] == 0:
                        full = False
                if full:
                    counter = counter + 1
                    for yN in range(y, 2, -1):
                        for xN in range(1, game_board_xLength - 1):
                            game_board[xN][yN] = game_board[xN][yN-1]

            return counter


        def landing():
            """
            Actions performed if the tetromino lands (and the Line full is)
            """
            if tetromino_yPos >= 4:
                randomCheckVar = True
            else:
                randomCheckVar = False
            tetromino_fix()
            sync_pixelBoard()
            paintLanding()
            rowsDeletedThisLanding = game_delete_fullRows()
            if rowsDeletedThisLanding > 0:
                sync_pixelBoard()
                paintFullRow()
                game_lines = game_lines + rowsDeletedThisLanding
                if(game_level == 6):
                    game_level = 1
                else:
                    game_level = game_level + 1
                game_speed = 1 / math.pow(game_lines + 1, 0.5)
                var.set("Lines: "+str(game_lines))
                var2.set("ColorType: " + str(game_level))
                tkFenster.update_idletasks()
            if rowsDeletedThisLanding == 4:
                # landinganimation
                if False:
                    print("WOW")

            if randomCheckVar:
                game_place_nextTetromino()
            else:
                game_over()


        """
        ---------------check move / rotation Functions-----------------------------
        """


        def check_cwRotation():
            check = True
            test = list(reversed(list(zip(*tetromino))))
            for x in range(4):
                for y in range(4):
                    if test[x][y] > 0:
                        if game_board[tetromino_xPos + x][tetromino_yPos + y] < 0:
                            check = False
            return check


        def check_ccwRotation():
            check = True
            test = list(zip(*tetromino[::-1]))
            for x in range(4):
                for y in range(4):
                    if test[x][y] > 0:
                        if game_board[tetromino_xPos + x][tetromino_yPos + y] < 0:
                            check = False
            return check


        def check_dMove():
            check = True
            for x in range(4):
                for y in range(4):
                    if(tetromino[x][y] > 0):
                        if(game_board[tetromino_xPos + x][tetromino_yPos + y + 1] < 0):
                            check = False
            return check


        def check_rMove():
            check = True
            for x in range(4):
                for y in range(4):
                    if(tetromino[x][y] > 0):
                        if(game_board[tetromino_xPos + x + 1][tetromino_yPos + y] < 0):
                            check = False
            return check


        def check_lMove():
            check = True
            for x in range(4):
                for y in range(4):
                    if(tetromino[x][y] > 0):
                        if(game_board[tetromino_xPos + x - 1][tetromino_yPos + y] < 0):
                            check = False
            return check


        """
        ---------------move / rotation Functions-----------------------------------
        """


        def rMove(event):
            if game_run:
                if check_rMove():
                    tetromino_xPos = tetromino_xPos + 1
                    tetromino_rewrite()
                    game_refresh()


        def lMove(event):
            if game_run:
                if check_lMove():
                    tetromino_xPos = tetromino_xPos - 1
                    tetromino_rewrite()
                    game_refresh()


        def dMove(event):
            if game_run:
                if check_dMove():
                    tetromino_yPos = tetromino_yPos + 1
                else:
                    landing()
                tetromino_rewrite()
                game_refresh()


        def cwRotation(event):
            if game_run:
                if check_cwRotation():
                    tetromino = list(reversed(list(zip(*tetromino))))
                    tetromino_rewrite()
                    game_refresh()


        def ccwRotation(event):
            if game_run:
                if check_ccwRotation():
                    tetromino = list(zip(*tetromino[::-1]))
                    tetromino_rewrite()
                    game_refresh()


        def randommove():
            randomVar = random.randint(1, 5)
            if(randomVar == 1):
                rMove("blub")
            if(randomVar == 2):
                lMove("blub")
            if(randomVar == 3):
                dMove("blub")
            if(randomVar == 4):
                cwRotation("blub")
            if(randomVar == 5):
                ccwRotation("blub")


        """
        ---------------gameloop Functions------------------------------------------
        """


        def dummy():
            while game_run:
                randomVar = random.randint(1, 5)
                if(randomVar == 1):
                    rMove("blub")
                if(randomVar == 2):
                    lMove("blub")
                if(randomVar == 3):
                    dMove("blub")
                if(randomVar == 4):
                    cwRotation("blub")
                if(randomVar == 5):
                    ccwRotation("blub")
                    
                time.sleep(random.randint(1, 20)/10)


        def mainLoop():
            while True:
                if game_run:
                    if check_dMove():
                        tetromino_yPos = tetromino_yPos + 1
                    else:
                        landing()
                    tetromino_rewrite()
                    game_refresh()
                    time.sleep(game_speed)


        """
        ---------------tkinter-----------------------------------------------------
        """

        if boardMode == False:
            tkFenster = Tk()
            tkFenster.title('PixelBoard')

            tkFenster.geometry('320x680')

            canvas = Canvas(master=tkFenster, bg='White')
            canvas.place(x=0, y=0+yDowner, width=size*160, height=size*(310+yDowner))

            tkFenster.bind('<Right>', cwRotation)
            tkFenster.bind('<Left>', ccwRotation)
            tkFenster.bind('<a>', lMove)
            tkFenster.bind('<s>', dMove)
            tkFenster.bind('<d>', rMove)
            tkFenster.bind('<Escape>', game_pause)

            var = StringVar()
            var.set("Lines: " + str(0))
            var2 = StringVar()
            var2.set("ColorType: " + str(game_level))

            LinesDisplay = Label(tkFenster, textvariable=var)
            LinesDisplay.place(x=0, y=0, width=160, height=yDowner)
            LinesDisplay = Label(tkFenster, textvariable=var2)
            LinesDisplay.place(x=160, y=0, width=160, height=yDowner)

            restart = Button(master=tkFenster, text='Restart Game') # , command=game_restart
            restart.bind('<Button-1>', game_restart)


        """
        ---------------game start--------------------------------------------------
        """


        game_start()
        game_refresh()


        t1 = Thread(target=mainLoop)
        t2 = Thread(target=dummy)

        t1.start()

        if dummyTester == True:
            t2.start()
            
        if boardMode == False:
            tkFenster.mainloop()



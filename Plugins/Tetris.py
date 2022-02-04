from Plugins.Plugin import Plugin
#from tkinter import *
import math
import random
import time

class BootPlugin(Plugin):
    
    """
    ---------------variables---------------------------------------------------
    """

    boardMode = True
    dummyTester = True
    heuselMode = False
    randomRotations = True
    
    bgColor = (1,1,1)
    prev = [[(0,0,0)  for i in range(30)] for j in range(15)]
    
    #game_width = 15
    #game_height = 30
    
    xDim = 15
    yDim = 30
    
    #pixelBoard_xLength = game_width + 2
    #pixelBoard_yLength = game_height + 2
    
    pixelBoard = [[0 for i in range(30)] for j in range(15)]
    alreadyPainted = [[0 for i in range(30)] for j in range(15)]
    
    #game_board_xLength = game_width + 2
    #game_board_yLength = game_height + 2
    #game_board_xPos = 0
    #game_board_yPos = 0
    #game_board = [[0 for i in range(30+2)] for j in range(15+2)]
    game_run = True
    game_speed = 0.2
    game_level = random.randint(1,6)
    game_lines = 0
    game_score = 0
    
    tetromino = [[0 for i in range(4)] for j in range(4)]
    tetromino_number = 0
    nextTetromino = [[0 for i in range(4)] for j in range(4)]
    nextTetromino_number = 0
    tetromino_startPos = int(xDim/2) - 2
    tetromino_xPos = 0
    tetromino_yPos = 0
    
    size = 2
    yDowner = 20
    leldassiehtcoolaus = 10
    
    
    def __init__(self, app, matrix):
        super().__init__(app, matrix)
    
    
    def deleteTetromino(self):
        self.canvas.delete("tag1")
    
    
    def deleteFixedTetrominos(self):
        self.canvas.delete("tag2")
    
    """
    ---------------print Functions (for debugging)-----------------------------
    """
    
    
    def print_pixelBoard(self):
        for y in range(self.yDim):
            for x in range(self.xDim):
                if(self.pixelBoard[x][y] >= 0):
                    print(" " + str(self.pixelBoard[x][y]), end="")
                else:
                    print(str(self.pixelBoard[x][y]), end="")
            print("")
    
    
    def print_pixelBoard_wBoarder(self):
        for y in range(self.pixelBoard_yLength):
            for x in range(self.pixelBoard_xLength):
                if(pixelBoard[x][y] >= 0):
                    print(" " + str(pixelBoard[x][y]), end="")
                else:
                    print(str(pixelBoard[x][y]), end="")
            print("")
    
    
    def print_array(self,xD: int, yD: int, inp: []):
        for y in range(yD):
            for x in range(xD):
                print(" " + str(inp[x][y]), end="")
                
            print("")
        print("")
    
    
    def print_tetromino(self):
        for y in range(4):
            for x in range(4):
                print(str(tetromino[x][y]) + " ", end="")
            print("")
    
    
    
    
    def lG(self,index):
        returnEr = self.bgColor
        if self.game_level == 1:
            returnEr = (255,               int(255/7*index),  0)
        if self.game_level == 2:
            returnEr = (255,               0,                 int(255/7*index))
        if self.game_level == 3:
            returnEr = (int(255/7*index),  255,               0)
        if self.game_level == 4:
            returnEr = (0,                 255,               int(255/7*index))
        if self.game_level == 5:
            returnEr = (int(255/7*index),  0,                 255)
        if self.game_level == 6:
            returnEr = (0,                 int(255/7*index),  255)
        return returnEr
    
    
    def getColor(self,x):
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
    
        TetrominoColors = [self.bgColor for i in range(9)]
    
        # Numbers are mixed, to see better difference between equal looking tetrominos
        if self.heuselMode == False:
            TetrominoColors[1] = self.lG(7)
            TetrominoColors[2] = self.lG(1)
            TetrominoColors[3] = self.lG(3)
            TetrominoColors[4] = self.lG(5)
            TetrominoColors[5] = self.lG(2)
            TetrominoColors[6] =self. lG(4)
            TetrominoColors[7] = self.lG(6)
        else:
            TetrominoColors[1] = (14, 74, 191)
            TetrominoColors[2] = (179, 65, 161)
            TetrominoColors[3] = (64, 211, 229)
            TetrominoColors[4] = (221, 236, 89)
            TetrominoColors[5] = (232, 118, 43)
            TetrominoColors[6] = (220, 52, 40)
            TetrominoColors[7] = (69, 179, 88)
    
        return TetrominoColors[x]
    
    
    def paint(self):
        """
        (re-)paints the canvas of the falling tetromino
        """
        
        new = [[(0,0,0)  for i in range(30)] for j in range(15)]
        for x in range(self.xDim):
            for y in range(self.yDim):
                col = self.getColor(abs(self.pixelBoard[x][y]))
                new[x][y] =  col
        if(new != self.prev):
            self.prev = new
            self.matrix.set_matrix(new)
            if (self.boardMode == False):
                self.matrix.delete_canvas()
            self.matrix.submit_all()

    
    def paintLanding(self):
        self.paint()
        """
        paints a landed Tetromino.
        The list "already painted" will be updated. It stores where canvas
            of landed tetrominos are already painted.
        
        global alreadyPainted
        self.deleteTetromino()
        for x in range(1, self.pixelBoard_xLength-1):
            for y in range(1, self.pixelBoard_yLength-1):
                if pixelBoard[x][y] < 0 and pixelBoard[x][y] > -8:
                    if alreadyPainted[x][y] == 0:
                        self.canvas.create_rectangle(self.size*(5+(x-1)*10), self.size*(5+(y-1)*10+self.yDowner), self.size*(5+9+(x-1)*10), self.size*(5+9+(y-1)*10+self.yDowner), fill = "#%02x%02x%02x" % (self.getColor(abs(self.pixelBoard[x][y]))[0],self.getColor(abs(self.pixelBoard[x][y]))[1],self.getColor(abs(self.pixelBoard[x][y]))[2]),tag = "tag2")
                        alreadyPainted[x][y] = 1
        """
    
    def paintFullRow(self):
        self.paint()
        """
        deletes all canvas of fallen tetrominos and repaints them.
        Function is triggered when a row (or multiple) is/are removed
        
        global alreadyPainted
        self.deleteFixedTetrominos()
        alreadyPainted = [[0 for i in range(self.pixelBoard_yLength)] for j in range(self.pixelBoard_xLength)]
        for x in range(1, self.pixelBoard_xLength-1):
            for y in range(1, self.pixelBoard_yLength-1):
                if pixelBoard[x][y] < 0 and pixelBoard[x][y] > -8:
                    self.canvas.create_rectangle(self.size*(5+(x-1)*10), self.size*(5+(y-1)*10+self.yDowner), self.size*(5+9+(x-1)*10), self.size*(5+9+(y-1)*10+self.yDowner), fill = "#%02x%02x%02x" % (self.getColor(abs(pixelBoard[x][y]))[0],self.getColor(abs(pixelBoard[x][y]))[1],self.getColor(abs(pixelBoard[x][y]))[2]),tag = "tag2")
                    alreadyPainted[x][y] = 1
        """
    
    def get_tetromino(self,x):
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
    ---------------pixelBoard/game_board Functions(gui)------------------------
    """
    
    
    def game_refresh(self):
        self.paint()
    
    """
    def game_setBorder(self):
        
        Sets the Border of the game to (-8)
        
        global game_board
        game_board = [[-8 for i in range(self.yDim)] for j in range(self.xDim)]
        for x in range(1, self.xDim - 1):
            for y in range(1, self.yDim - 1):
                self.pixelBoard[x][y] = 0
    """
    
    """
    ---------------game / tetromino Functions----------------------------------
    """
    
    
    def tetromino_fix(self):
        """
        Marks the moving Tetromino as landed Tetromino (*-1)
        """
        for x in range(4):
            for y in range(4):
                if x+self.tetromino_xPos < self.xDim and y+self.tetromino_yPos < self.yDim:
                    if self.pixelBoard[x+self.tetromino_xPos][y+self.tetromino_yPos] > 0:
                        self.pixelBoard[x+self.tetromino_xPos][y+self.tetromino_yPos] = self.pixelBoard[x+self.tetromino_xPos][y+self.tetromino_yPos]*(-1)
    
    
    def tetromino_rewrite(self):
        """
        Deletes the Tetrino in the game_board and places it new 
            (at new coordinates)
        """
        for x in range(self.xDim ):
            for y in range(self.yDim):
                if self.pixelBoard[x][y] > 0:
                    self.pixelBoard[x][y] = 0
        for x in range(4):
            for y in range(4):
                if(self.tetromino[x][y] > 0):
                    self.pixelBoard[self.tetromino_xPos + x][self.tetromino_yPos + y] = self.tetromino[x][y]
    
    
    def game_place_nextTetromino(self):
        """
        After the landed tetromino, the next starts at the top.
            nextTetromino will be created
        """
        global tetromino_xPos, tetromino_yPos
        global tetromino, nextTetromino
        global tetromino_number, nextTetromino_number
    
        self.tetromino = self.nextTetromino
        self.tetromino_number = self.nextTetromino_number
    
        Temp = self.get_tetromino(random.randint(1, 7))
        self.nextTetromino = Temp[0]
        self.nextTetromino_number = Temp[1]
    
        self.tetromino_xPos = self.tetromino_startPos
        self.tetromino_yPos = 0
        if self.randomRotations:
            for x in range(random.randint(0, 3)):
                self.tetromino = list(reversed(list(zip(*self.tetromino))))
        self.tetromino_rewrite()
    
    
    def game_start(self):
        """
        Creates tetromino and nextTetromino and places it at the top
        """
        #self.game_setBorder()
        # paintStartScreen()
    
        global tetromino, nextTetromino
        global tetromino_number, nextTetromino_number
        global tetromino_xPos, tetromino_yPos
    
        Temp = self.get_tetromino(random.randint(1, 7))
        self.tetromino = Temp[0]
        if self.randomRotations:
            for x in range(random.randint(0, 3)):
                self.tetromino = list(reversed(list(zip(*self.tetromino))))
        self.tetromino_number = Temp[1]
    
        Temp = self.get_tetromino(random.randint(1, 7))
        self.nextTetromino = Temp[0]
        self.nextTetromino_number = Temp[1]
    
        self.tetromino_xPos = self.tetromino_startPos
        self.tetromino_yPos = 0
        self.tetromino_rewrite()
        #self.sync_pixelBoard()
        #self.print_pixelBoard()
    
    
    """
    ---------------event actions-----------------------------------------------
    """
    
    
    def game_pause(self, event):
        global game_run
        if game_run:
            self.game_run = False
        else:
            self.game_run = True
    
    
    def game_restart(self,event):
        global game_run, game_level, game_lines, game_speed, pixelBoard, alreadyPainted
        self.alreadyPainted = [[0 for i in range(self.pixelBoard_yLength)] for j in range(self.pixelBoard_xLength)]
        self.game_board = [[0 for i in range(self.game_board_yLength)] for j in range(self.game_board_xLength)]
        self.game_setBorder()
        self.game_run = True
        self.sync_pixelBoard()
        self.deleteTetromino()
        self.deleteFixedTetrominos()
        self.game_level = random.randint(1,6)
        self.game_lines = 0
        self.game_speed = 1.0
        self.var.set("Lines: "+str(game_lines))
        self.var2.set("ColorType: " + str(game_level))
        self.tkFenster.update_idletasks()
        self.restart.place_forget()
        
        self.game_start()
        self.game_refresh()
    
    
    def game_over(self):
        global game_run
        self.game_run = False
        self.var2.set("Game Over")
        self.tkFenster.update_idletasks()
        self.restart.place(x=80, y=self.yDowner+340-20, width=160, height=self.size*20)
    
    
    def game_delete_fullRows(self):
        """
        Deletes all full Lines and drops the lines above
    
        Returns
        -------
        counter : int
            Number of deleted Lines
    
        """
        counter = 0
        for y in range(self.yDim):
            full = True
            for x in range(self.xDim):
                if self.pixelBoard[x][y] == 0:
                    full = False
            if full:
                counter = counter + 1
                for yN in range(y, 2, -1):
                    for xN in range(self.xDim):
                        self.game_board[xN][yN] = self.game_board[xN][yN-1]
    
        return counter
    
    
    def landing(self):
        """
        Actions performed if the tetromino lands (and the Line full is)
        """
        global game_lines, game_speed, game_level
        if self.tetromino_yPos >= 4:
            randomCheckVar = True
        else:
            randomCheckVar = False
        self.tetromino_fix()
        self.paintLanding()
        rowsDeletedThisLanding = self.game_delete_fullRows()
        if rowsDeletedThisLanding > 0:
            self.sync_pixelBoard()
            self.paintFullRow()
            self.game_lines = game_lines + rowsDeletedThisLanding
            if(self.game_level == 6):
                self.game_level = 1
            else:
                self.game_level = game_level + 1
            self.game_speed = 1 / math.pow(game_lines + 1, 0.5)
            self.var.set("Lines: "+str(game_lines))
            self.var2.set("ColorType: " + str(game_level))
            self.tkFenster.update_idletasks()
        if rowsDeletedThisLanding == 4:
            # landinganimation
            if False:
                print("WOW")
    
        if randomCheckVar:
            self.game_place_nextTetromino()
        else:
            self.game_over()
    
    
    """
    ---------------check move / rotation Functions-----------------------------
    """
    
    
    def check_cwRotation(self):
        check = True
        test = list(reversed(list(zip(*self.tetromino))))
        for x in range(4):
            for y in range(4):
                if test[x][y] > 0:
                    if self.pixelBoard[self.tetromino_xPos + x][self.tetromino_yPos + y] < 0:
                        check = False
        return check
    
    
    def check_ccwRotation(self):
        check = True
        test = list(zip(*self.tetromino[::-1]))
        for x in range(4):
            for y in range(4):
                if test[x][y] > 0:
                    if self.pixelBoard[self.tetromino_xPos + x][self.tetromino_yPos + y] < 0:
                        check = False
        return check
    
    
    def giveLowestTetrominoPoint(self):
        lowest = 0
        for y in range(4):
            for x in range(4):
                if self.tetromino[x][y] > 0:
                    if y > lowest:
                        lowest = y
        return lowest
    
    
    def check_dMove(self):
        check = True
        if(self.tetromino_yPos >= 30-(self.giveLowestTetrominoPoint()+1)):
            return False
        for x in range(4):
            for y in range(4):
                if(self.tetromino[x][y] > 0):
                    if(self.pixelBoard[self.tetromino_xPos + x][self.tetromino_yPos + y+1] < 0):
                        return False
        return check
    
    
    def check_rMove(self):
        check = True
        for x in range(4):
            for y in range(4):
                if(self.tetromino[x][y] > 0):
                    if(self.pixelBoard[self.tetromino_xPos + x+1][self.tetromino_yPos + y] < 0):
                        check = False
        return check
    
    
    def check_lMove(self):
        check = True
        for x in range(4):
            for y in range(4):
                if(self.tetromino[x][y] > 0):
                    if(self.pixelBoard[self.tetromino_xPos + x-1][self.tetromino_yPos + y] < 0):
                        check = False
        return check
    
    
    """
    ---------------move / rotation Functions-----------------------------------
    """
    
    
    def rMove(self,event):
        global tetromino_xPos
        if self.game_run:
            if self.check_rMove():
                self.tetromino_xPos = self.tetromino_xPos + 1
                self.tetromino_rewrite()
                self.game_refresh()
    
    
    def lMove(self,event):
        global tetromino_xPos
        if self.game_run:
            if self.check_lMove():
                self.tetromino_xPos = self.tetromino_xPos - 1
                self.tetromino_rewrite()
                self.game_refresh()
    
    
    def dMove(self,event):
        global tetromino_yPos
        if self.game_run:
            if self.check_dMove():
                self.tetromino_yPos = self.tetromino_yPos + 1
            else:
                self.landing()
            self.tetromino_rewrite()
            self.game_refresh()
    
    
    def cwRotation(self,event):
        global tetromino
        if self.game_run:
            if self.check_cwRotation():
                self.tetromino = list(reversed(list(zip(*self.tetromino))))
                self.tetromino_rewrite()
                self.game_refresh()
    
    
    def ccwRotation(self,event):
        global tetromino
        if self.game_run:
            if self.check_ccwRotation():
                self.tetromino = list(zip(*self.tetromino[::-1]))
                self.tetromino_rewrite()
                self.game_refresh()
    
    
    def randommove(self):
        randomVar = random.randint(1, 5)
        if(randomVar == 1):
            self.rMove("blub")
        if(randomVar == 2):
            self.lMove("blub")
        if(randomVar == 3):
            self.dMove("blub")
        if(randomVar == 4):
            self.cwRotation("blub")
        if(randomVar == 5):
            self.ccwRotation("blub")
    
    
    """
    ---------------gameloop Functions------------------------------------------
    """
    
    
    def mainLoopwDummy(self):
        while True:
            if self.game_run:
                randomVar = random.randint(1, 5)
                if(randomVar == 1):
                    self.rMove("blub")
                if(randomVar == 2):
                    self.lMove("blub")
                if(randomVar == 3):
                    self.dMove("blub")
                if(randomVar == 4):
                    self.cwRotation("blub")
                if(randomVar == 5):
                    self.ccwRotation("blub")
                        
                if self.check_dMove():
                    self.tetromino_yPos = self.tetromino_yPos + 1
                else:
                    self.landing()
                self.tetromino_rewrite()
                self.game_refresh()
                time.sleep(self.game_speed)
    
    
    def mainLoop(self):
        global tetromino_yPos
        while True:
            if self.game_run:
                if self.check_dMove():
                    self.tetromino_yPos = self.tetromino_yPos + 1
                else:
                    self.landing()
                self.tetromino_rewrite()
                self.game_refresh()
                time.sleep(game_speed)
    
    
    
    
    def run(self):
        
        self.matrix.set_matrix(self.prev)
        self.matrix.submit_all()
        
        self.game_start()
        self.game_refresh()
        
        self.mainLoopwDummy()

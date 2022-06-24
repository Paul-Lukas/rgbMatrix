# Created on Sat Feb 5 23:12 2022
# @author: Jan
    
from Plugins.Plugin import Plugin
import math
import random
import time

class BootPlugin(Plugin):
    
#--------------------------
    bgMode = True
    defaultBg = (1,1,1)
    epilepsipepsiMode = False
    
    boardMode = True
    
    dummyMode = True
    randomRotations = True
#--------------------------

    game_speed = 0.2
    
    game_width = 15
    game_height = 30
    
    prev = [[(1,0,0)  for i in range(30)] for j in range(15)]
    
    pixelBoard_xLength = game_width + 2
    pixelBoard_yLength = game_height + 2
    pixelBoard = [[0 for i in range(30+2)] for j in range(15+2)]
    alreadyPainted = [[0 for i in range(30+2)] for j in range(15+2)]
    
    game_board_xLength = game_width + 2
    game_board_yLength = game_height + 2
    game_board_xPos = 0
    game_board_yPos = 0
    game_board = [[0 for i in range(30+2)] for j in range(15+2)]
    
    game_run = True
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
    
    
    def c(self,index,num,g):
        returnEr = (0, 0, 0)
        if g == 1:
            returnEr = (255,               int(255/num*index),  0)
        if g == 2:
            returnEr = (255,               0,                 int(255/num*index))
        if g == 3:
            returnEr = (int(255/num*index),  255,               0)
        if g == 4:
            returnEr = (0,                 255,               int(255/num*index))
        if g == 5:
            returnEr = (int(255/num*index),  0,                 255)
        if g == 6:
            returnEr = (0,                 int(255/num*index),  255)
        return returnEr
    
    
    def getColor(self,x):
        """
        Creates Color Values for a specific Tetromino
        """
    
        TetrominoColors = [0 for i in range(9)]
        
        g = self.game_level
        
        # Numbers are mixed, to see better difference between equal looking tetrominos
        TetrominoColors[1] = self.c(7,7,g)
        TetrominoColors[2] = self.c(1,7,g)
        TetrominoColors[3] = self.c(3,7,g)
        TetrominoColors[4] = self.c(5,7,g)
        TetrominoColors[5] = self.c(2,7,g)
        TetrominoColors[6] = self.c(4,7,g)
        TetrominoColors[7] = self.c(6,7,g)
        
        """
        TetrominoColors[1] = (14, 74, 191)
        TetrominoColors[2] = (179, 65, 161)
        TetrominoColors[3] = (64, 211, 229)
        TetrominoColors[4] = (221, 236, 89)
        TetrominoColors[5] = (232, 118, 43)
        TetrominoColors[6] = (220, 52, 40)
        TetrominoColors[7] = (69, 179, 88)
        """
        
        return TetrominoColors[x]
    
    def reduceAlpha(self,tup, red):
        return (int(tup[0]*red),int(tup[1]*red),int(tup[2]*red))
        
    def paintBg(self):
        if self.epilepsipepsiMode:
            b = random.randint(1,4)
            a = self.game_level + b
            if(a > 6):
                a = a-6
        else:
            a = self.game_level + 1
            if(a > 6):
                a = 1
        
        new = [[(0,0,0)  for i in range(30)] for j in range(15)]
        for y in range(30):
            for x in range(15):
                new[x][y] = self.reduceAlpha(self.c(y,30,a),0.5)
        
        return new
        
        
    def paint(self):
        #print("paint!")
        if self.bgMode:
            new = self.paintBg()
        else:
            new = [[(self.defaultBg)  for i in range(30)] for j in range(15)]
            
        for x in range(1, self.pixelBoard_xLength-1):
            for y in range(1, self.pixelBoard_yLength-1):
                if self.pixelBoard[x][y] != 0:
                    col = self.getColor(abs(self.pixelBoard[x][y]))
                    try:
                        new[x-1][y-1] =  col
                    except:
                        print(x,y)
                        return False
        if(new != self.prev):
            self.prev = new
            self.matrix.set_matrix(new)
            if (self.boardMode == False):
                self.matrix.delete_canvas()
            self.matrix.submit_all()
    
    def paintLanding(self):
        self.paint()
    
    
    def paintFullRow(self):
        self.paint()
    
    
    def get_tetromino(self,x):
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
    

    def sync_pixelBoard(self):
        """
        syncs the game_board with the pixelBoard.
        The code is generated, to difference between this two Fields,
            to show additional information on the Board (like next Tetromino, etc)
        """
        for x in range(self.game_board_xLength):
            for y in range(self.game_board_yLength):
                self.pixelBoard[self.game_board_xPos+x][self.game_board_yPos+y] = self.game_board[x][y]
    
    
    def game_refresh(self):
        self.sync_pixelBoard()
        self.paint()
    
    
    def game_setBorder(self):
        """
        Sets the Border of the game to (-8)
        """
        global game_board
        self.game_board = [[-8 for i in range(self.game_board_yLength)] for j in range(self.game_board_xLength)]
        for x in range(1, self.game_board_xLength - 1):
            for y in range(1, self.game_board_yLength - 1):
                self.game_board[x][y] = 0
    
    
    """
    ---------------game / tetromino Functions----------------------------------
    """
    
    
    def tetromino_fix(self):
        """
        Marks the moving Tetromino as landed Tetromino (*-1)
        """
        for x in range(4):
            for y in range(4):
                if x+self.tetromino_xPos < self.game_board_xLength and y+self.tetromino_yPos < self.game_board_yLength:
                    if self.game_board[x+self.tetromino_xPos][y+self.tetromino_yPos] > 0:
                        self.game_board[x+self.tetromino_xPos][y+self.tetromino_yPos] = self.game_board[x+self.tetromino_xPos][y+self.tetromino_yPos]*(-1)
    
    
    def tetromino_rewrite(self):
        """
        Deletes the Tetrino in the game_board and places it new 
            (at new coordinates)
        """
        for x in range(1, self.game_board_xLength - 1):
            for y in range(1, self.game_board_yLength - 1):
                if self.game_board[x][y] > 0:
                    self.game_board[x][y] = 0
        for x in range(4):
            for y in range(4):
                if(self.tetromino[x][y] > 0):
                    self.game_board[self.tetromino_xPos + x][self.tetromino_yPos + y] = self.tetromino[x][y]
    
    
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
        self.game_setBorder()
        self.sync_pixelBoard()
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
    
    
    """
    ---------------event actions-----------------------------------------------
    """
    
    
    def game_pause(self,event):
        global game_run
        if self.game_run:
            self.game_run = False
        else:
            self.game_run = True
    
    
    def game_restart(self,event):
        global game_run, game_level, game_lines, game_speed, pixelBoard, alreadyPainted, game_board
        self.pixelBoard = [[0 for i in range(self.pixelBoard_yLength)] for j in range(self.pixelBoard_xLength)]
        self.alreadyPainted = [[0 for i in range(self.pixelBoard_yLength)] for j in range(self.pixelBoard_xLength)]
        self.game_board = [[0 for i in range(self.game_board_yLength)] for j in range(self.game_board_xLength)]
        self.game_setBorder()
        self.game_run = True
        self.sync_pixelBoard()
        self.game_level = random.randint(1,6)
        self.game_lines = 0
        self.game_speed = 1.0
        
        self.game_start()
        self.game_refresh()
    
    
    def game_over(self):
        global game_run
        self.game_run = False
    """
    !!! Score Anzeige!
    """
    
    
    def game_delete_fullRows(self):
        """
        Deletes all full Lines and drops the lines above
    
        Returns
        -------
        counter : int
            Number of deleted Lines
    
        """
        counter = 0
        for y in range(1, self.game_board_yLength - 1):
            full = True
            for x in range(1, self.game_board_xLength - 1):
                if self.game_board[x][y] == 0:
                    full = False
            if full:
                counter = counter + 1
                for yN in range(y, 2, -1):
                    for xN in range(1, self.game_board_xLength - 1):
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
        self.sync_pixelBoard()
        self.paintLanding()
        rowsDeletedThisLanding = self.game_delete_fullRows()
        if rowsDeletedThisLanding > 0:
            self.sync_pixelBoard()
            self.paintFullRow()
            self.game_lines = self.game_lines + rowsDeletedThisLanding
            if(self.game_level == 6):
                self.game_level = 1
            else:
                self.game_level = self.game_level + 1
            self.game_speed = 1 / math.pow(self.game_lines + 1, 0.5)
        if rowsDeletedThisLanding == 4:
            """
            !!! Landing-Animation
            """
    
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
                    if self.game_board[self.tetromino_xPos + x][self.tetromino_yPos + y] < 0:
                        check = False
        return check
    
    
    def check_ccwRotation(self):
        check = True
        test = list(zip(*self.tetromino[::-1]))
        for x in range(4):
            for y in range(4):
                if test[x][y] > 0:
                    if self.game_board[self.tetromino_xPos + x][self.tetromino_yPos + y] < 0:
                        check = False
        return check
    
    
    def check_dMove(self):
        check = True
        for x in range(4):
            for y in range(4):
                if(self.tetromino[x][y] > 0):
                    if(self.game_board[self.tetromino_xPos + x][self.tetromino_yPos + y + 1] < 0):
                        check = False
        return check
    
    
    def check_rMove(self):
        check = True
        for x in range(4):
            for y in range(4):
                if(self.tetromino[x][y] > 0):
                    if(self.game_board[self.tetromino_xPos + x + 1][self.tetromino_yPos + y] < 0):
                        check = False
        return check
    
    
    def check_lMove(self):
        check = True
        for x in range(4):
            for y in range(4):
                if(self.tetromino[x][y] > 0):
                    if(self.game_board[self.tetromino_xPos + x - 1][self.tetromino_yPos + y] < 0):
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
    
    def mainLoop(self):
        global tetromino_yPos
        while True:
            if self.game_run:
                self.dMove("blub")
                if self.dummyMode:
                    time.sleep(self.game_speed/2)
                    self.randommove()
                    time.sleep(self.game_speed/2)
                else:
                    time.sleep(self.game_speed)
    
    
    """
    ---------------game start--------------------------------------------------
    """
    
    
    def run(self):
        self.matrix.set_matrix(self.prev)
        self.matrix.submit_all()
        
        self.game_start()
        self.game_refresh()
        
        self.mainLoop()


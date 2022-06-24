from ..basePlugin import BasePlugin
import time
import random

class FlappyBird(BasePlugin):
    width = 15
    height = 30
    cX = -2
    cY = 0
    cLevel = 0
    gameover = 0
    score = 0


    def __init__(self, app, output):
        super().__init__(app, output)
        #self.pluginName = "Flappy-Bird"
        self.version = "pre 0.1"


    def run(self):
        game = [[0 for j in range(self.height)] for i in range(self.width)]
        for i in range(self.width):
            for j in range(self.height):
                game[i][j] = 0
        self.initPlayer()
        self.clock()

    def pipes(self, x, y, level):
        if (y < 0) | (y > self.height - 1):
            print("! y out of bounds")
            return

        distance = int(self.getspacing(level) / 2)
        yUp = y - distance
        yDown = y + distance

        current = 0
        while current <= self.height - 1:
            if (current < yUp) | (current > yDown):
                try:
                    if x > -1:
                        self.game[x][current] = 2
                except:
                    print("! game[", x, "][", current, "] not in bounds")

            if (current == yUp - 1) | (current == yDown + 1):
                try:
                    if x > -2:
                        self.game[x + 1][current] = 2
                except:
                    print("! game[", x + 1, "][", current, "] not in bounds")

                try:
                    if x > 0:
                        self.game[x - 1][current] = 2
                except:
                    print("! game[", x - 1, "][", current, "] not in bounds")
            current += 1


    def checkPipes(self):
        self.clear(2)
        if (self.cX > -2) & (self.cX < self.width + 1):
            print("Case 1: ", self.cX, self.cY, self.cLevel)
            self.pipes(self.cX, self.cY, self.cLevel)
        if self.cX < -1:
            self.cLevel = self.checkLevel()
            self.cX = self.width
            self.cY = random.randint((self.getspacing(self.cLevel) / 2) + 1, (self.height - 1) - ((self.getspacing(self.cLevel) / 2) + 1))
            print("Case 2: ", self.cX, self.cY, self.cLevel)
            self.pipes(self.cX, self.cY, self.cLevel)
        self.cX = self.cX - 1


    def jump(self):
        current_position = self.getCurrentPlayerPosition()
        if (self.gamestatus == 1) & (current_position > 1):
            nPosition = current_position - 2  # previously 4
            if self.hitdetection(1) == 0:
                self.clear(1)
                self.game[1][nPosition] = 1


    def gravity(self):
        current_position = self.getCurrentPlayerPosition()
        if (self.gamestatus == 1) and (current_position < (self.height - 1)):
            next_position = current_position + 1  # previously 2
            if self.hitdetection(2) == 0:
                self.clear(1)
                self.game[1][next_position] = 1


    def hitdetection(self, case) -> int:
        hitdetected = 0
        cPlayerPos = self.getCurrentPlayerPosition()
        if (cPlayerPos < (self.height - 1)) & (cPlayerPos > 1):  # Out of bounds
            if case == 1:  # Jump
                if self.game[2][cPlayerPos - 1] == 2:  # forward up
                    hitdetected = 1
                elif self.game[2][cPlayerPos - 2] == 2:  # forward 2 up
                    hitdetected = 1
                elif self.game[1][cPlayerPos - 1] == 2:  # on top
                    hitdetected = 1

            if case == 2:  # Gravity
                if self.game[2][cPlayerPos + 1] == 2:  # forward down
                    hitdetected = 1
                elif self.game[1][cPlayerPos + 1] == 2:  # down
                    hitdetected = 1
        else:
            print("Player Position out of bounds")
            hitdetected = 1

        if hitdetected == 1:
            print("! Hit detected")
            self.gameover = 1
        return hitdetected


    def initPlayer(self):
        self.game[1][int(self.height / 2)] = 1


    def screensaver(self):
        cPlayerPos = self.getCurrentPlayerPosition()
        drop = 1
        # if Pipes only 5 (or less) away and if distance to the middle is over 8 then double jumps
        if ((self.cX - 1) <= 5) & (abs(cPlayerPos - self.cY) > 8):
            drop = 2

        if cPlayerPos != self.cY:
            if cPlayerPos > self.cY:
                self.setCurrentPlayerPosition(cPlayerPos - drop)
            else:
                self.setCurrentPlayerPosition((cPlayerPos + drop))


    def getCurrentPlayerPosition(self):
        for i in range(self.height):
            if self.game[1][i] == 1:
                return i
        return -1


    def setCurrentPlayerPosition(self, y):
        self.game[1][self.getCurrentPlayerPosition()] = 0
        self.game[1][y] = 1


    def getspacing(self, level):
        spacing = {
            1: 12,
            2: 10,
            3: 8,
            4: 6,
            5: 4
        }
        return spacing.get(level, -1)


    def getColor(self, value):
        rgbTuple = {
            0: (0, 188, 255),  # Background: Light Blue
            1: (255, 0, 0),  # Player: Red
            2: (0, 255, 34)  # Pipe: Green
        }
        return rgbTuple.get(value, -1)


    def scorecounter(self):
        if self.cX == 1:
            self.score += 1
            print("Score updated to: ", self.score)


    def clear(self, type):
        for i in range(self.width):
            for j in range(self.height):
                if self.game[i][j] == type:
                    self.game[i][j] = 0


    def checkLevel(self):
        level = 1
        if self.score < 5:
            level = 1
        elif self.score < 10:
            level = 2
        elif self.score < 15:
            level = 3
        elif self.score < 20:
            level = 4
        if self.score >= 20:
            level = 5  # later maybe level = int(score/4)
        return level


    def translator(self):
        tupleMatrix = [[(0, 0, 0) for j in range(15)] for i in range(30)]
        for a in range(self.width):
            for b in range(self.height):
                self.matrix[a, b] = self.getColor(self.game[a][b])

        self.out.set_matrix(tupleMatrix)
        self.out.submit_all()


    def clock(self):
        while self.gameover == 0:
            self.checkPipes()
            #self.screensaver()
            self.scorecounter()

            for i in range(2):
                self.gravity()
                self.translator()
                time.sleep(0.1)
                i += 1


    def input(self, inp):
        self.jump()

    def get_html(self):
        with open("..FlappyBird.html", "r") as f:
            return f.read()

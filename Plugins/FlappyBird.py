from Plugins.Plugin import Plugin
import time
import random

class BootPlugin(Plugin):
    width = 15
    height = 30
    cX = -2
    cY = 0
    cLevel = 0
    gameover = 0
    score = 0


    def __init__(self, app, matrix):
        super().__init__(app, matrix)


    def run(self):

        def pipes(x, y, level):
            if (y < 0) | (y > self.height - 1):
                print("! y out of bounds")
                return

            distance = int(getspacing(level) / 2)
            yUp = y - distance
            yDown = y + distance

            current = 0
            while current <= self.height - 1:
                if (current < yUp) | (current > yDown):
                    try:
                        if x > -1:
                            game[x][current] = 2
                    except:
                        print("! game[", x, "][", current, "] not in bounds")

                if (current == yUp - 1) | (current == yDown + 1):
                    try:
                        if x > -2:
                            game[x + 1][current] = 2
                    except:
                        print("! game[", x + 1, "][", current, "] not in bounds")

                    try:
                        if x > 0:
                            game[x - 1][current] = 2
                    except:
                        print("! game[", x - 1, "][", current, "] not in bounds")
                current += 1


        def checkPipes():
            clear(2)
            if (self.cX > -2) & (self.cX < self.width + 1):
                print("Case 1: ", self.cX, self.cY, self.cLevel)
                pipes(self.cX, self.cY, self.cLevel)
            if self.cX < -1:
                self.cLevel = checkLevel()
                self.cX = self.width
                self.cY = random.randint((getspacing(self.cLevel) / 2) + 1, (self.height - 1) - ((getspacing(self.cLevel) / 2) + 1))
                print("Case 2: ", self.cX, self.cY, self.cLevel)
                pipes(self.cX, self.cY, self.cLevel)
            self.cX = self.cX - 1


        def hitdetection(case):
            hitdetected = 0
            if case == 1:  # Jump
                if game[2][getCurrentPlayerPosition() - 1] == 2:  # forward up
                    hitdetected = 1
                elif game[2][getCurrentPlayerPosition() - 2] == 2:  # forward 2 up
                    hitdetected = 1
                elif game[1][getCurrentPlayerPosition() - 1] == 2:  # on top
                    hitdetected = 1

            if case == 2:  # Gravity
                if game[2][getCurrentPlayerPosition() + 1] == 2:  # forward down
                    hitdetected = 1
                elif game[1][getCurrentPlayerPosition() + 1] == 2:  # down
                    hitdetected = 1

            if hitdetected == 1:
                self.gameover == 1
            return hitdetected

        def initPlayer():
            game[1][int(self.height / 2)] = 1


        def hacks():
            zip = getCurrentPlayerPosition()
            if zip != self.cY:
                if zip > self.cY:
                    setCurrentPlayerPosition(zip - 1)
                else:
                    setCurrentPlayerPosition((zip + 1))


        def getCurrentPlayerPosition():
            for i in range(self.width):
                for j in range(self.height):
                    if game[i][j] == 1:
                        return j
            return -1

        def setCurrentPlayerPosition(y):
            game[1][getCurrentPlayerPosition()] = 0
            game[1][y] = 1


        def getspacing(level):
            spacing = {
                1: 12,
                2: 10,
                3: 8,
                4: 6,
                5: 4
            }
            return spacing.get(level, -1)


        def getColor(value):
            rgbTuple = {
                0: (0, 188, 255),  # Background: Light Blue
                1: (255, 0, 0),  # Player: Red
                2: (0, 255, 34)  # Pipe: Green
            }
            return rgbTuple.get(value, -1)

        def scorecounter():
            if (self.cX == 1):
                self.score += 1


        def clear(type):
            for i in range(self.width):
                for j in range(self.height):
                    if game[i][j] == type:
                        game[i][j] = 0

        def checkLevel():
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


        def translator():
            tupleMatrix = [[(0, 0, 0) for j in range(15)] for i in range(30)]
            for a in range(self.width):
                for b in range(self.height):
                    self.matrix[a, b] = getColor(game[a][b])

            self.matrix.set_matrix(tupleMatrix)
            self.matrix.submit_all()


        def clock():
            while self.gameover == 0:
                checkPipes()
                hacks()
                scorecounter()
                translator()
                time.sleep(0.1)


        game = [[0 for j in range(self.height)] for i in range(self.width)]
        for i in range(self.width):
            for j in range(self.height):
                game[i][j] = 0

        initPlayer()
        clock()


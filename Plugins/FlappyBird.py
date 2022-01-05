from Plugins.Plugin import Plugin
import time
import random

class BootPlugin(Plugin):
    width = 15
    height = 30
    cX = -2
    cY = 0
    cLevel = 0

    def __init__(self, app, matrix):
        super().__init__(app, matrix)

    #Run wird beim start ausgeführt und muss den Code enthalten, der im endeffekt ausgeführt werden soll
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

        # Returns the spacing between pipes depending on the level
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


        def clear(type):
            for i in range(self.width):
                for j in range(self.height):
                    if game[i][j] == type:
                        game[i][j] = 0

        def checkLevel():
            return random.randint(1,5)

        def translator():
            tupleMatrix = [[(0, 0, 0) for j in range(15)] for i in range(30)]
            for a in range(self.width):
                for b in range(self.height):
                    self.matrix[a, b] = getColor(game[a][b])
            self.matrix.set_matrix(tupleMatrix)
            self.matrix.submit_all()


        def clock():
            for i in range (60):
                checkPipes()
                translator()
                time.sleep(0.1)


        game = [[0 for j in range(self.height)] for i in range(self.width)]
        for i in range(self.width):
            for j in range(self.height):
                game[i][j] = 0

        clock()


from Plugins.Plugin import Plugin
import time
import random

class BootPlugin(Plugin):
    def __init__(self, app, matrix):
        super().__init__(app, matrix)

    #Run wird beim start ausgeführt und muss den Code enthalten, der im endeffekt ausgeführt werden soll
    def run(self):
        width = 15
        height = 30
        cX = -2
        cY = 0
        cLevel = 0

        def pipes(x, y, level):
            if (y < 0) | (y > height - 1):
                print("! y out of bounds")
                return

            distance = int(getspacing(level) / 2)
            yUp = y - distance
            yDown = y + distance

            current = 0
            while current <= height - 1:
                if (current < yUp) | (current > yDown):
                    try:
                        if (x > -1):
                            game[x][current] = 2
                    except:
                        print("! game[", x, "][", current, "] not in bounds")

                if (current == yUp - 1) | (current == yDown + 1):
                    try:
                        if (x > -2):
                            game[x + 1][current] = 2
                    except:
                        print("! game[", x + 1, "][", current, "] not in bounds")

                    try:
                        if (x > 0):
                            game[x - 1][current] = 2
                    except:
                        print("! game[", x - 1, "][", current, "] not in bounds")
                current += 1


        def checkPipes():
            global cX
            global cY
            global cLevel

            self.matrix.fill_all((0, 188, 255))
            if (cX > -2) & (cX < width + 1):
                print("Case 1: ", cX, cY, cLevel)
                pipes(cX, cY, cLevel)
            if cX < -1:
                cLevel = checkLevel()
                cX = width
                cY = random.randint((getspacing(cLevel) / 2) + 1, (height - 1) - ((getspacing(cLevel) / 2) + 1))
                print("Case 2: ", cX, cY, cLevel)
                pipes(cX, cY, cLevel)
            cX = cX - 1

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


        def checkLevel():
            return random.randint(1,5)

        def translator():
            tupleMatrix = [[(0, 0, 0) for j in range(15)] for i in range(30)]
            for a in range(height):
                for b in range(width):
                    self.matrix[a, b] = getColor(game[b][a])
            self.matrix.set_matrix(tupleMatrix)


        def clock():
            for i in range (60):
                checkPipes()
                translator()
                time.sleep(0.017)


        game = [[0 for j in range(height)] for i in range(width)]
        for i in range(width):
            for j in range(height):
                game[i][j] = 0

        clock()


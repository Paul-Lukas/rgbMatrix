from Plugins.Plugin import Plugin

import time
import random


class BootPlugin(Plugin):
    def __init__(self, app, matrix):
        super().__init__(app, matrix)


    #Run wird beim start ausgeführt und muss den Code enthalten, der im endeffekt ausgeführt werden soll
    def run(self):
        def reloadboardrandom(punktespieler1,punktespieler2,punktespieler3,punktespieler4):
            global punktegesamtspieler1
            global punktegesamtspieler2
            global punktegesamtspieler3
            global punktegesamtspieler4
            while punktespieler1 >= 0:
                randomy = randint(0,29)
                randomx = randint(0,14)
                if besitz[randomy][randomx] == 0:
                    besitz[randomy][randomx] = 1
                    punktespieler1 -= 1
                    punktegesamtspieler1 += 1
                if (punktegesamtspieler1 + punktegesamtspieler2 + punktegesamtspieler3 + punktegesamtspieler4) == 450:
                    break
            while punktespieler2 >= 0:
                randomy = randint(0,29)
                randomx = randint(0,14)
                if besitz[randomy][randomx] == 0:
                    besitz[randomy][randomx] = 2
                    punktespieler2 -= 1
                    punktegesamtspieler2 += 1
                if (punktegesamtspieler1 + punktegesamtspieler2 + punktegesamtspieler3 + punktegesamtspieler4) == 450:
                    break
            while punktespieler3 >= 0:
                randomy = randint(0,29)
                randomx = randint(0,14)
                if besitz[randomy][randomx] == 0:
                    besitz[randomy][randomx] = 3
                    punktespieler3 -= 1
                    punktegesamtspieler3 += 1
                if (punktegesamtspieler1 + punktegesamtspieler2 + punktegesamtspieler3 + punktegesamtspieler4) == 450:
                    break
            while punktespieler4 >= 0:
                randomy = randint(0,29)
                randomx = randint(0,14)
                if besitz[randomy][randomx] == 0:
                    besitz[randomy][randomx] = 4
                    punktespieler4 -= 1
                    punktegesamtspieler4 += 1
                if (punktegesamtspieler1 + punktegesamtspieler2 + punktegesamtspieler3 + punktegesamtspieler4) == 450:
                    break

            print("\n")
            for i in range(30):
                print(besitz[i])
            print(punktegesamtspieler1)
            print(punktegesamtspieler2)
            print(punktegesamtspieler3)
            print(punktegesamtspieler4)
                
            for y in range(30):
                for x in range(15):
                    #setcoordinate(x,y,besitz[y][x])
                    if besitz[y][x] == 1:
                        self.matrix[x, y] = (255, 0, 0)
                    elif besitz[y][x] == 2:
                        self.matrix[x, y] = (0, 0, 255)
                    elif besitz[y][x] == 3:
                        self.matrix[x, y] = (0, 255, 0)
                    elif besitz[y][x] == 4:
                        self.matrix[x, y] = (255, 255, 0)
                    else:
                        self.matrix[x, y] = (0, 0, 0)
            self.matrix.submit_all()

        def random():
            reloadboardrandom(randint(1,5),randint(1,5),randint(1,5),randint(1,5))

        

        punktegesamtspieler1 = 0
        punktegesamtspieler2 = 0
        punktegesamtspieler3 = 0
        punktegesamtspieler4 = 0
        wand = []
        reihe = []
        besitz = []
        row = []
        for i in range(30):
            reihe = []
            row = []
            for z in range(15):
                reihe += [(0,0,0)]
                row += [0]
            besitz += [row]
            wand += [reihe] 

        
        for i in range(30):
            random()
        return
        
        print("Fertig")

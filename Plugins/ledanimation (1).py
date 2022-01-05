from Plugins.Plugin import Plugin

import time
import random


class BootPlugin(Plugin):
    punktegesamtspieler1 = 0
    punktegesamtspieler2 = 0
    punktegesamtspieler3 = 0
    punktegesamtspieler4 = 0
    def __init__(self, app, matrix):
        super().__init__(app, matrix)


    #Run wird beim start ausgeführt und muss den Code enthalten, der im endeffekt ausgeführt werden soll
    def run(self):
        self.punktegesamtspieler1 = 0
        self.punktegesamtspieler2 = 0
        self.punktegesamtspieler3 = 0
        self.punktegesamtspieler4 = 0
        
        def reloadboardrandom(punktespieler1,punktespieler2,punktespieler3,punktespieler4):
            while punktespieler1 >= 0:
                randomy = randint(0,29)
                randomx = randint(0,14)
                if besitz[randomy][randomx] == 0:
                    besitz[randomy][randomx] = 1
                    punktespieler1 -= 1
                    self.punktegesamtspieler1 += 1
                if (self.punktegesamtspieler1 + self.punktegesamtspieler2 + self.punktegesamtspieler3 + self.punktegesamtspieler4) == 450:
                    break
            while punktespieler2 >= 0:
                randomy = randint(0,29)
                randomx = randint(0,14)
                if besitz[randomy][randomx] == 0:
                    besitz[randomy][randomx] = 2
                    punktespieler2 -= 1
                    self.punktegesamtspieler2 += 1
                if (self.punktegesamtspieler1 + self.punktegesamtspieler2 + self.punktegesamtspieler3 + self.punktegesamtspieler4) == 450:
                    break
            while punktespieler3 >= 0:
                randomy = randint(0,29)
                randomx = randint(0,14)
                if besitz[randomy][randomx] == 0:
                    besitz[randomy][randomx] = 3
                    punktespieler3 -= 1
                    self.punktegesamtspieler3 += 1
                if (self.punktegesamtspieler1 + self.punktegesamtspieler2 + self.punktegesamtspieler3 + self.punktegesamtspieler4) == 450:
                    break
            while punktespieler4 >= 0:
                randomy = randint(0,29)
                randomx = randint(0,14)
                if besitz[randomy][randomx] == 0:
                    besitz[randomy][randomx] = 4
                    punktespieler4 -= 1
                    self.punktegesamtspieler4 += 1
                if (self.punktegesamtspieler1 + self.punktegesamtspieler2 + self.punktegesamtspieler3 + self.punktegesamtspieler4) == 450:
                    break

            print("\n")
            for i in range(30):
                print(besitz[i])
            print(self.punktegesamtspieler1)
            print(self.punktegesamtspieler2)
            print(self.punktegesamtspieler3)
            print(self.punktegesamtspieler4)
                
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

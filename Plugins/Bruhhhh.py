import random
import time
from Plugins.Plugin import Plugin

class BootPlugin(Plugin):
    self.FalschGeloest = 25
    self.z = 0
    self.matrix.fill_all((0, 0, 0))
    self.lauf = 0
        
    def __init__(self, app, matrix):
        super().__init__(app, matrix)
            
    def run(self):
        self.matrix.fill_all((0, 0, 0))
        self.matrix[0, 29] = (236, 178, 83)
        self.matrix[1, 29] = (236, 178, 83)
        self.matrix[0, 28] = (236, 178, 83)
        self.matrix[1, 28] = (236, 178, 83)
        self.matrix[5, 29] = (77, 137, 40)
        self.matrix[4, 29] = (77, 137, 40)
        self.matrix[5, 28] = (77, 137, 40)
        self.matrix[4, 28] = (77, 137, 40)
        self.matrix[9, 29] = (58, 133, 213)
        self.matrix[10, 29] = (58, 133, 213)
        self.matrix[9, 28] = (58, 133, 213)
        self.matrix[10, 28] = (58, 133, 213)
        self.matrix[13, 29] = (204, 215, 69)
        self.matrix[14, 29] = (204, 215, 69)
        self.matrix[13, 28] = (204, 215, 69)
        self.matrix[14, 28] = (204, 215, 69)

    
    if (self.lauf <= 50):
         if (z <= 24):
             self.matrix[0, self.FalschGeloest] = (255, 0, 0)
             self.matrix[1, self.FalschGeloest] = (255, 0, 0)
             self.matrix[4, self.FalschGeloest] = (255, 0, 0)
             self.matrix[5, self.FalschGeloest] = (255, 0, 0)
             self.matrix[9, self.FalschGeloest] = (255, 0, 0)
             self.matrix[10, self.FalschGeloest] = (255, 0, 0)
             self.matrix[13, self.FalschGeloest] = (255, 0, 0)
             self.matrix[14, self.FalschGeloest] = (255, 0, 0)
             self.FalschGeloest = self.FalschGeloest - 1
             self.z = self.z + 1
             time.sleep(0.01)
             self.lauf = self.lauf + 1
                    
         else:
            self.matrix[0, self.FalschGeloest] = (0, 0, 0)
            self.matrix[1, self.FalschGeloest] = (0, 0, 0)
            self.matrix[4, self.FalschGeloest] = (0, 0, 0)
            self.matrix[5, self.FalschGeloest] = (0, 0, 0)
            self.matrix[9, self.FalschGeloest] = (0, 0, 0)
            self.matrix[10, self.FalschGeloest] = (0, 0, 0)
            self.matrix[13, self.FalschGeloest] = (0, 0, 0)
            self.matrix[14, self.FalschGeloest] = (0, 0, 0)
            self.FalschGeloest = self.FalschGeloest + 1

            time.sleep(0.01)
            self.lauf = self.lauf + 1
    else:
        self.z = 0
        return   


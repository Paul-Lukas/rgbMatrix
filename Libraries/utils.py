import random


class Utils:
    def random_tuple(self, lengh: int, **color_params) -> tuple:
        color_min = color_params.get("min", 0)
        color_max = color_params.get("max", 255)
        mtuple = []

        for i in range(lengh):
            mtuple.append(random.randint(color_min, color_max))
        return tuple(mtuple)

    def getRandomMatrix(self, width: int, heigh: int) -> list:
        matrix = [[(0, 0, 0) for j in range(heigh)] for i in range(width)]
        for i in range(width):
            for j in range(heigh):
                matrix[i][j] = self.random_tuple(3)
        return matrix

    def getChangedIndices(self, array1, array2):
        out = []
        for i in range(len(array1)):
            for j in range(len(array1[i])):
                if array1[i][j] != array2[i][j]:
                    out.append((i, j))
        return out

    def getNumForCords(self, x: int, y: int, xMax: int):
        if (x % 2) == 0:
            n = y + (x * xMax)
        else:
            n = (x * xMax) + (xMax - y - 1)
        return n

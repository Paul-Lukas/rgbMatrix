import random


class Utils:
    def random_tuple(self, lengh: int, **color_params) -> tuple:
        """
        :param lengh: lengh of tupel
        :param color_params: min or max to set minimum / maximum value of color (0 - 255 by default)
        :return: random Color Tuple
        """
        color_min = color_params.get("min", 0)
        color_max = color_params.get("max", 255)
        mtuple = []

        for i in range(lengh):
            mtuple.append(random.randint(color_min, color_max))
        return tuple(mtuple)

    def getRandomMatrix(self, width: int, heigh: int) -> list:
        """
        Generates a Matrix filled with random Color Tuples
        :param width: width of Matrix
        :param heigh: height of matrix
        :return: matrix filled with random Color Tuples
        """
        matrix = [[(0, 0, 0) for j in range(heigh)] for i in range(width)]
        for i in range(width):
            for j in range(heigh):
                matrix[i][j] = self.random_tuple(3)
        return matrix

    def getChangedIndices(self, array1, array2) -> list:
        """
        generates a List of tuples with the Coordinates which have changed from array1 to array2
        @param array1: first array
        @param array2: second array
        @return: list with the Coordinates which have changed example [ (1, 2), (3, 4), (5, 6) ]
        """
        out = []
        for i in range(len(array1)):
            for j in range(len(array1[i])):
                if array1[i][j] != array2[i][j]:
                    out.append((i, j))
        return out

    def getNumForCords(self, x: int, y: int, yLen: int):
        """
        calculates the Number in the Pixel String from Coordinates
        @param x: x value
        @param y: y value
        @param yLen: lengh of y (height value)
        @return: number in Pixel String
        """
        if (x % 2) == 0:
            n = y + (x * yLen)
        else:
            n = (x * yLen) + (yLen - y - 1)
        return n

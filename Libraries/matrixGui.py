import tkinter as tk

class NeoMatrixGui():
    matrix = []
    canvas = tk.Canvas
    root = tk.Tk()
    size = 20

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

        self.root.title("Matrix Sim")
        self.root.geometry(str(self.width*self.size)+"x"+str(self.height*self.size))

        self.canvas = tk.Canvas(
            self.root,
            height= self.height * self.size,
            width= self.width * self.size
        )

        self.canvas.pack()

        self.matrix = [[(0, 0, 0) for j in range(height)] for i in range(width)]

    def __getitem__(self, item):
        if len(item) != 2:
            raise ValueError('Index needs two values example: [1, 2]')
        return self.matrix[item[0]][item[1]]

    def __setitem__(self, key, value):
        if len(key) != 2:
            raise ValueError('Index needs two values example: [1, 2]')
        self.matrix[key[0]][key[1]] = value

    def submit_all(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                colorval = "#%02x%02x%02x" % self.matrix[i][j]

                self.canvas.create_rectangle(i*self.size, j*self.size, i*self.size+self.size, j*self.size+self.size, fill=colorval)
        self.root.update_idletasks()
        self.root.update()

    def fill_all(self, color: tuple):
        """
        Fills sets all the Pixels to the specified color
        :param color: needs to be a tripel with RGB values example: (255, 6, 187)
        """
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                self.matrix[i][j] = color
        self.submit_all()

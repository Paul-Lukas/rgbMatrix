import tkinter as tk


class NeoMatrixGui():
	matrix = []
	oldmatrix = []
	canvas = tk.Canvas
	root = tk.Tk()
	size = 20


	def __init__(self, width: int, height: int):
		self.width = width
		self.height = height

		self.root.title("Application Sim")
		self.root.geometry(str(self.width * self.size) + "x" + str(self.height * self.size))

		self.canvas = tk.Canvas(
			self.root,
			height = self.height * self.size,
			width = self.width * self.size
		)

		self.canvas.pack()

		self.matrix = [[(0, 0, 0) for j in range(height)] for i in range(width)]
		self.oldmatrix = [[(0, 0, 0) for j in range(height)] for i in range(width)]


	def __getitem__(self, item):
		if len(item) != 2:
			raise ValueError('Index needs two values example: [1, 2]')
		return self.matrix[item[0]][item[1]]


	def __setitem__(self, key, value):
		if len(key) != 2:
			raise ValueError('Index needs two values example: [1, 2]')
		self.matrix[key[0]][key[1]] = value


	def __getChangedIndices(self, array1, array2):
		out = []
		for i in range(len(array1)):
			for j in range(len(array1[i])):
				if array1[i][j] != array2[i][j]:
					out.append((i, j))
		return out


	def submit_all(self):
		changes = self.__getChangedIndices(self.matrix, self.oldmatrix)

		for change in changes:
			colorval = "#%02x%02x%02x" % self.matrix[change[0]][change[1]]
			self.canvas.create_rectangle(change[0] * self.size, change[1] * self.size,
			                             change[0] * self.size + self.size,
			                             change[1] * self.size + self.size,
			                             fill = colorval)

		self.oldMatrix = [row[:] for row in self.matrix]

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


	def set_matrix(self, matrix):
		"""
		Replace the matrix
		:param matrix: new 2dim tupel array must be same lengh as old one
		:return: true if lengh is right, false if not
		"""
		if len(matrix) != len(self.matrix):
			return False
		else:
			if len(matrix[0]) != len(self.matrix[0]):
				return False
			else:
				self.matrix = matrix
				return True

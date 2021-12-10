import neopixel


class NeoMatrix:
	"""
	Handels all the Conversion from Application to String
	The Application must be horizontal
	"""
	matrix = []
	width = 0
	height = 0

	__pixels = object


	def __init__(self, width: int, height: int, pixels: neopixel.NeoPixel):
		self.width = width
		self.height = height

		self.__pixels = pixels

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
		"""
		Writes all the changes to tne Neopixel String
		"""
		i = 0
		for pixel in self.__convert_matrix(self.matrix):
			self.__pixels[i] = pixel
			i += 1
		self.__pixels.write()


	def fill_all(self, color: tuple):
		"""
		Fills sets all the Pixels to the specified color
		:param color: needs to be a tripel with RGB values example: (255, 6, 187)
		"""
		for i in range(len(self.matrix)):
			for j in range(len(self.matrix[i])):
				self.matrix[i][j] = color
		self.__pixels.fill(color)
		self.__pixels.write()


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


	def __convert_matrix(self, matrix) -> list:
		"""
		Converts a specific Application to an Array
		Example: input=  [
							[1, 2, 3, 4, 5],
							[10, 9, 8, 7, 6],
							[11, 12, 13, 14, 15]
						 ]
		:param matrix: Application(two dimensional array) uneven columns flipped
		:return: one dimensional Array
		"""
		index = []
		for i in range(len(matrix)):
			if i % 2 == 0:
				index.append(matrix[i])
			else:
				index.append(self.__flip_array(matrix[i]))

		return self.__flatten_array(index)


	def __flip_array(self, array: list) -> list:
		"""
		Flips an array
		Example: input=  [1, 2, 3, 4, 5]
				 Output= [5, 4, 3, 2, 1]
		:param array: Array to flip
		:return: Flipped Array
		"""
		flipped = []
		for i in range(len(array)):
			index = i * (-1) - 1
			flipped.append(array[index])
		return flipped


	def __flatten_array(self, array: list) -> list:
		"""
		Flattens two dimensional array to one dimensional
		Example: input=  [
							[1, 2, 3, 4, 5],
							[6, 7, 8, 9, 10]
						 ]

				 Output= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
		:param array: two dimensional array
		:return: one dimensional array
		"""
		flat = []

		for i in array:
			for j in i:
				flat.append(j)
		return flat

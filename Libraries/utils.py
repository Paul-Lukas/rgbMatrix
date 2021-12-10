import random


class utils:

	def __random_tuple(lengh: int, **color_params) -> tuple:
		color_min = color_params.get("min", 0)
		color_max = color_params.get("max", 255)
		mtuple = []

		for i in range(lengh):
			mtuple.append(random.randint(color_min, color_max))
		return tuple(mtuple)


	def __getChangedIndices(array1, array2):
		out = []
		for i in range(len(array1)):
			for j in range(len(array1[i])):
				if array1[i][j] != array2[i][j]:
					out.append((i, j))
		return out

import neopixel
import board

import Libraries.matrix as matrix

if __name__ == '__main__':
    pixels = neopixel.NeoPixel(board.NEOPIXEL, 20, auto_write=False)
    matrix = matrix.NeoMatrix(height=10, width=10, pixels=pixels)

    matrix[1,2] = (255, 0, 0)


from Application.BaseApplication import BaseApplication

import board
import neopixel

if __name__ == '__main__':
    pixels = neopixel.NeoPixel(board.D18, 450, auto_write = False)
    omatrix = matrix.NeoMatrix(15, 30, pixels)

    app = BaseApplication(omatrix)
    app.run()

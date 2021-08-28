import time

import board
import neopixel

import matrix


if __name__ == '__main__':
    pixels = neopixel.NeoPixel(board.D18, 450, auto_write=False)
    omatrix = matrix.NeoMatrix(15, 30, pixels)

    omatrix.fill_all((0, 0, 0))
    time.sleep(1)
    # R
    omatrix.fill_all((255, 0, 0))
    time.sleep(1)
    # G
    omatrix.fill_all((0, 255, 0))
    time.sleep(1)
    # B
    omatrix.fill_all((0, 0, 255))
    time.sleep(1)
    omatrix.fill_all((255, 255, 255))
    time.sleep(1)
    omatrix.fill_all((0, 0, 0))
    time.sleep(1)

    omatrix[0, 0] = (0, 0, 255)
    omatrix[14, 0] = (0, 255, 255)
    omatrix[0, 29] = (0, 255, 255)
    omatrix[14, 29] = (0, 255, 0)

    omatrix.submit_all()

    time.sleep(2)

    for i in range(30):
        for j in range(15):
            if (i + j) % 2 == 0:
                omatrix[j, i] = (255, 0, 0)
            else:
                omatrix[j, i] = (0, 0, 255)

            time.sleep(0.25)
            omatrix.submit_all()

    omatrix.fill_all((0, 0, 0))
    omatrix.submit_all()
    
    print("Fertig")

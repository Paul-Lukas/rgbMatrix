from PIL import Image, ImageSequence

with Image.open(r"New Piskel.gif") as im:
    i = 0
    array = []
    for frame in ImageSequence.Iterator(im):
        rgb_im = frame.convert('RGB')
        x, y = frame.size
        array2 = [[]] * x
        for j in range(x):
            for k in range(y):
                pixel = rgb_im.getpixel((j, k))
                array2[j].append(pixel)

        array.append(array2)
        i += 1

    #print(array)
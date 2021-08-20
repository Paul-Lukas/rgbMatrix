from PIL import Image

class imgToArray:
    img = object
    oarray = list

    def img_to_array(img_path):
        img = Image.open(img_path)
        ow = img.size[0]
        oh = img.size[1]

        ratio = int((oh / ow) * 15)

        size = (15, ratio)

        out = img.resize(size)

        oarray = [[out.getpixel((j, i)) for j in range(size[0])] for i in range(size[1])]

        return print(oarray)

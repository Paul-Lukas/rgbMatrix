import PIL

class imgToArray:
    img = object

    def img_to_array(self, img_path):
        img = PIL.Image.open(img_path)
        ow, oh = img.size()

        ratio = oh / ow

        out = img.resize((15, ratio * 15))

        return list(out)

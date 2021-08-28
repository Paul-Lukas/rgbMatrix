from PIL import Image, ImageSequence


class ImgTools:

    def read_gif(self, path):
        """
        Converts an Gif animation to Array of Pixels
        :param path: full path to the Gif
        :return: Array of Pixels
        Example:
        [ #Frames
            [ #Rows
                [(255, 0, 0), (123, 123, 123), (0, 73, 12)], #Tupels
                [(55, 65, 39), (12, 94, 124), (12, 0, 112)]
            ],
            [
                [(255, 0, 0), (123, 123, 123), (0, 73, 12)],
                [(255, 0, 0), (143, 12, 15), (0, 73, 12)]
            ]
        ]
        """
        with Image.open(path) as im:
            array = []
            for frame in ImageSequence.Iterator(im):
                array.append(self.__to_array(frame))
            return array

    def read_img(self, path):
        """
        Converts Image to Array of Pixels
        :param path: Full path to Image
        :return: Array of Pixels
        """
        with Image.open(path) as im:
            array = self.__to_array(im)
            return array

    @staticmethod
    def __to_array(im):
        """
        Converts Image to Array
        :param im: Image / Frame
        """
        rgb_im = im.convert('RGB')
        x, y = im.size
        array = [[]] * x
        for i in range(x):
            for j in range(y):
                pixel = rgb_im.getpixel((i, j))
                array.append(pixel)
        return array

import matplotlib.pyplot as plt
from PIL import Image

from filter import Filter

if __name__ == '__main__':
    image = Image.open("data/lena.png")

    # plt.imshow(image, cmap='gray')
    # plt.show()
    #
    # bw = Filter.black_white(image)
    #
    # plt.imshow(bw, cmap='gray')
    # plt.show()
    #
    # blurry_bw = Filter().blurry(bw)
    # plt.imshow(blurry_bw, cmap='gray')
    # plt.show()

    blurry_color = Filter().blurry(image)
    plt.imshow(blurry_color)
    plt.show()

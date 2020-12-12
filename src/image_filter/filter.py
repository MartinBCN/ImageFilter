import numpy as np
from PIL import Image
from scipy.signal import convolve2d


class Filter(object):
    @staticmethod
    def black_white(img: Image) -> Image:
        """
        Transform a RGB image into BW

        Parameters
        ----------
        img

        Returns
        -------

        """
        img_array = np.array(img)
        bw = img_array.mean(axis=2)
        return Image.fromarray(np.uint8(bw))

    @staticmethod
    def gaussian_filter(x: float = 9.5):
        n = 20
        offset = 2 * n * (1 - x)
        a = np.zeros((n, n))
        for i in range(n):
            for j in range(n):
                dist = (i - offset) ** 2 + (j - offset) ** 2
                a[i, j] = np.exp(-dist / 50.)
        a /= a.sum()  # normalize the kernel
        return a

    def blurry(self, img: Image, x: float) -> Image:

        img_array = np.array(img)
        gaussian_filter = self.gaussian_filter(x)

        # in color
        out = np.zeros(img_array.shape)
        print(out.shape)

        if len(out.shape) == 2:
            # BW
            out = convolve2d(img_array, gaussian_filter, mode='same')
        elif len(out.shape) == 3:
            # RGB
            for i in range(3):
                out[:, :, i] = convolve2d(img_array[:, :, i], gaussian_filter, mode='same')
        else:
            raise ValueError

        return Image.fromarray(np.uint8(out))

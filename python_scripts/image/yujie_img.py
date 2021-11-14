import numpy as np
import matplotlib.pyplot as plt
import cv2


class Image:
    def __init__(self, *args, **kwargs):
        """
        args -- tuple of anonymous arguments
        kwargs -- dictionary of named arguments
        """
        if kwargs.get('path') != None:
            self.img_path = kwargs.get("path")
            self.img_bgr = cv2.imread(self.img_path)
            b, g, r = cv2.split(self.img_bgr)
            self.img = cv2.merge([r, g, b])
            self.width, self.height, self.channel = self.read_property()
        elif kwargs.get('bgr') == True:
            b, g, r = cv2.split(args[0])
            self.img = cv2.merge([r, g, b])
            self.width, self.height, _ = self.read_property()
            self.channel = 3
        elif kwargs.get('rgb') == True:
            self.img = args[0]
            self.width, self.height, _ = self.read_property()
            self.channel = 3
        elif kwargs.get('intensity') == True:
            self.img = args[0]
            self.width, self.height, _ = self.read_property()
            self.channel = 1
        if self.channel == 3:
            self.img_gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        elif self.channel == 1:
            self.img_gray = self.img.copy()
        else:
            print("Image with unsupported channels")
        self.img_thres = None
        self.img_float = None

    def read_property(self):
        if self.img.ndim == 2:
            channel = 1
        elif self.img.ndim == 3:
            channel = self.img.shape[2]
        width = self.img.shape[1]
        height = self.img.shape[0]
        return width, height, channel

    def get_thres(self, th1, th2):
        if (th1 < th2) & (th1 > 0) & (th2 < np.max(self.img_gray)):
            self.thres_img = self.img_gray.copy()
            self.thres_img[self.thres_img > th2] = 0
            self.thres_img[self.thres_img < th1] = 0
            self.thres_img[(self.thres_img >= th1) & (self.thres_img <= th2)] = 255
        else:
            print("Error: invalid thresholds")
            print(th1 < th2)
            print(th1 > 0)
            print(th2 < np.max(self.img_gray))

    def cast_float(self):
        self.img_float = np.float32(self.img)

    def draw_hist(self, num_bins=256):
        plt.hist(self.img_gray.reshape(-1), num_bins, facecolor='blue', alpha=0.5)
        plt.show()

    def draw_img(self, flag='r', figsize=[6, 6]):
        """
        'r': raw
        'g': gray
        't': threshold
        'c': color separately
        """
        if flag == 'r':
            plt.imshow(self.img)
            plt.show()
        elif flag == 'g':
            plt.imshow(self.img_gray)
            plt.show()
        elif flag == 't':
            plt.imshow(self.thres_img)
            plt.show()
        elif flag == 'c':
            plt.figure(100, figsize)
            for i in range(3):
                colors = ['Red', 'Green', 'Blue']
                plt.subplot(1, 3, i + 1)
                plt.imshow(self.img[:, :, i])
                plt.axis('off')
                plt.title(colors[i])

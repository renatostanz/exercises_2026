# The user can get an RGB color histogram from this script

# To execute this script the user must execute it with its image path as a command line argument.

import matplotlib.pyplot as plt
import sys
import os
import cv2 as cv
from numpy import array, asarray


def get_img_path() -> str:
    path = sys.argv[-1]
    if not os.path.exists(path):
        raise FileNotFoundError(f"No such file: {path}")

    img_extensions = [".jpg", ".jpeg", ".png"]
    has_valid_extensions = lambda extensions: False if len(extensions) == 0 else True if path.endswith(extensions[-1]) else has_valid_extensions(extensions[:-1])

    if not has_valid_extensions(img_extensions):
        raise TypeError(f"The selected file must contain a valid image extension. Such as: {', '.join(img_extensions[:-1])}, {img_extensions[-1]}")

    return path
    

class Histogram():
    def __init__(self, img_path: str | os.PathLike) -> None:
        try:
            img = cv.imread(img_path)
        except:
            raise IOError("The image path you provided didn't fit the opencv criteria.")

        self.set_img(img)


    def set_img(self, new_img) -> None:
        self.img = new_img
        img_height, img_width = self.img.shape[:2]
        self.upper_bound = 0


    def show_img(self) -> None:
        cv.imshow("Original Image", self.img)


    def get_hist(self, img: array) -> list[int]:
        hist = [0 for i in range(256)]

        for line in img[:]:
            for pixel in line:
                hist[pixel] += 1

        max_count = max(hist)
        if self.upper_bound * 1.05 < max_count:
            self.upper_bound = max_count * 1.05

        return hist


    def show_hist(self, img: array, color: str) -> None:
        hist = self.get_hist(img)

        hist_fig, ax = plt.subplots(figsize=(10, 5), dpi=100)
        ax.plot(hist, color=color, linewidth=2, label=f'{color.capitalize()} Pixels Count')
        ax.set_xlim(0, 255)
        ax.set_ylim(0, self.upper_bound)
        ax.set_xlabel("Intensity")
        ax.set_ylabel("Count")
        ax.set_title(f'{color.capitalize()} Histogram')
        ax.grid(True)
        ax.legend()

        hist_fig.canvas.draw()
        hist_rgba = asarray(hist_fig.canvas.buffer_rgba())
        hist_bgr = cv.cvtColor(hist_rgba, cv.COLOR_RGBA2BGR)

        plt.close(hist_fig)

        cv.imshow(f"{color.capitalize()} Histogram", hist_bgr)


    @staticmethod
    def wait_and_clear() -> None:
        cv.waitKey(0)
        cv.destroyAllWindows()
        

    def show_rgb_hists(self) -> None:
        rgb_img = cv.cvtColor(self.img, cv.COLOR_BGR2RGB)
        rgb_channels = cv.split(rgb_img)

        for rgb_channel, color in zip(rgb_channels, ['red', 'blue', 'green']):
            self.show_hist(rgb_channel, color)

        self.wait_and_clear()


if __name__ == "__main__":
    img_path = get_img_path()

    hist = Histogram(img_path)
    hist.show_img()
    hist.show_rgb_hists()

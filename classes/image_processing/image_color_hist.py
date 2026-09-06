# The user can get an RGB color histogram from this script

# To execute this script the user must add into its command line arguments the image path.
# If they want, they can also choose the histogram color by adding it as a command line argument.

import matplotlib.pyplot as plt
import sys
import os
import cv2 as cv
from numpy import array, asarray

def get_hist(img: array):
    hist = [0 for i in range(256)]

    for line in img[:]:
        for pixel in line:
            hist[pixel] += 1

    return hist


def show_hist(img: array, color: str):
    hist = get_hist(img)

    hist_fig, ax = plt.subplots(figsize=(10, 5), dpi=100)
    ax.plot([i for i, _ in enumerate(hist)], hist, color=color, linewidth=2, label=f'{color.capitalize()} Pixels Count')
    ax.set_title(f'{color.capitalize()} Histogram')
    ax.grid(True)
    ax.legend()

    hist_fig.canvas.draw()
    hist_rgba = asarray(hist_fig.canvas.buffer_rgba())
    hist_bgr = cv.cvtColor(hist_rgba, cv.COLOR_RGBA2BGR)

    plt.close(hist_fig)

    cv.imshow(f"{color.capitalize()} Histogram", hist_bgr)

    
def check_img_path(path: str) -> bool:
    if not os.path.exists(path):
        raise FileNotFoundError(f"No such file: {path}")

    img_extensions = [".jpg", ".jpeg", ".png"]
    has_valid_extensions = lambda extensions: False if len(extensions) == 0 else True if path.endswith(extensions[-1]) else has_valid_extensions(extensions[:-1])

    if not has_valid_extensions(img_extensions):
        raise TypeError(f"The selected file must contain a valid image extension. Such as: {', '.join(img_extensions[:-1])}, {img_extensions[-1]}")
    return True


def get_argv() -> list[str, str | None]:
    if sys.argv[-1].lower() not in ["red", "blue", "green"]:
        check_img_path(sys.argv[-1])
        return [sys.argv[-1].lower(), None]

    check_img_path(sys.argv[-2])
    return [i.lower() for i in sys.argv[-2:]]


if __name__ == "__main__":
    img_path, color = get_argv()
    img = cv.imread(img_path)
    img_resized = cv.resize(img, (960, 540))
    cv.imshow("Original Image Rezised", img_resized)
    rgb_img = cv.cvtColor(img_resized, cv.COLOR_BGR2RGB)

    if not color:
        color = input("Choose a color to plot a histogram: ").lower()

    rgb_channels = cv.split(rgb_img)
    single_color_img = rgb_channels[0]
    if color == "green":
        single_color_img = rgb_channels[1]
    elif color == "blue":
        single_color_img = rgb_channels[2]

    show_hist(single_color_img, color)

    cv.waitKey(0)
    cv.destroyAllWindows()

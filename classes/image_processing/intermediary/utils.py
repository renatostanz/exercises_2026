import cv2 as cv
import os

from numpy import ndarray

def load_rgb_img(path: str | os.PathLike) -> ndarray:
    print(f" | Loading line image ({path})")
    img = cv.imread(path)
    return cv.cvtColor(img, cv.COLOR_BGR2RGB)


def path_check(path: str | os.PathLike | None) -> bool:
    if path != None and os.path.exists(path):
        return True
    return False

def get_pixel_color_sum(pixel: ndarray) -> int:
    sum_ = 0
    for c in pixel:
        sum_ += int(c)
    return sum_

def is_pixel_colored_check(pixel: ndarray) -> bool: 
    pixel_sum = get_pixel_color_sum(pixel)
    return pixel_sum < (3 * 255)


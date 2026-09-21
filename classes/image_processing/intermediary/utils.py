import cv2 as cv
import os

from numpy import ndarray

def load_rgb_img(path: str | os.PathLike) -> ndarray:
    print(f"   Loading image ({path})")
    img = cv.imread(path)
    return cv.cvtColor(img, cv.COLOR_BGR2RGB)


def path_check(path: str | os.PathLike | None) -> bool:
    if path != None and os.path.exists(path):
        return True
    return False

def check_pixels_color_match(pixel_a: ndarray, pixel_b: ndarray) -> int:
    is_equal = True
    for value_a, value_b in zip(pixel_a, pixel_b):
        if value_a != value_b:
            return False
    return True

def is_pixel_colored(pixel: ndarray) -> bool: 
    pixel_sum = 0
    for c in pixel:
        pixel_sum += int(c)

    return pixel_sum < (3 * 255)


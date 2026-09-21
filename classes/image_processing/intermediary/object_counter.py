import random as rnd
import cv2 as cv
import os

from numpy import ndarray
from collections import deque
from utils import load_rgb_img, path_check, is_pixel_colored, check_pixels_color_match

class ObjectCounter:
    def __init__(self, path: str | os.PathLike | None):
        self.path = None
        if path_check(path):
            self.path = path


    @staticmethod
    def pick_random_img_path() -> str | os.PathLike:
        objects_options = [2, 3, 4]
        selected_object = rnd.choice(objects_options)

        path = os.path.join("data", f"{selected_object}objetos.bmp")

        if not os.path.exists(path):
            raise FileNotFoundError(f"Couldn't find a line image.")

        return path


    def fill_object_with_white(self, row: int, col: int) -> None:
        number_of_rows, number_of_cols, _ = self.rgb_img.shape
        origin_pixel = self.rgb_img[row, col].copy()
        self.rgb_img[row, col] = [255 for i in range(3)]
        next_pixels = deque([(row, col)])

        while len(next_pixels) > 0: 
            pixel_row, pixel_col = next_pixels.pop()

            for r in range(3):
                next_row = pixel_row + r - 1
                for c in range(3):
                    if (r, c) == (1, 1):
                        continue

                    next_col = pixel_col + c - 1

                    index_contitions = (
                        next_row >= 0 and 
                        next_row < number_of_rows and 
                        next_col >= 0 and 
                        next_col < number_of_cols
                    )

                    if index_contitions:
                        pixel = self.rgb_img[next_row, next_col]
                        if check_pixels_color_match(origin_pixel, pixel):
                            self.rgb_img[next_row, next_col] = [255 for i in range(3)]
                            next_pixels.append((next_row, next_col))


    def count_objects(self, path: str | os.PathLike | None) -> str:
        if path_check(path):
            print(" + Proceeding with new image file.")
        elif path_check(self.path):
            print(" + Proceeding with initial image file.")
            path = self.path
        else:
            print(" + Proceeding with random image file.")
            path = self.pick_random_img_path()

        self.rgb_img = load_rgb_img(path)
        number_of_rows, number_of_cols, _ = self.rgb_img.shape
        object_count = 0

        for row in range(number_of_rows):
            for col in range(number_of_cols):
                pixel = self.rgb_img[row, col]
                if is_pixel_colored(pixel):
                    self.fill_object_with_white(row, col)
                    object_count += 1

        return object_count

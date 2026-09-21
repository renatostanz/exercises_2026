import random as rnd
import cv2 as cv
import os

from numpy import ndarray
from utils import load_rgb_img, path_check, is_pixel_colored_check, get_pixel_color_sum

class LineClassifier:
    def __init__(self, path: str | os.PathLike | None) -> None:
        self.path = None
        if path_check(path):
            self.path = path


    @staticmethod
    def pick_random_line_path() -> str | os.PathLike:
        line_options = ["horizontal", "inclinada", "vertical"]
        selected_line = rnd.choice(line_options)

        path = os.path.join("data", f"{selected_line}.bmp")

        if not os.path.exists(path):
            raise FileNotFoundError(f"Couldn't find a line image.")

        return path


    @staticmethod
    def classify_line(rgb_img: ndarray) -> str:
        print(f" | Line's image loaded successfuly!\n | Starting classification process...")

        number_of_rows, number_of_columns, _ = rgb_img.shape
        for row in range(number_of_rows):
            for col in range(number_of_columns):
                pixel = rgb_img[row, col]
                if not is_pixel_colored_check(pixel):
                    continue

                if is_pixel_colored_check(rgb_img[row, col+1]):
                    return "horizontal"
                elif is_pixel_colored_check(rgb_img[row+1, col]):
                    return "vertical"
                elif is_pixel_colored_check(rgb_img[row+1, col+1]):
                    return "diagonal"
                return "point"


    def get_line_classification(self, path: str | os.PathLike | None) -> str:
        if path_check(path):
            print(" | Proceeding with new image file.")
        elif path_check(self.path):
            print(" | Proceeding with initial image file.")
            path = self.path
        else:
            print(" | Proceeding with random image file.")
            path = self.pick_random_line_path()

        rgb_img = load_rgb_img(path)
        return self.classify_line(rgb_img)


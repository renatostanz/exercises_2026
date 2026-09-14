import cv2 as cv
from utils import InteractiveColors, get_img_path

if __name__ == "__main__":
    img_path = get_img_path()
    interaction = InteractiveColors(img_path)

    interaction.show_interactive_window()
    cv.waitKey(0)
    cv.destroyAllWindows()

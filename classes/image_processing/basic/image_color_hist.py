# The user can get an RGB color histogram from this script

# To execute this script the user must execute it with its image path as a command line argument.

from utils import get_img_path, Histogram


if __name__ == "__main__":
    img_path = get_img_path()

    hist = Histogram(img_path)
    hist.show_source_img()
    hist.show_rgb_hists()
    hist.wait_and_clear()

from utils import get_img_path, Histogram


if __name__ == "__main__":
    img_path = get_img_path()

    hist = Histogram(img_path)
    hist.show_source_img()
    hist.show_rgb_hists()
    hist.wait_and_clear()

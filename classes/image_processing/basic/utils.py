import matplotlib.pyplot as plt
import sys
import os
import cv2 as cv
from numpy import array, asarray, vstack, ndarray, arange, uint8


def get_img_path() -> str | os.PathLike:
    path = sys.argv[-1]
    if not os.path.exists(path):
        raise FileNotFoundError(f"No such file: {path}")

    img_extensions = [".jpg", ".jpeg", ".png"]
    has_valid_extensions = lambda extensions: False if len(extensions) == 0 else True if path.endswith(extensions[-1]) else has_valid_extensions(extensions[:-1])

    if not has_valid_extensions(img_extensions):
        raise TypeError(f"The selected file must contain a valid image extension. Such as: {', '.join(img_extensions[:-1])}, {img_extensions[-1]}")

    return path



def load_img(img_path: str | os.PathLike) -> ndarray:
    try:
        img = cv.imread(str(img_path))
        if img is None:
            raise ValueError
    except Exception:
        raise IOError("The image path provided didn't fit the OpenCV criteria.")

    return img



class InteractiveColors:
    def __init__(self, img: str | os.PathLike | ndarray) -> None:
        if isinstance(img, (str, os.PathLike)):
            self.source_img = load_img(img)
        elif isinstance(img, ndarray):
            self.source_img = img

        self.source_img_hsv = cv.cvtColor(self.source_img, cv.COLOR_BGR2HSV)

        self.filtered_source_img = self.source_img.copy()
        self.filtered_source_img_hsv = self.source_img_hsv.copy()

        self.interactive_img = self.filtered_source_img.copy()
        self.interactive_img_hsv = self.filtered_source_img_hsv.copy()

        self.source_window_name = "Iteractive Source Image"
        self.interactive_window_name = "Interative Image"
        self.kernel_size = 3
        self.brightness_trackbar_value = 256


    def show_source_img(self) -> None:
        cv.imshow(self.source_window_name, self.img)


    def update_brightness(self, value: int) -> None:
        self.brightness_trackbar_value = value

        delta_value = value - 256
        for line in range(self.filtered_source_img_hsv.shape[0]):
            for column in range(self.filtered_source_img_hsv.shape[1]):
                original_pixel_value = int(self.filtered_source_img_hsv[line, column, 2])
                if original_pixel_value + delta_value <= 0:
                    self.interactive_img_hsv[line, column, 2] = 0
                elif original_pixel_value + delta_value >= 255:
                    self.interactive_img_hsv[line, column, 2] = 255
                else:
                    self.interactive_img_hsv[line, column, 2] = original_pixel_value + delta_value

        self.interactive_img = cv.cvtColor(self.interactive_img_hsv, cv.COLOR_HSV2BGR)
        cv.imshow(self.interactive_window_name, self.interactive_img)


    def set_kernel_size(self, value: int) -> None:
        self.kernel_size = 1 + 2*value

    
    def _get_kernel_avg(self, row: int, col: int, offset: int) -> int:
        hsv_sums = [0, 0, 0]
        for r in range(self.kernel_size):
            for c in range(self.kernel_size):
                x = row + r - offset
                y = col + c - offset
                for channel in range(3):
                    hsv_sums[channel] += int(self.interactive_img_hsv[x,y,channel])

        return [value // (self.kernel_size ** 2) for value in hsv_sums]


    def apply_avg_filter(self):
        offset = self.kernel_size // 2
        max_row = self.interactive_img.shape[0] - offset
        max_col = self.interactive_img.shape[1] - offset
        new_hsv_img = []
        for row in range(offset, max_row, self.kernel_size):
            new_hsv_img_row = []
            for col in range(offset, max_col, self.kernel_size):
                pixel = self._get_kernel_avg(row, col, offset)
                new_hsv_img_row.append(pixel)

            new_hsv_img.append(new_hsv_img_row)    
        self.filtered_source_img_hsv = array(new_hsv_img, dtype=uint8)
        self.filtered_source_img = cv.cvtColor(self.filtered_source_img_hsv, cv.COLOR_HSV2BGR)

        self.interactive_img = self.filtered_source_img.copy()
        self.interactive_img_hsv = self.filtered_source_img_hsv.copy()


    def _check_filter_dim(self):
        if (self.filtered_source_img.shape[0] < self.kernel_size or
            self.filtered_source_img.shape[1] < self.kernel_size):
            return False
        return True


    def manage_filters(self, event: int, x: int, y: int, flags: int, param: any) -> None:
        if event == cv.EVENT_LBUTTONDOWN and self._check_filter_dim():
            self.apply_avg_filter()
            cv.imshow(self.interactive_window_name, self.interactive_img)
            
        # Reset
        elif event == cv.EVENT_MBUTTONDOWN:
            self.filtered_source_img = self.source_img.copy()
            self.filtered_source_img_hsv = self.source_img_hsv.copy()

            self.interactive_img = self.filtered_source_img.copy()
            self.interactive_img_hsv = self.filtered_source_img_hsv.copy()
            self.update_brightness(self.brightness_trackbar_value)
            cv.imshow(self.interactive_window_name, self.interactive_img)


    def show_interactive_window(self) -> None:
        cv.namedWindow(self.interactive_window_name)
        cv.createTrackbar('Brightness variation', self.interactive_window_name, 256, 511, self.update_brightness)
        cv.createTrackbar('Filter Kernell Size', self.interactive_window_name, 1, 4, self.set_kernel_size)
        cv.imshow(self.interactive_window_name, self.interactive_img)
        cv.setMouseCallback(self.interactive_window_name, self.manage_filters)



class Histogram:
    def __init__(self, img: str | os.PathLike | ndarray) -> None:
        if isinstance(img, (str, os.PathLike)):
            img = load_img(img)

        self.source_window_name = "Histograms Source Image"
        self.rgb_window_name = "RGB Histograms"
        self.color_names = ["red", "green", "blue"]
        self.set_img(img)


    def set_img(self, new_img: ndarray) -> None:
        self.img = new_img.copy()
        self.upper_bound = 0


    def show_source_img(self) -> None:
        cv.imshow(self.source_window_name, self.img)


    def destroy_source_img_window(self) -> None:
        cv.destroyWindow(self.source_window_name)


    def get_hist(self, img: ndarray) -> ndarray:
        hist = [0 for i in range(256)]
        for line in img[:]:
            for pixel in line:
                hist[pixel] += 1

        max_count = max(hist)
        if self.upper_bound * 1.05 < max_count:
            self.upper_bound = max_count * 1.05
        return hist 


    def get_hist_fig(self, img: ndarray, color: str) -> plt.Figure:
        hist = self.get_hist(img)

        hist_fig, ax = plt.subplots(figsize=(8, 2.5), dpi=100)
        ax.plot(hist, color=color, linewidth=2, label=f'{color.capitalize()} Pixels Count')
        ax.set_xticks(arange(0, 255, 25))
        ax.set_xlim(0, 255)
        ax.set_ylim(0, self.upper_bound)
        ax.set_xlabel("Intensity")
        ax.set_ylabel("Count")
        ax.set_title(f'{color.capitalize()} Histogram')
        ax.grid(True)
        ax.legend(loc="upper right")
        
        hist_fig.tight_layout()
        return hist_fig


    def _fig_to_cv_img(self, fig: plt.Figure) -> ndarray:
        fig.canvas.draw()
        rgba = asarray(fig.canvas.buffer_rgba())
        bgr = cv.cvtColor(rgba, cv.COLOR_RGBA2BGR)
        plt.close(fig)  
        return bgr


    def show_rgb_hists(self) -> None:
        rgb_img = cv.cvtColor(self.img, cv.COLOR_BGR2RGB)
        rgb_channels = cv.split(rgb_img)

        hist_images = []
        for rgb_channel, color in zip(rgb_channels, self.color_names):
            fig = self.get_hist_fig(rgb_channel, color)
            cv_img = self._fig_to_cv_img(fig)
            hist_images.append(cv_img)

        combined_hists = vstack(hist_images)
        cv.imshow(self.rgb_window_name, combined_hists)


    def destroy_hists_windows(self) -> None:
        cv.destroyWindow(self.rgb_window_name)


    def wait_and_clear(self) -> None:
        cv.waitKey(0)
        self.destroy_source_img_window()
        self.destroy_hists_windows()

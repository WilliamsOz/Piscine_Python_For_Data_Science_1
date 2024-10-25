import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load
from PIL import Image
import sys
import os


def print_row_first_element(array, ind):
    """
    Print a formatted display of an 2D array given.

    Args :
        array (array) : The array to print.
        ind (int) : An int indicator to specifying the format:
                    0 for single bracket and 1 for triple brackets.
    """
    count = 0
    for row in array:
        count += 1
    length = count
    count = 0
    for row in array:
        if count == 0:
            if ind == 1:
                print("[[[", row[0], "]", sep="")
            else:
                print("[[", row[0], sep="")
        if count > 0 and count < 3 or count > length - 4:
            if ind == 1:
                if count == length - 1:
                    print("  [", row[0], "]]]", sep="")
                elif count < length - 1:
                    print("  [", row[0], "]", sep="")
            else:
                if count == length - 1:
                    print(row[0], "]]", sep="")
                else:
                    print(row[0], sep="")
        if count == 2:
            print("    ...")
        count += 1


def main():
    """
    Load an image, print some information and display it after zooming.
    """
    try:
        if len(sys.argv) != 2:
            raise AssertionError("Wrong number of parameter.")
        path = sys.argv[1]
        if not path.lower().endswith(("jpg", "jpeg")):
            raise AssertionError("Image must be jpg or jpeg extension.")
        if not os.path.exists(path):
            raise FileNotFoundError("Image not found", path)
        img = Image.open(path)
        if img is None:
            raise AssertionError("Failed to load image.")

        print_row_first_element(ft_load(path), 0)

        zoomed_image = img.crop((400, 100, 800, 500))
        zoomed_image.save("zoomed_image.jpg")
        print(f"New shape after slicing: {zoomed_image.size}")

        grayscale_image = zoomed_image.convert("L")
        print_row_first_element(np.array(grayscale_image), 1)

        plt.imshow(grayscale_image, cmap="gray")
        plt.title("Zoomed Image")
        plt.axis('on')
        plt.show()

    except Exception as error:
        print("\033[31m", Exception.__name__ + ":", error, "\033[0m")
    return 0


if __name__ == "__main__":
    main()

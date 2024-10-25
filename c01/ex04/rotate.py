from load_image import ft_load
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
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
    Load an image, cut a square part from it and transpose it.
    It should display it, print the new shape, and the data of the image
    after the transpose.
    """
    try:
        if len(sys.argv) != 2:
            raise AssertionError("Wrong number of argument.")
        path = sys.argv[1]
        if not path.lower().endswith(("jpg", "jpeg")):
            raise AssertionError("Image must be jpg or jpeg extension.")
        if not os.path.exists(path):
            raise FileNotFoundError("Image not found", path)
        img = Image.open(path)
        if img is None:
            raise AssertionError("Failed to load image.")

        square_crop_img = img.crop((400, 100, 800, 500))
        square_crop_img.save("square_crop.jpg")
        print(f"The shape of image is: {square_crop_img.size}")

    except Exception as error:
        print(Exception.__name__ + ":", error)
        exit(1)
    return


if __name__ == "__main__":
    main()

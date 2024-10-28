import numpy as np
from PIL import Image
import os


def print_row_first_element(array):
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
            print("[[", row[0], sep="")
        if count > 0 and count < 3 or count > length - 4:
            if count == length - 1:
                print("  ", row[0], "]]", sep="")
            elif count < length - 1:
                print("  ", row[0], sep="")
            else:
                if count == length - 1:
                    print(row[0], sep="")
                else:
                    print(row[0], sep="")
        if count == 2:
            print("    ...")
        count += 1
    print("    ...")


def ft_load(path: str) -> np.ndarray:
    """
    Load an image from path given and convert it as 2D array.

    Args :
        path (str) : the path to the image.

    Returns the 2D array converted from the given image.
    """
    try:
        if not path.lower().endswith(("jpg", "jpeg")):
            raise AssertionError("Image must be jpg or jpeg extension.")
        if not os.path.exists(path):
            raise FileNotFoundError("Image not found", path)

        img = Image.open(path)

        print(f"The shape of image is: (\
{img.size[1]}, {img.size[0]}, {img.layers})")
        print_row_first_element(np.array(img))

        return np.array(img)

    except Exception as error:
        print("\033[31m", Exception.__name__ + ":", error, "\033[0m")
        exit(1)

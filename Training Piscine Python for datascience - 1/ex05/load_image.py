import numpy as np
from PIL import Image
import os


def trim(array, x, y, width, height, depth=3):
    """
        Trim an array using the given parameters

        Args :
            array : The array to trim.
            x and y : Coordinate of the upper left point of the
            rectancle to be cut.
            width : Width of the rectangle.
            height : Height of the rectangle.
            depth : Depth of the color, numbers of layers, 3 is for RGB.

        Returns :
            Return a sub part of array defined by parameters given.
    """
    return array[y:y+width, x:x+height, :depth]


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

        print(np.array(img))

        return np.array(img)

    except Exception as error:
        print("\033[31m", Exception.__name__ + ":", error, "\033[0m")
        exit(1)

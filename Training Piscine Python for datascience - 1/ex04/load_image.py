import numpy as np
from PIL import Image
import os


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

        return np.array(img)

    except Exception as error:
        print("\033[31m", Exception.__name__ + ":", error, "\033[0m")
        exit(1)

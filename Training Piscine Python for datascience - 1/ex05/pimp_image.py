import numpy as np
from PIL import Image


def ft_invert(array) -> np.ndarray:
    """Inverts the color of the image received."""
    # Substract every pixel by 255 to invert color of pixel.
    image = 255 - array
    Image.fromarray(image).show()

    return image


def ft_red(array) -> np.ndarray:
    """Keeps only the red color channel of the image."""
    # Extract red canal.
    red_channel = array[:, :, 0]
    # Create an array of 0
    image = np.zeros_like(array)
    # Fill the red canal with the extract value, leaving green and
    # blue canal to 0.
    image[:, :, 0] = red_channel
    Image.fromarray(image).show()

    return image


def ft_green(array) -> np.ndarray:
    """Keeps only the green color channel of the image."""
    # Extract green canal.
    green_channel = array[:, :, 1]
    image = array.copy()
    # Put red canals to 0.
    image[:, :, 0] = 0
    # Put blue canals to 0.
    image[:, :, 2] = 0
    image[:, :, 1] = green_channel
    Image.fromarray(image).show()

    return image


def ft_blue(array) -> np.ndarray:
    """Keeps only the blue color channel of the image."""
    # Extract blue canal.
    blue_channel = array[:, :, 2]
    # Create new array fill with 0.
    image = np.zeros_like(array)
    # Fill the blue canal with extracted value, leaving red and green
    # canals to 0.
    image[:, :, 2] = blue_channel
    Image.fromarray(image).show()

    return image


def ft_grey(array) -> np.ndarray:
    """Converts the image to grayscale."""
    # Divide every canals by 3 to obtains grey intensity.
    red_channel = array[:, :, 0] / 3
    green_channel = array[:, :, 1] / 3
    blue_channel = array[:, :, 2] / 3
    # Sums of 3 values to obtains grey value.
    grey_channel = red_channel + green_channel + blue_channel
    grey_image = np.stack([grey_channel, grey_channel, grey_channel], axis=2)
    Image.fromarray(grey_image.astype(np.uint8)).show()

    return grey_image

import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


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


def main():
    """
    Load an image, print some information and display it after zooming.
    """
    try:
        try:
            image = ft_load('animal.jpeg')
        except Exception as error:
            print(error)
            exit(1)

        print(image)

        image = trim(image, 450, 100, 400, 400, 1)

        print(f'New shape after slicing: {image.shape}', end='')
        print(f' or ({image.shape[0]}, {image.shape[1]})')
        print(image)

        # Erase the 3D dimension (depth) and convert the image to 2D
        # for the grayscale display.
        image = np.squeeze(image)
        # Display image in grayscale.
        plt.imshow(image, cmap='gray')
        plt.title("Zoomed Image")
        plt.axis('on')
        plt.show()

    except Exception as error:
        print("\033[31m", Exception.__name__ + ":", error, "\033[0m")
    return 0


if __name__ == "__main__":
    main()

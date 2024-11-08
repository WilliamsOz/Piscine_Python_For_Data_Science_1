from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


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


def rotate(array):
    """
        Rotate an array

        Args :
            array : the array to rotate.

        Returns :
            The rotated array.
    """
    # Transpose the array, convert tuple as list, reverse the order to
    # rotate the image and convert as 2D array.
    return np.asarray(list(list(x) for x in zip(*array))[::-1])


def main():
    """
    Load an image, cut a square part from it and transpose it.
    It should display it, print the new shape, and the data of the image
    after the transpose.
    """
    try:
        try:
            image = ft_load('animal.jpeg')
        except Exception as error:
            print(error)
            exit(1)

        image = trim(image, 450, 100, 400, 400, 1)
        print(f'The shape of the image is: {image.shape}', end='')
        print(f' or ({image.shape[0]}, {image.shape[1]})')
        print(image)

        image = rotate(image)

        print(f'New shape after Transpose: ({image.shape[0]}, \
{image.shape[1]})')
        # Display only the first layer of array.
        print(image[:, :, 0])

        image = np.squeeze(image)
        plt.imshow(image, cmap='gray')
        plt.title("Transposed Image")
        plt.axis('on')
        plt.show()

    except Exception as error:
        print(Exception.__name__ + ":", error)
        exit(1)
    return


if __name__ == "__main__":
    main()

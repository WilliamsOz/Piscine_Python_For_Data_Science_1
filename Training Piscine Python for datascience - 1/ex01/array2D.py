import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Truncate an array of 2D and print the shape before and after the truncate.

    Args :
        family (list) : The 2D array to be truncated.
        start (int) : The beginning of truncate.
        end (int) : The end of truncate.

    Returns :
        Trucated version of the 2D array.
    """
    try:
        if not family:
            raise AssertionError("Empty 2D array.")
        if not isinstance(family, list):
            raise TypeError("Arguments must be a 2D array.")
        if not all(isinstance(n, (int, float)) for row in family for n in row):
            raise TypeError("Values in 2D array must be integer or float.")
        if start >= len(family):
            raise ValueError("The start can't be greater or equal than \
the size of 2D array.")
        if not isinstance(start, int) or not isinstance(end, int):
            raise TypeError("The start and end values must be integer.")
        len_item = len(family[0])
        for item in family:
            if len_item != len(item):
                raise AssertionError("List in 2D array are not same size.")

        arr = np.array(family)

        print(f"My shape is : {np.array(family).shape}")
        print(f"My new shapes is : {arr[start:end].shape}")

        arr = arr[start:end].tolist()

    except Exception as error:
        print("\033[31m", Exception.__name__ + ":", error, "\033[0m")
        exit(1)

    return arr

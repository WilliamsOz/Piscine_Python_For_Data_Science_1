import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float])\
        -> list[int | float]:
    """
    Give the list of Body Mass Index.

    Args :
        height (list of int or float) : List of height in meter.
        weight (list of int or float) : List of weight in kg.

    Returns :
        Return the list of BMI (weight/height²)
    """
    try:
        if len(height) != len(weight) or not height or not weight:
            raise ValueError("List of arguments must have same size.")

        if not isinstance(height, list) or\
                not isinstance(weight, list):
            raise TypeError("Arguments must be a list of int or float.")

        for h, w in zip(height, weight):
            if not isinstance(h, int) and not isinstance(h, float) or\
                    not isinstance(w, int) and not isinstance(w, float):
                raise TypeError("List must contains only int or float.")

        for h, w in zip(height, weight):
            if h <= 0 or w <= 0:
                raise ValueError("Arguments must be positive.")

        if not all(isinstance(n, (int, float)) for n in height) or\
                not all(isinstance(n, (int, float)) for n in weight):
            raise TypeError("Arguments must be int or float.")

        np_height = np.array(height)
        np_weight = np.array(weight)
        bmi = np_weight / (np_height**2)

        tab = []
        for item in bmi:
            tab.append(float(item))

    except Exception as error:
        print("\033[91mError :", error, "\033[0m")
        exit(1)
    return tab


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Return a list of booleans based on BMI and limit.

    Args:
        bmi (list of int or float) : BMI to check.
        limit (int) : Limit BMI not to exceed.

    Returns :
        Return True if the limit is exceed and False otherwise.
    """
    try:
        if not isinstance(bmi, list) or\
                not all(isinstance(n, int) for n in bmi) and\
                not all(isinstance(n, float) for n in bmi) or\
                not isinstance(limit, int):
            raise TypeError("All arguments must be int or float.")

        tab = []
        for item in bmi:
            tab.append(item > limit)

    except Exception as error:
        print("\033[91mError :", error, "\033[0m")
        exit(1)
    return tab

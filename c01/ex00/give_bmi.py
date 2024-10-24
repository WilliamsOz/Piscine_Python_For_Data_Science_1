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
        if not height or not weight or\
            not isinstance(height, list) or\
                not isinstance(weight, list):
            raise AssertionError("Arguments must be a list of int or float.")

        if len(height) != len(weight):
            raise AssertionError("List of arguments must have same size.")

        if not all(isinstance(n, int) for n in height) and\
                not all(isinstance(n, float) for n in height) or\
                not all(isinstance(n, int) for n in weight) and\
                not all(isinstance(n, float) for n in weight):
            raise AssertionError("Arguments must be int or float.")

        np_height = np.array(height)
        np_weight = np.array(weight)
        bmi = np_weight / (np_height**2)

        tab = []
        for item in bmi:
            tab.append(float(item))

    except ValueError as error:
        print(ValueError.__name__ + ":", error)
        exit(1)
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)
        exit(1)
    return tab


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Return a list of booleans based on BMI and limit.

    Args:
        bmi (list of int or float) : BMI to check.
        limit (int) : Limit BMI not to exceed.

    Returns :
        Return True or False is the BMI limit is exceed.
    """
    try:
        if not isinstance(bmi, list) or\
                not all(isinstance(n, int) for n in bmi) and\
                not all(isinstance(n, float) for n in bmi) or\
                not isinstance(limit, int):
            raise AssertionError("Arguments type error.")

        tab = []
        for item in bmi:
            tab.append(item > limit)

    except ValueError as error:
        print(ValueError.__name__ + ":", error)
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)
    return tab

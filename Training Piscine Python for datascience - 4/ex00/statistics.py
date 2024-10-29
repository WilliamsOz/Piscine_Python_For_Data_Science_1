from typing import Any


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """
    Calculs various statistical mesure as Mean, Median, Quartile
    Standard Deviation and Variance according to the **kwargs ask.

    Args :
        args (Any) : Variable number of positional arguments
    representing values for calculations.
        kwargs (Any) : Keyword arguments indicating the
    requested statistical measures for printing.

    Returns :
        The function return None.
        It prints the requested statistical measures.

    Notes :
        The function calculate the mean, median, quartile,
        standard deviation and variancebased on the provided arguments.
    """
    args_list = list(args)
    if not args_list:
        for i in kwargs.values():
            print("ERROR")
        return

    mean = sum(args_list) / len(args_list)
    sorted_list = sorted(args_list)
    median = sorted_list[int(len(args_list) / 2)]
    quart_25 = (int(len(sorted_list)) - 1) * 0.25
    quart_75 = (int(len(sorted_list)) - 1) * 0.75
    quartile_25 = sorted_list[int(quart_25)]
    quartile_75 = sorted_list[int(quart_75)]
    quartile_dict = [float(quartile_25), float(quartile_75)]
    var = sum((x - mean) ** 2 for x in sorted_list) / len(sorted_list)
    std = var ** 0.5

    for i in kwargs.values():
        if i == "mean":
            print("mean :", mean)
        elif i == "median":
            print("median :", median)
        elif i == "quartile":
            print("quartile :", quartile_dict)
        elif i == "std":
            print("std :", std)
        elif i == "var":
            print("var :", var)

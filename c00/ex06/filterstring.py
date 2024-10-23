import sys
from ft_filter import ft_filter


def main():
    """
    Take 2 argument :
    1. a string
    2. an integer

    Return a list of words that are greater than the integer given.
    """
    try:
        arg1 = sys.argv[1]
        if len(sys.argv) != 3 or not isinstance(arg1, str):
            raise AssertionError("the arguments are bad")

        arg2 = sys.argv[2]
        try:
            arg2 = int(arg2)
        except AssertionError as error:
            print(AssertionError.__name__ + ":", error)
            sys.exit(1)

        filtered_list = \
            list(ft_filter((lambda word: len(word) > arg2), arg1.split()))

        print(filtered_list)

    except ValueError as error:
        print(ValueError.__name__ + ":", error)
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)

    return 0


if __name__ == "__main__":
    main()

import sys
from string import punctuation


def n_lower_chars(string):
    """"
    Return number of lower char in string.
    """
    return sum(1 for c in string if c.islower())


def n_upper_chars(string):
    """"
    Return number of upper char in string.
    """
    return sum(1 for c in string if c.isupper())


def n_punc_chars(string):
    """"
    Return number of punctuation in string.
    """
    count = 0
    for i in range(0, len(string)):
        if string[i] in punctuation:
            count += 1
    return count


def n_space_chars(string):
    """"
    Return number of spaces in string.
    """
    return sum(1 for char in string if char.isspace())


def n_digit_chars(string):
    """"
    Return number of digits in string.
    """
    return sum(1 for c in string if c.isdigit())


def get_data(string):
    """"
    Get composition data of string.

    Return data as a dictionary.
    """
    data = {}
    data["len"] = len(string)
    data["upper_chars"] = n_upper_chars(string)
    data["lower_chars"] = n_lower_chars(string)
    data["punct_chars"] = n_punc_chars(string)
    data["space_chars"] = n_space_chars(string)
    data["digit_chars"] = n_digit_chars(string)
    return data


def print_data(data):
    """
    Print the composition of the string.
    """
    print("The text contains", data["len"], "characters:")
    print(data["upper_chars"], "upper letters")
    print(data["lower_chars"], "lower letters")
    print(data["punct_chars"], "punctuation marks")
    print(data["space_chars"], "spaces")
    print(data["digit_chars"], "digits")


def main():
    """"
    Analyzes the given text and print its char composition.

    Ask for input if no input is given.
    """
    try:
        data = {}
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
        elif len(sys.argv) == 1:
            print("What is the text to count?")
            string = sys.stdin.readline()
            data = get_data(string)
        else:
            data = get_data(sys.argv[1])
        print_data(data)
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)
        exit(1)
    return 0


if __name__ == "__main__":
    main()

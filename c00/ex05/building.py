import sys
from string import punctuation


def catch_input():
    str = input("What is the text to count?\n")
    return str


def n_lower_chars(string):
    return sum(1 for c in string if c.islower())


def n_upper_chars(string):
    return sum(1 for c in string if c.isupper())


def n_punc_chars(string):
    print("CCCCC", str(string).count(punctuation))
    return 1


def get_data(str):
    data = {}
    data["len"] = len(str)
    data["upper_chars"] = n_upper_chars(str)
    data["lower_chars"] = n_lower_chars(str)
    data["punct_chars"] = n_punc_chars(str)
    return data


def main():
    try:
        data = {}
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
        elif len(sys.argv) == 1:
            str = catch_input()
            data = get_data(str)
        else:
            data = get_data(sys.argv[1])
        print(data["len"])
        print(data["upper_chars"])
        print(data["lower_chars"])
        print(data["punct_chars"])
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)
        exit(1)
    return 0


if __name__ == "__main__":
    main()

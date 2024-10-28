import sys


MORSE_CODE_DICT = {' ': '/ ', 'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}


def forbidden_char(string):
    """
    Take a string and check if there is a forbidden char.

    Return True if there is a forbidden char and false otherwise.
    """
    special_char = " ,.?/-()"

    if not string:
        return True

    for char in string:
        if not (char.isalnum() or char in special_char):
            return True

    return False


def main():
    """
    Convert a string into a morse string and print it.
    """
    try:
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are bad")
        if forbidden_char(sys.argv[1]):
            raise AssertionError("the arguments are bad")
        string = str(sys.argv[1]).upper()
        string = string
        morse_string = []
        for char in string:
            morse_string.append(MORSE_CODE_DICT[char])
        print(' '.join(morse_string))
    except ValueError as error:
        print(ValueError.__name__ + ":", error)
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)
    return


if __name__ == "__main__":
    main()

from ft_filter import ft_filter


def is_even(n):
    return n % 2 == 0


def is_odd(n):
    return n % 2


def test_filter():
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    string = ["pomme", "banane", "peche", "kiwi", "fruit de la passion"]
    mixed = [1, "pomme", 2.21, 2, "banane", 3, "peche", 4.42]

    print("Test for even numbers:")
    even_numbers = ft_filter(is_even, num)
    assert list(even_numbers) == [2, 4, 6, 8, 10], \
        "\033[91mTest failed..\033[0m"
    print("\033[92mTest succeed!\033[0m")

    print("Test for odd numbers:")
    odd_numbers = ft_filter(is_odd, num)
    assert list(odd_numbers) == [1, 3, 5, 7, 9], \
        "\033[91mTest failed..\033[0m"
    print("\033[92mTest succeed!\033[0m")

    print("Test for numbers greater than 5:")
    greater_than_5 = ft_filter(lambda x: x > 5, num)
    assert list(greater_than_5) == [6, 7, 8, 9, 10], \
        "\033[91mTest failed..\033[0m"
    print("\033[92mTest succeed!\033[0m")

    print("Test for strings greater than 5:")
    long_strings = ft_filter(lambda x: len(x) > 5, string)
    assert list(long_strings) == ["banane", "fruit de la passion"], \
        "\033[91mTest failed..\033[0m"
    print("\033[92mTest succeed!\033[0m")

    print("Test for integer:")
    is_integer = ft_filter(lambda x: isinstance(x, int), mixed)
    assert list(is_integer) == [1, 2, 3], \
        "\033[91mTest failed..\033[0m"
    print("\033[92mTest succeed!\033[0m")

    print("Test for float:")
    is_floats = ft_filter(lambda x: isinstance(x, float), mixed)
    assert list(is_floats) == [2.21, 4.42], \
        "\033[91mTest failed..\033[0m"
    print("\033[92mTest succeed!\033[0m")

    print("\033[93mEnd of test.\033[0m")


test_filter()

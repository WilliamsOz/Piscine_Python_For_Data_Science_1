def ft_filter(func, it):
    """
    ft_filter(function or None, iterable) --> filter object

    Return an iterator yielding those items of iterable for which
    function(item) is true.
    If function is None, return the items that are true.
    """
    if not func:
        return (item for item in it if item)
    else:
        return (item for item in it if func(item))


def count_in_list(lst: list, s: str):
    """
        Return the number of occurence of s in the list
    """
    return len(list(ft_filter(lambda x: x == s, lst)))

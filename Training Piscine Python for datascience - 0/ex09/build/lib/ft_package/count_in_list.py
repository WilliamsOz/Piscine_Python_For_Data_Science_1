
def count_in_list(list, value):
    """
    Find number of occurence value in list.

    Args :
        list : the list to look in.
        value: the element to find in list.

    Returns :
        Number of element in list.
    """
    count = 0

    if list:
        for item in list:
            if item == value:
                count += 1

    return count

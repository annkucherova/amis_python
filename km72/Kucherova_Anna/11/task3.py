def opposite(list):

    if len(list) == 1:
        return list
    else:
        return opposite(list[1:]) + [list[0]]
    
    """
    This function revers the list

    Args:
        list: list of numbers

    Returns:
        opposite: list of int numbers

    Raises:
        ValueError

    Examples:
        l = [9, 45, 1, 3]
        >>> print(min_elem(l))
        "Data is correct"
        "3, 1, 45, 9"

        l = [0, 8, 'c', 7]
        >>> print(min_elem(l))
        Traceback (most recent call last):
            ...
        ValueError
    """


list1 = [int(elem) for elem in input("Введіть список: ").split()]

print(opposite(list1))

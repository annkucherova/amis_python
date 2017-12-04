def minElement(list):
    if len(list) == 1:
        return list[0]
    list1 = list[1:]
    min = minElement(list1)
    if min > list[0]:
        min = list[0]
    return min

    """
    This function find min element of list

    Args:
        list: list of numbers

    Returns:
        min element: float number

    Raises:
        ValueError

    Examples:
        list = [9, 45, 1, 3]
        >>> print(minElement(list))
        "Data is correct"
        "1"

        list = [0, 8, 'c', 7]
        >>> print(minElement(list))
        Traceback (most recent call last):
            ...
        ValueError
    """


list = [int(elem) for elem in input("Введіть список чисел: ").split()]

print(minElement(list))


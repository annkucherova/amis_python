def bigger2(list, element, max1, max2):
    if element < len(list):
        if list[element] > max1:
            max2 = max1
            max1 = list[element]
        elif list[element] > max2:
            max2 = list[element]
        return bigger2(list, element + 1, max1, max2)
    else:
        return max2

    """
    This function find the second biggest element of the list

    Args:
        list: list of numbers

    Returns:
        biggest elem: float number

    Raises:
        ValueError

    Examples:
        list = [9, 45, 1, 3]
        >>> print(minElement(list))
        "Data is correct"
        "9"

        list = [0, 8, 'c', 7]
        >>> print(minElement(list))
        Traceback (most recent call last):
            ...
        ValueError
    """


list1 = [int(x) for x in input("Введіть список натуральних чисел: ").split()]

print(bigger2(list1, 0, 0, 0))

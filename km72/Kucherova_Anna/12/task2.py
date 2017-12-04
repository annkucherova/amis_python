def quantity(list1, elem, max1):
    if elem < len(list1):
        if list1[elem] > max1:
            max1 = list1[elem]
        return quantity(list1, elem + 1, max1)
    else:
        return max1


def quantity2(list1, elem, maxx, i):
    if elem < len(list1):
        if list1[elem] == maxx:
            i = i + 1
        return quantity2(list1, elem + 1, maxx, i)
    else:
        return i

        """
    This functions find quantity of repeating elements of the list

    Args:
        list: list of numbers

    Returns:
        quantity: int number

    Raises:
        ValueError

    Examples:
        list = [9, 45, 1, 1, 3]
        >>> print(minElement(list))
        "Data is correct"
        "2"

        list = [0, 8, 'c', 7]
        >>> print(minElement(list))
        Traceback (most recent call last):
            ...
        ValueError
    """


list1 = [int(x) for x in input("Введіть список натуральних чисел: ").split()]
print(quantity2(list1, 0, quantity(list1, 0, 0), 0))

def merge_two_lists(list1, list2):
    """
    Сливает два отсортированных связанных списка, представленных в виде кортежей (val, next),
    в один отсортированный список.

    >>> l1 = (1, (2, (4, None)))
    >>> l2 = (1, (3, (4, None)))
    >>> merge_two_lists(l1, l2)
    (1, (1, (2, (3, (4, (4, None))))))

    >>> merge_two_lists(None, None) is None
    True

    >>> l3 = (0, None)
    >>> merge_two_lists(None, l3)
    (0, None)
    """
    pass


if __name__ == '__main__':
    import doctest
    doctest.testmod()
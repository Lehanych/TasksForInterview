def group_anagrams(words):
    """
    Группирует слова, являющиеся анаграммами друг друга.

    >>> words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    >>> # Результат может содержать списки в разном порядке, поэтому проверим по длине и содержимому
    >>> sorted([sorted(group) for group in group_anagrams(words)])
    [['ate', 'eat', 'tea'], ['bat'], ['nat', 'tan']]

    >>> group_anagrams(["a"])
    [['a']]

    >>> group_anagrams([])
    []
    """
    pass


if __name__ == '__main__':
    import doctest
    doctest.testmod()
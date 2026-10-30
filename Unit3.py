# Конструктор
def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch)
    return [label] + list(branches)

# Селекторы
def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def tree_max(t):
    """Возвращает наибольший элемент дерева.
    >>> t = tree(4, [tree(2, [tree(1)]), tree(10)])
    >>> tree_max(t)
    10
    """
    pass

def find_path(tree, x):
    """
    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])]), tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 6)
    [2, 7, 6]
    >>> find_path(t, 10)
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)
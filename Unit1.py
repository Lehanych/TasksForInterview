def total_by_customer(orders):
    """
    Возвращает словарь {имя_клиента: общая сумма его заказов}.
    Клиенты без заказов в результат не попадают.
    Заказы с отрицательной суммой игнорируются.

    >>> orders = [
    ...     {'customer': 'Анна', 'amount': 500},
    ...     {'customer': 'Борис', 'amount': 300},
    ...     {'customer': 'Анна', 'amount': 200},
    ... ]
    >>> total_by_customer(orders)
    {'Анна': 700, 'Борис': 300}

    >>> # Проверка игнорирования отрицательных сумм
    >>> orders_with_negatives = [
    ...     {'customer': 'Иван', 'amount': 1000},
    ...     {'customer': 'Иван', 'amount': -150},
    ...     {'customer': 'Мария', 'amount': -50},
    ... ]
    >>> total_by_customer(orders_with_negatives)
    {'Иван': 1000}

    >>> # Проверка пустого списка заказов
    >>> total_by_customer([])
    {}
    """
    pass


if __name__ == '__main__':
    import doctest
    doctest.testmod()
def dedupe(employees):
    """
    Убирает дубликаты сотрудников по email. 
    Из дубликатов оставляет запись с наибольшей зарплатой.
    Сохраняет порядок первых появлений email.
    Возвращает новый список, не изменяя исходный.

    >>> employees = [
    ...     {'email': 'a@x.com', 'name': 'Анна', 'salary': 100},
    ...     {'email': 'b@x.com', 'name': 'Борис', 'salary': 120},
    ...     {'email': 'a@x.com', 'name': 'Анна', 'salary': 150},
    ... ]
    >>> result = dedupe(employees)
    >>> result
    [{'email': 'a@x.com', 'name': 'Анна', 'salary': 150}, {'email': 'b@x.com', 'name': 'Борис', 'salary': 120}]
    >>> # Убедимся, что исходный список не изменился
    >>> employees[0]['salary']
    100
    """
                
    pass


if __name__ == '__main__':
    import doctest
    doctest.testmod()
import types

"""
Доработать функцию flat_generator. Должен получиться генератор, который принимает список списков и возвращает их 
плоское представление. Функция test в коде ниже также должна отработать без ошибок.\
"""


def flat_generator(list_of_lists):
    list_length = 0
    list_depth = 0
    list_of_lists_len = len(list_of_lists)

    while list_of_lists_len != list_depth:
        yield list_of_lists[list_depth][list_length]
        if len(list_of_lists[list_depth]) - 1 == list_length:
            list_depth += 1
            list_length = 0
        else:
            list_length += 1


def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()

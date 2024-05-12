import types

"""
Необязательное задание. Написать генератор, аналогичный генератору из задания 2, но обрабатывающий списки с любым 
уровнем вложенности. Шаблон и тест в коде ниже:
"""


def flat_generator(list_of_list):
    list_length = 0
    list_depth = 0
    list_cursor = 0
    list_of_lists_len = len(list_of_list)

    while list_of_lists_len != list_depth:
        current_item = list_of_list[list_depth][list_length]
        item = current_item

        while isinstance(item, list):
            if len(item) == 0:
                return
            else:
                item = item[list_cursor]

        yield item
        if isinstance(current_item, list) and len(current_item) - 1 > list_cursor:
            list_cursor += 1
        elif len(list_of_list[list_depth]) - 1 == list_length:
            list_depth += 1
            list_length = 0
            list_cursor = 0
        else:
            list_length += 1
            list_cursor = 0


def test_4():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)


if __name__ == '__main__':
    test_4()

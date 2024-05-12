"""
Необязательное задание. Написать итератор, аналогичный итератору из задания 1,
но обрабатывающий списки с любым уровнем вложенности. Шаблон и тест в коде ниже:
"""


class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.len_list_of_list = len(list_of_list)

    def __iter__(self):
        self.cursor = 0
        self.list_length = 0
        self.list_depth = 0
        return self

    def __next__(self):
        if self.len_list_of_list <= self.list_depth:
            raise StopIteration

        current_item = self.list_of_list[self.list_depth][self.list_length]
        item = current_item

        while isinstance(item, list):
            if len(item) == 0:
                raise StopIteration
            else:
                item = item[self.cursor]

        if isinstance(current_item, list) and len(current_item) - 1 > self.cursor:
            self.cursor += 1
        elif len(self.list_of_list[self.list_depth]) - 1 <= self.list_length:
            self.list_depth += 1
            self.list_length = 0
            self.cursor = 0
        else:
            self.list_length += 1
            self.cursor = 0

        return item


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()

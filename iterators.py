
"""
Доработать класс FlatIterator в коде ниже. Должен получиться итератор, который принимает список списков и
возвращает их плоское представление, т. е. последовательность, состоящую из вложенных элементов. Функция test в коде
ниже также должна отработать без ошибок.
"""


class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.len_list_of_list = len(list_of_list)

    def __iter__(self):
        self.list_length = 0
        self.list_depth = 0
        return self

    def __next__(self):
        if self.len_list_of_list <= self.list_depth:
            raise StopIteration
        item = self.list_of_list[self.list_depth][self.list_length]
        if len(self.list_of_list[self.list_depth]) - 1 <= self.list_length:
            self.list_depth += 1
            self.list_length = 0
        else:
            self.list_length += 1
        return item


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()

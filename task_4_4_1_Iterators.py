# -*- coding: utf-8 -*-

class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.index = -1

    def __iter__(self):
        self.next_list = []
        return self

    def __next__(self):
        # print(self.index, self.list_of_list)
        if not self.next_list:
            # next_nested_list iterated_list - Вложенный и Итерируемый, Следующий и (previous) Предыдущий
            self.index += 1
            if self.index == len(self.list_of_list):
                raise StopIteration
            # self.next_list = list(self.list_of_list[self.index])
            self.next_list = self.list_of_list[self.index][:]
            print(type(self.list_of_list[self.index]), isinstance(self.list_of_list[self.index], list))
            print(self.index, self.next_list)
        return self.next_list.pop(0)  # IndexError: pop from empty list - "pop из пустого списка"


def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    print(f'\nlist_of_lists_1: {list_of_lists_1}\n')
    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        print(flat_iterator_item, check_item)
        assert flat_iterator_item == check_item

    print(f'\nlist_of_lists_1: {list_of_lists_1}\n')

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()

    print('\n  -- Конец --  ')  # - Для блокнота

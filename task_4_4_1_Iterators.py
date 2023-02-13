# -*- coding: utf-8 -*-
#                       Итераторы и генераторы.
#       Задача 1. Получить итератор, который принимает список списков и возвращает его плоское представление.

from typing import Any, List


class FlatIterator:

    def __init__(self, list_of_list: List[List[Any]]) -> None:
        """Создаёт объект обрабатываемого списка."""
        self.list_of_list: List[List[Any]] = list_of_list
        self.index: int
        self.next_list: List[Any] = []

    def __iter__(self) -> Any:
        """Подготавливает список для обработки в цикле."""
        self.index = -1
        self.next_list = []
        return self

    def __next__(self) -> Any:
        """Выполняет одну итерацию из цикла, возвращает одно значение из списка."""
        if not self.next_list:
            self.index += 1
            if self.index >= len(self.list_of_list):
                raise StopIteration
            # self.next_list = list(self.list_of_list[self.index])    # 1) Тоже работает.
            self.next_list = self.list_of_list[self.index][:]  # 2)
        return self.next_list.pop(0)


def test_1():
    list_of_lists_1: List[List[Any]] = [
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

    print(f'\nlist_of_lists_1: {list_of_lists_1}')

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()

    print('\n  -- Конец --  ')  # - Для блокнота

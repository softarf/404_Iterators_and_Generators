# -*- coding: utf-8 -*-
#                       Итераторы и генераторы.
#       Задача 2. Получить генератор, который принимает список списков и возвращает его плоское представление.

from typing import Any, List

import types


def flat_generator(list_of_lists: List[List[Any]]) -> Any:
    """Возвращает одно, очередное, значение из списка."""
    index: int = 0
    next_list: List[Any] = []
    while index < len(list_of_lists):
        if not next_list:
            next_list = list_of_lists[index][:]
        yield next_list.pop(0)
        if not next_list:
            index += 1


def test_2():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    print(f'\nlist_of_lists_1: {list_of_lists_1}\n')

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        print(flat_iterator_item, check_item)
        assert flat_iterator_item == check_item

    print(f'\nlist_of_lists_1: {list_of_lists_1}')

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()

    print('\n  -- Конец --  ')  # - Для блокнота

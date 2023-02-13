# -*- coding: utf-8 -*-
#                       Итераторы и генераторы.
#       Задача 4. Получить генератор, который принимает список со списками
#                 произвольной вложенности и возвращает его плоское представление.

from typing import Any, List, Tuple
from copy import deepcopy

import types


def clear_empty_lists(work_list: List[Any], level: int) -> Tuple[List[Any], int]:
    """Удаляет вложенные опустевшие списки."""
    while level >= 0 and not work_list[level]:
        work_list.pop()    # .pop(self.level)
        level -= 1
    return work_list, level


def flat_generator(list_of_list: List[Any]) -> Any:
    """Возвращает одно, очередное, значение из списка."""
    index: int = 0
    level: int = -1
    work_list: List[Any] = []
    while index < len(list_of_list):
        if not work_list:
            work_list.append(deepcopy(list_of_list[index]))
            level += 1
        interim_element: Any = work_list[level].pop(0)
        while isinstance(interim_element, list):
            if interim_element:
                work_list.append(interim_element)
                level += 1
                interim_element = work_list[level].pop(0)
            else:
                if work_list[level]:
                    interim_element = work_list[level].pop(0)
                else:
                    work_list, level = clear_empty_lists(work_list, level)
                    if level >= 0 or index < len(list_of_list) - 1:
                        interim_element = work_list[level].pop(0)
                    else:
                        break
        if interim_element != []:
            yield interim_element
        work_list, level = clear_empty_lists(work_list, level)
        if not work_list:
            index += 1


def test_4():

    list_of_lists_2 = [
        [['a', []], ['b', [], 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]


    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        print(flat_iterator_item, check_item)
        assert flat_iterator_item == check_item


    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)


if __name__ == '__main__':
    test_4()

    print('\n  -- Конец --  ')  # - Для блокнота

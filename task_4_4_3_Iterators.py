# -*- coding: utf-8 -*-
#                       Итераторы и генераторы.
#       Задача 3. Получить итератор, который принимает список со списками
#                 произвольной вложенности и возвращает его плоское представление.

from typing import Any, List
from copy import deepcopy


class FlatIterator:

    def __init__(self, list_of_lists: List[Any]) -> None:
        """Создаёт объект обрабатываемого списка."""
        self.list_of_lists: List[Any] = list_of_lists
        self.work_list: List[Any] = []
        self.idx: int
        self.level: int

    def clear_empty_lists(self) -> None:
        """Удаляет вложенные опустевшие списки."""
        while self.level >= 0 and not self.work_list[self.level]:
            self.work_list.pop()    # .pop(self.level)
            self.level -= 1

    def __iter__(self) -> Any:
        """Подготавливает список для обработки в цикле."""
        self.idx = -1
        self.level = -1
        self.work_list = []
        return self

    def __next__(self) -> Any:
        """Выполняет одну итерацию из цикла, возвращает одно значение из списка."""
        if not self.work_list:
            self.idx += 1
            if self.idx >= len(self.list_of_lists):
                raise StopIteration
            self.work_list.append(deepcopy(self.list_of_lists[self.idx]))
            self.level += 1
        interim_element: Any = self.work_list[self.level].pop(0)
        while isinstance(interim_element, list):
            if interim_element:
                self.work_list.append(interim_element)
                self.level += 1
                interim_element = self.work_list[self.level].pop(0)
            else:
                if self.work_list[self.level]:
                    interim_element = self.work_list[self.level].pop(0)
                else:
                    self.clear_empty_lists()
                    if self.level < 0 and self.idx >= len(self.list_of_lists) - 1:
                        raise StopIteration
                    else:
                        interim_element = self.work_list[self.level].pop(0)
        self.clear_empty_lists()
        return interim_element


def test_3():

    list_of_lists_2 = [
        [['a', []], ['b', [], 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        print(flat_iterator_item, check_item)
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()

    print('\n  -- Конец --  ')  # - Для блокнота

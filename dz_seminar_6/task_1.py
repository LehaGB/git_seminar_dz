"""
Элементы из заданного диапазона
Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону
(т.е. не меньше заданного минимума и не больше заданного максимума).
На вход подается список с элементамиlist_1 и
границы диапазона в виде чисел min_number, max_number.
На входе:
list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_number = 0
max_number = 10
На выходе:
1 2 3 6 7 9 10 11 13 14 16 19 -> индексы чисел
"""


from typing import List


def index_number(array: List[int]) -> int:
    """На вход принемает список целых чисел, вовращает индекс числа.

    Args:
        array (List[int]): целое число

    Returns:
            int: индекс числа
    """
    min_number = 0
    max_number = 10
    array = []
    for i in range(len(list_1)):
        if list_1[i] >= min_number and list_1[i] <= max_number:
            array.append(i)
    return array


list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]


if __name__ == '__main__':
    print(*index_number(list_1))

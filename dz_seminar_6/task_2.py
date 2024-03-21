"""
Арифметическая прогрессия.
Заполните массив элементами арифметической прогрессии.
Её первый элемент a1 , разность d и количество элементов n
будет задано автоматически.
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
На входе: a1 = 2 d = 3 n = 4
На выходе: 2 5 8 11

"""


from typing import List


# def arithmetic_progression(a1: int, d: int, n: int) -> List[int]:
#     list_1 = []
#     for i in range(n):
#         result = (a1 + i * d)
#         list_1.append(result)
#     return list_1


# a1 = int(input('Введите первое число: '))
# d = int(input('Введите второе число: '))
# n = int(input('Введите третие число: '))


# if __name__ == '__main__':
#     print(*arithmetic_progression(a1, d, n))

a1 = 2
d = 3
n = 4
for i in range(n):
    print(a1 + i * d)

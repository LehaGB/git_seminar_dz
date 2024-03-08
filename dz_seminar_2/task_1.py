"""
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
решкой, а некоторые – гербом. Определите минимальное число
монеток, которые нужно перевернуть, чтобы все монетки были
повернуты вверх одной и той же стороной. Выведите минимальное
количество монет, которые нужно перевернуть.

"""
coins = [0, 0, 0, 0, 0]
count_zero = 0
count2 = 0
for coin in range(len( coins)):
    if coins[coin] == 0:
        count_zero += 1
    if coins[coin] == 1:
        count2 += 1
if count_zero > count2:
        print(f'{count2} -> 1')
if count_zero < count2:
        print(f'{count_zero} -> 0')
# if count_zero == count2:
#         print(f'{count_zero} == ')


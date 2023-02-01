# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты
# вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
# Пример:
# 5 -> 1 0 1 1 0
# 2

from random import randint

coins = int(input("Введите количество монет: "))
heads = 0
tails = 0

print(f'{coins} -> ', end='')

for value in range(0, coins):
    temp = 0
    temp += randint(0, 1)
    print(f'{temp}', end=' ')
    if temp == 1:
        heads += 1
    else:
        tails += 1
print()
if heads > tails:
    print(tails)
elif heads < tails:
    print(heads)
else:
    print(f"{heads} or {tails} Без разницы")

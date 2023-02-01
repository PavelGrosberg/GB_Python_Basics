# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# Пример:
# 10 -> 1 2 4 8

number = int(input("Введите число N: "))

counter = 0
value = 1
print(f'{number} -> ', end='')
while value <= number:
    value = 2 ** counter
    if value <= number:
        print(value, end=' ')
    counter += 1

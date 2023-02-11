# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания
# все те числа, которые встречаются в обоих наборах. Пользователь вводит 2 числа. n - кол-во элементов первого
# множества.
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
# Пример:
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

from random import randint

first_set_len = int(input('Кол-во элементов первого множества: '))
second_set_len = int(input('Кол-во элементов второго множества: '))
print(first_set_len, end=' ')
print(second_set_len)

first_set = []
second_set = []

for i in range(0, first_set_len):
    first_set.append(randint(1, 10))
print(*first_set)
first_set = set(first_set)

for i in range(0, second_set_len):
    second_set.append(randint(1, 10))
print(*second_set)
second_set = set(second_set)
print(*first_set.intersection(second_set))

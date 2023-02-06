# Задаем длину списка наполненного рандомными числами от 1 до 100.
# Вводим искомое число X
# Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
# которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению

from random import randint

len_list = int(input("Введите длину списка: "))
number = int(input("Введите искомое число Х: "))
numbers = [0] * len_list
for i in range(len(numbers)):
    numbers[i] = randint(1, 100)
print(numbers)
count = 0

if number in numbers:
    for i in range(len(numbers)):
        if numbers[i] == number:
            count += 1
    print(f'Число Х = {number} встречается в заданном списке {count} раза')

elif number not in numbers:
    left_number = number
    right_number = number
    while right_number not in numbers and right_number <= 100:
        right_number += 1
    if right_number <= 100:
        print(f'Число {number} отсутствует в заданном списке, максимально близкое большее число {right_number}')
    else:
        print("Максимально близкого большего числа к заданному не существует")
    if right_number not in numbers:
        while left_number not in numbers:
            left_number -= 1
        print(f'Максимально близкое меньшее число {left_number}')

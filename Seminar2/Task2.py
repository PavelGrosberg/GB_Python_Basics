# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две
# подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
# Пример:
# 4 4 -> 2 2
# 5 6 -> 2 3

"""
X = 0
Y = 0

X + Y = S
X * Y = P

Y = S - X
P = X * (S - X)
-X * X + S * X - P = 0
"""

from math import sqrt


def calc_guess_numbers(x, y):
    discriminant = x * x + 4 * -y
    # print(f'D = {discriminant}')
    if discriminant > 0:
        sq = sqrt(discriminant)/2
        p = x / 2
        x1 = int(p - sq)
        x2 = int(p + sq)
        print(f'{x1} {x2}')
    elif discriminant == 0:
        x1 = int(x / 2)
        x2 = x1
        print(f'{x1} {x2}')
    else:
        print("Корней нет")
    return


def search_guess_numbers():
    number1 = int(input("Сумма чисел: "))
    number2 = int(input("Произведение чисел: "))
    print(f'{number1} {number2} -> ', end='')
    calc_guess_numbers(number1, number2)


search_guess_numbers()

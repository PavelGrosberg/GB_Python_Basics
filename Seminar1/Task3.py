# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет
# счастливость билета.
# Пример:
# 385916 -> yes
# 123456 -> no

def sum_digit(number):
    first_digit = number // 100
    second_digit = number // 10 % 10
    third_digit = number % 10
    sum_digits = first_digit + second_digit + third_digit
    return sum_digits


ticket_number = int(input("Введите номер билета: "))
first_three = ticket_number // 1000
second_three = ticket_number % 1000

if sum_digit(first_three) == sum_digit(second_three):
    print(f'{ticket_number} -> yes')
else:
    print(f'{ticket_number} -> no')

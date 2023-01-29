# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

number = int(input("Введите трехзначное число:"))
if 0 < number < 1_000:
    first_digit = number // 100
    second_digit = number // 10 % 10
    third_digit = number % 10
    sum_digits = first_digit + second_digit + third_digit
    print(f'{number} -> {sum_digits} ({first_digit} + {second_digit} + {third_digit})')
else:
    print("Это так не работает !!!")

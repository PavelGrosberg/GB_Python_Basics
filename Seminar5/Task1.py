# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии

def rec_pow(a, b):
    if b == 1:
        return a
    return a * pow(a, b - 1)


print(pow(2, 4))

# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал
# каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза
# больше журавликов, чем Петя и Сережа вместе?
# Пример:
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

S = int(input("Сколько всего журавликов сделали ребята? \n"))
if S % 6 == 0:
    serg = petr = x = int(S / 6)
    kate = 4 * x
    print(f'{S} -> {serg} {kate} {petr}')
elif S < 6:
    print("Логически, исходя из условия, журавликов не может быть меньше чем 6. Получится неверное уравнение S = 2x + 4x")
else:
    print('Ошибка. "полтора" журавлика')

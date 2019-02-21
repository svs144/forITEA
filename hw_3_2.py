# Валидация входного числа
def validate_input(n):
    if n.isdigit():
        n = int(n)     #порядковый номер числа Ф.
        return n
    else:
        return -1

# Расчет числа Фибоначчи
def get_fibonachi(n):
    summ = 0  # значение порядкового номера числа Ф.
    f_part = 0
    s_part = 1
    if n == 0:  # 0й эл = 0
        summ = f_part
    elif n == 1:  # 1й эл = 1
        summ = s_part
    else:  # 2й+ эл = сумме двух предыдущих
        for x in range(2, n):
            if x % 2 == 0:
                f_part = f_part + s_part
            else:
                s_part = f_part + s_part
        summ = f_part + s_part
    return summ

# Вызов функций
while True:
    n = input('Введите порядковый номер Числа Фибоначчи: ').strip()
    n = validate_input(n)
    if n >= 0:
        break
print('Элемент [{}] ряда Чисел Фибоначчи = {}'.format(n, get_fibonachi(n)))





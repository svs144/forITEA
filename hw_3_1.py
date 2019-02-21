a = input('Введите число a: ').strip()
b = input('Введите число b: ').strip()

# Валидация входного числа
def validate_numbers(input_num):
    num_ok = True
    cnt_point = 0
    cnt_minus = 0
    for x in input_num:
        if (x.isdigit()):
            pass
        elif (x.isalpha()):
            num_ok = False
        elif (x == '.'):
            cnt_point += 1
        elif (x == '-'):
            cnt_minus += 1
        else:
            num_ok = False
    if cnt_minus > 1 or cnt_point > 1 or input_num == '':
        num_ok = False
    return num_ok


# Расчет суммы натуральных чисел
def sum_natural_numbers(a, b):
    summ = 0  # сумма всех натуральных чисел
    if float(a) < float(b):
        start = int(a) if a.isdigit() else float(a)
        end = int(b) if b.isdigit() else float(b)
    elif float(a) > float(b):
        start = int(b) if b.isdigit() else float(b)
        end = int(a) if a.isdigit() else float(a)
    else:
        if not a.isdigit():
            if float(a) == int(float(a)):
                return int(float(a))
            else:
                return 0
        else:
            return a
        exit()
    rez_isset = False  # если не найдены числа, то дописываем '0'
    show_float = False
    end = int(end) + 1
    while start < end:
        if show_float or start == int(start):
            if start > 0:
                summ += int(start)
            rez_isset = True
        else:
            show_float = True
        start += 1
    if not rez_isset:
        return 0
    else:
        return summ

# Вызов функций
if validate_numbers(a) and validate_numbers(b):
    print('Сумма натуральных чисел в диапазоне от ', a, ' до ', b, '>>> ', sum_natural_numbers(a, b))
else:
    print('Неверный формат ввода данных!')

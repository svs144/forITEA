first_num = input('Введите число a: ')
second_num = input('Введите число b: ')
summ = 0  # сумма всех натуральных чисел

if (float(first_num) >= 0 and float(second_num) >= 0):
    diff = float(first_num) - float(second_num)  # ищем начало и конец диапазона
    if diff < 0:
        start = int(first_num) if first_num.isdigit() else float(first_num)
        end = int(second_num) if second_num.isdigit() else float(second_num)
    elif diff > 0:
        start = int(second_num) if second_num.isdigit() else float(second_num)
        end = int(first_num) if first_num.isdigit() else float(first_num)
    else:
        if not first_num.isdigit() or first_num == '0':
            print('Сумма натуральных чисел в диапазоне от ', first_num, ' до ', second_num, '>>> 0')
        else:
            print('Сумма натуральных чисел в диапазоне от', first_num, ' до ', second_num, '>>> ', first_num)
        exit()
    print('Сумма натуральных чисел в диапазоне от ', start, ' до ', end, '>>> ', end='')
    rez_isset = False  # если не найдены числа, то дописываем строку "не найдено"
    show_float = False
    end = int(end) + 1
    while start < end:
        if show_float or start == int(start):
            summ += int(start)
            rez_isset = True
        else:
            show_float = True
        start += 1
    print('0') if not rez_isset else print(summ)
else:
    print('Неверный формат ввода данных!')

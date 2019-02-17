first_num = input('Введите число a: ').strip()
second_num = input('Введите число b: ').strip()
summ = 0  # сумма всех натуральных чисел
error = False

cnt_point1 = 0  # счетчики точек
cnt_point2 = 0
cnt_minus1 = 0  # счетчики минусов
cnt_minus2 = 0
for x in first_num:
    if (x.isdigit()):
        pass
    elif (x.isalpha()):
        error = True
    elif (x == '.'):
        cnt_point1 += 1
    elif (x == '-'):
        cnt_minus1 += 1
    else:
        error = True

for x in second_num:
    if (x.isdigit()):
        pass
    elif (x.isalpha()):
        error = True
    elif (x == '.'):
        cnt_point2 += 1
    elif (x == '-'):
        cnt_minus2 += 1
    else:
        error = True

if not error and first_num != '' and second_num != '' and cnt_point1 < 2 and cnt_point2 < 2 and cnt_minus1 < 2 and cnt_minus2 < 2:
    if float(first_num) < float(second_num):
        start = int(first_num) if first_num.isdigit() else float(first_num)
        end = int(second_num) if second_num.isdigit() else float(second_num)
    elif float(first_num) > float(second_num):
        start = int(second_num) if second_num.isdigit() else float(second_num)
        end = int(first_num) if first_num.isdigit() else float(first_num)
    else:
        if not first_num.isdigit():
            if float(first_num) == int(float(first_num)):
                print('Сумма натуральных чисел в диапазоне от ', first_num, ' до ', second_num, '>>> ', int(float(first_num)))
            else:
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
            if start > 0:
                summ += int(start)
            rez_isset = True
        else:
            show_float = True
        start += 1
    print('0') if not rez_isset else print(summ)
else:
    print('Неверный формат ввода данных!')

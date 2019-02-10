while True:
    fib_num = input('Введите порядковый номер Числа Фибоначчи: ')
    if fib_num.isdigit():
        fib_num = int(fib_num)     #порядковый номер числа Ф.
        summ = 0                   #значение порядкового номера числа Ф.
        break

f_part = 0
s_part = 1

if fib_num == 0:  #0й эл = 0
    summ = f_part
elif fib_num == 1:#1й эл = 1
    summ = s_part
else: #2й+ эл = сумме двух предыдущих
    for x in range(2, fib_num):
        if x % 2 == 0:
            f_part = f_part + s_part
        else:
            s_part = f_part + s_part
    summ = f_part + s_part

print('Элемент [{}] ряда Чисел Фибоначчи = {}'.format(fib_num, summ))



def calc_to_bin(number):
    rez = '';
    while True:
        x,y = divmod(number, 2)
        rez = str(number - x * 2) + rez
        number = x
        if x < 2:
            if x == 1:
                rez = str(x) + rez
            rez = '0b' + rez
            print('Число в двоичном коде >>> ', rez)
            break
    pass


num = int(input('Введите число для конвертации >>> '))
calc_to_bin(num)
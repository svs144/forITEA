def check(num_str):
    try:
        return int(input('Введите ' + num_str + ' целое число: '))
    except:
        print('Вы ввели не целое число!')
        exit()

def show(val):
    print('Целое = ' + str(val))
    print('Вещественное = ' + str(float(val)))
    print('Логическое = ' + str(bool(val)))
    print('Строка = "' + str(val) + '"')

def rez(a, b):
    c = a + b
    print('Целое + Целое = ' + str(c))
    c = a * b
    print('Целое * Целое = ' + str(c))
    c = a + float(b)
    print('Целое + Вещественное = ' + str(c))
    c = a * float(b)
    print('Целое * Вещественное = ' + str(c))
    c = a + bool(b)
    print('Целое + Логичское = ' + str(c))
    c = a * bool(b)
    print('Целое * Логическое = ' + str(c))
    c = a * str(b)
    print('Целое * Строка = "' + str(c) + '"')
    c = float(a) + b
    print('Вещественное + Целое = ' + str(c))
    c = float(a) * b
    print('Вещественное * Целое = ' + str(c))
    c = float(a) + float(b)
    print('Вещественное + Вещественное = ' + str(c))
    c = float(a) * float(b)
    print('Вещественное * Вещественное = ' + str(c))
    c = float(a) + bool(b)
    print('Вещественное + Логическое = ' + str(c))
    c = float(a) * bool(b)
    print('Вещественное * Логическое = ' + str(c))
    c = bool(a) + b
    print('Логическое + Целое = ' + str(c))
    c = bool(a) * b
    print('Логическое * Целое = ' + str(c))
    c = bool(a) + float(b)
    print('Логическое + Вещественное = ' + str(c))
    c = bool(a) * float(b)
    print('Логическое * Вещественное = ' + str(c))
    c = bool(a) + bool(b)
    print('Логическое + Логическое = ' + str(c))
    c = bool(a) * bool(b)
    print('Логическое * Логическое = ' + str(c))
    c = bool(a) * str(b)
    print('Логическое * Строка = "' + str(c) + '"')
    c = str(a) * b
    print('Строка * Целое = "' + str(c) + '"')
    c = str(a) * bool(b)
    print('Строка * Логическое = "' + str(c) + '"')
    c = str(a) + str(b)
    print('Строка + Строка = "' + str(c) + '"')

first  = check('первое')
show(first)
second = check('второе')
show(second)
rez(first, second)

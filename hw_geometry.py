import math

FIRST_LINE = '          *'
SECOND_LINE = '***********'
new_line = ''


def three_angles(mode='tr2'):
    y_range = 0
    for x in range(10):
        y_range += 1
        f_line = False
        for y in range(y_range):
            if not f_line:
                new_line = FIRST_LINE[x:12]
                if mode != 'tr1':
                    new_line += x * '*'
                print(new_line, end='')
                f_line = True
            else:
                print('*', end='')
        print()

    if mode == 'romb':
        for x in range(10):
            y_range -= 1
            f_line = False
            for y in range(y_range):
                if not f_line:
                    new_line = (x + 2) * ' ' + SECOND_LINE[x:9]
                    print(new_line, end='')
                    f_line = True
                else:
                    print('*', end='')
            print()


# равноб треугольник
three_angles()

# ромб
three_angles('romb')

# прям треугольник
three_angles('tr1')

#круг (через sin и cos)
r = 20
a = []
for angle in range(0, 360, 5):
    x = round(math.sin(angle) * r);
    y = round(math.cos(angle) * r);
    a.append([x, y]) #координаты с шагом 5 градусов записываем в список

# -30 +30 (x y)
find = False #флаг, который указывает что координаты в списке найдены
for x in range(-40, 40):
    for y in range(-40, 40):
        for x2, y2 in a:
            if x == x2 and y == y2:
                find = True
                break
        if find:
            find = False
            print('**', end='')
        else:
            print('  ', end='')
    print('')

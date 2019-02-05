try:
    first_num  = float(input('Введите Число1: '))
    second_num = float(input('Введите Число2: '))
except:
    print('Число задано неверно!')
    exit()

sum_rez = first_num + second_num
dif_rez = first_num - second_num
multi_rez = first_num * second_num
pow_rez = first_num ** second_num
div_rez = first_num / second_num
euclidiv_rez = first_num // second_num
mod_rez = first_num % second_num

print()
print('Арифметические')
print(('{0} + {1} = {2}').format(first_num, second_num, sum_rez))
print(('{0} - {1} = {2}').format(first_num, second_num, dif_rez))
print(('{0} * {1} = {2}').format(first_num, second_num, multi_rez))
print(('{0} ** {1} = {2}').format(first_num, second_num, pow_rez))
print(('{0} / {1} = {2}').format(first_num, second_num, div_rez))
print(('{0} // {1} = {2}').format(first_num, second_num, euclidiv_rez))
print(('{0} % {1} = {2}').format(first_num, second_num, mod_rez))
print()

print('Cравнения')
comparis_rez = first_num == second_num
print(('{0} == {1}  {2}').format(first_num, second_num, comparis_rez))
comparis_rez = first_num != second_num
print(('{0} != {1}  {2}').format(first_num, second_num, comparis_rez))
comparis_rez = first_num > second_num
print(('{0} > {1}  {2}').format(first_num, second_num, comparis_rez))
comparis_rez = first_num < second_num
print(('{0} < {1}  {2}').format(first_num, second_num, comparis_rez))
comparis_rez = first_num >= second_num
print(('{0} >= {1}  {2}').format(first_num, second_num, comparis_rez))
comparis_rez = first_num <= second_num
print(('{0} <={1}  {2}').format(first_num, second_num, comparis_rez))
print()

print('Тождественности')
tozhd_rez = first_num is second_num
print(('{0} is {1}  {2}').format(first_num, second_num, tozhd_rez))
tozhd_rez = first_num is not second_num
print(('{0} is not {1}  {2}').format(first_num, second_num, tozhd_rez))
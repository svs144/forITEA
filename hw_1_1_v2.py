from datetime import date

first_name  = str(input('Введите Ваше имя: '))
second_name = str(input('Введите Вашу фамилию: '))
print(('{0} {1}, добро пожаловать в мир Python! :)').format(first_name, second_name), end='\n\n')

now = date.today() #текущая дата (г-м-д)

#Ввод даты рождения и валидация
try:
    day_birth   = int(input('Введите день Вашего рождения (целое число): '))
    month_birth = int(input('Введите месяц Вашего рождения (целое число): '))
    year_birth  = int(input('Введите год Вашего рождения (целое число): '))
    if len(str(day_birth)) > 2 or month_birth < 1 or month_birth > 12:
        print('Месяц Вашего рождения задан неверно')
        exit()
    if len(str(day_birth)) > 2 or day_birth < 1 or day_birth > 31:
        print('День Вашего рождения задан неверно')
        exit()
    if len(str(year_birth)) != 4 or year_birth > now.year:
        print('Год Вашего рождения задан неверно')
        exit()
except:
    print('Вы ввели не целое число!')
    exit()

#Расчет количества прожитых лет
age_year   = now.year - year_birth

if (now.month, now.day) < (month_birth, day_birth):
    age_year -= 1
    # Расчет количества прожитых месяцев
    age_month = age_year * 12 + 12 - month_birth + now.month - 1
    print(('{0} {1} {2}').format(age_month, month_birth, now.month))
else:
    age_month = age_year * 12 + now.month - month_birth - 1

if 30 - day_birth + now.day >= 30:
    age_month += 1

#Расчет количество прожитых дней, месяцев, лет до даты начала курса 31.01.2019
itea_date  = date(2019, 1, 31)

try:
    birth_date = date(year_birth, month_birth, day_birth)
except:
    print('Дата Вашего рождения задана неверно')
    exit()

delta      = itea_date - birth_date
years_to, remainder = divmod(delta.days, 365)
months_to  = remainder // 30
days_to    = now.day - 1

print('Вы прожили ' + str(age_year) + ' лет')
print('Вы прожили ' + str(age_month) + ' месяцев')
print('Вы прожили {0} дней {1} месяцев {2} лет до даты начала курса'.format(days_to, months_to, years_to))
import certifi  # валидация SSL-сертификата
import urllib3
import pymongo
from urllib.parse import quote
from time import gmtime, strftime

DB_NAME = 'vacancy'
DB_TABLE = 'professions'
DB_ISSET = False

# Приветствие
print('=== Поиск вакансии на портале Rabota.ua by Андрей Н. (ITEA, PythonBase Feb 2019) ===')

# Выбор режима работы
work_mode = input(
    'Введите режим работы ( 1 - поиск и добавлений новых записей, 2 - извлечение всех записей БД, 3 - форматироние БД; по умолчанию - 1): ')
if len(work_mode.strip()) == 0:
    work_mode = 1
# Если не удается получить режим работы , то выходим с программы
try:
    work_mode = int(work_mode)
except:
    print('Режим работы не выбран!')
    exit()

# Коннект к серверу, выбор БД, выбор таблицы
# Если не удалось подключится - работаем в режиме без БД
try:
    print('Ожидаем связи с сервером MongoDB ...')
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient[DB_NAME]
    mycol = mydb[DB_TABLE]
    DB_ISSET = True
    dblist = myclient.list_database_names()
    if DB_NAME in dblist:
        print('Связь с сервером MongoDB установлена!')
except:
    print('Сервер MongoDB не найден!')
    DB_ISSET = False
    if work_mode > 1:
        exit()

#########################
# Обьяление функций
#########################
# Показать все записи БД
def showRecords():
    if DB_ISSET:
        count_rec = 0
        for rec in mycol.find().sort("name", pymongo.ASCENDING):
            print(rec)
            count_rec += 1
        print('Извлечено {} записей!'.format(count_rec))
    exit()


# Удалить все записи БД
def deleteRecords():
    x = mycol.delete_many({})
    print(x.deleted_count, " записей удалено.")
    exit()


# Добавление  записи в БД
def addRecord(current_job, current_company, current_price):
    if DB_ISSET:
        add_record = {"name": current_job, "company": current_company, "salary": current_price, "link": current_link}
        mycol.insert_one(add_record)


#####################

if work_mode == 3:
    deleteRecords()
elif work_mode == 2:
    showRecords()
elif work_mode == 1:
    pass
else:
    print('Режим работы не выбран!')
    exit()

# входящие параметры (работа и город)
work_str = input('Введите профессию (по умолчанию бухгалтер): ')
city_str = input('Введите город (по умолчанию Киев): ')

# обработка входных параметров
if len(work_str) == 0:
    work_str = 'бухгалтер'
if len(city_str) == 0:
    city_str = 'киев'
work_str = work_str.lower()
city_str = city_str.lower()

# название файла с результатами
file_name = strftime("%Y.%m.%d %H_%M_%S", gmtime())
file_name += '.txt'

# номер начальной страницы (постраничная навигация)
page = 1

# страница существует
page_isset = True

# главный цикл (постраничный переход)
while page_isset:
    # пакет certifi для HTTPS используем
    http = urllib3.PoolManager(
        cert_reqs='CERT_REQUIRED',
        ca_certs=certifi.where())

    # кодирование кириллицы в юникод
    # динамичеки меняем ссылки (с учетом постраничной навигации)
    url = 'https://rabota.ua/zapros/' + format(quote(work_str)) + '/' + format(quote(city_str))
    if page > 1:
        add_url = '/pg' + str(page)
        url = url + add_url

    # подмена хидеров браузера (иначе может на мобильную версию перекинуть)
    r = http.request(
        'GET',
        url,
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        })

    # страница не сервере не существует
    if r.status != 200:
        print('Ошибочный URL!')
        exit()

    # декодирование контента страницы
    datas = str(r.data.decode('utf-8'))
    page = page + 1

    # проверка на переход за границы существования вакансий
    try:
        current_pos = datas.index('вакансий пока нет.')
        if current_pos > 0:
            page_isset = False
            print('Выход.')
    except ValueError:
        current_pos = 0

    # поиск атрибута даного класса на странице
    current_pos = datas.index('f-vacancylist-tablewrap')

    # впомогательный цикл-парсер содержимого одной страницы
    while (current_pos >= 0):
        current_job = ''  # профессия
        current_company = ''  # компания
        current_price = ''  # зарплата (может быть неукзаана)
        current_link = ''  # ссылка на вакансию
        try:
            current_pos = datas.index('f-visited-enable ga_listing', current_pos)
            try:
                current_pos += 1
                next_pos = datas.index('f-visited-enable ga_listing', current_pos)
            except ValueError:
                next_pos = len(datas)
            finally:
                current_pos = datas.index('title="', current_pos, next_pos)
                current_pos += 7
                begin_pos = current_pos
                current_pos = datas.index('"', current_pos)
                current_job = datas[begin_pos:current_pos]
                try:
                    current_pos = datas.index('href="', current_pos, next_pos)
                    current_pos += 6
                    begin_pos = current_pos
                    current_pos = datas.index('">', current_pos, next_pos)
                    current_link = 'https://rabota.ua' + datas[begin_pos:current_pos]
                    current_pos = datas.index('f-text-dark-bluegray f-visited-enable', current_pos)
                    current_pos = datas.index('title="', current_pos, next_pos)
                    current_pos += 7
                    begin_pos = current_pos
                    current_pos = datas.index('"', current_pos, next_pos)
                    current_company = datas[begin_pos:current_pos]
                    try:
                        current_pos = datas.index('fd-beefy-soldier -price', current_pos, next_pos)
                        current_pos += 25
                        begin_pos = current_pos
                        current_pos = datas.index('</p>', current_pos, next_pos)
                        current_price = datas[begin_pos:current_pos]
                    except ValueError:
                        current_price = 'не указано'
                        current_pos += 25
                except ValueError:
                    current_pos += 7
        except ValueError:
            break

        # вывод части извлеченной информации в консоль
        print(('Профессия: {0}, компания: {1}, зп: {2};').format(current_job, current_company, current_price))

        # добавление извлеченной информации в БД
        addRecord(current_job, current_company, current_price)

        # сохранение извлеченной информации в файл txt
        try:
            with open(file_name, "a") as file:
                file.write(
                    'профессия: ' + current_job + ', компания: ' + current_company + ', ссылка: ' + current_link + ', зп: ' + current_price + '\n')
        except:
            pass

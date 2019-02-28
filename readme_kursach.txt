1. Устанавливаем MondoDB (https://www.mongodb.com/download-center/community) вкладка Сервер. Устанавливаем без Compass (GUI для MongoDB)
2. В windows вручную создаем на диске C:/data/db  (две директории)
3. В установленой директории MongoDB в папке bin запускаем mongod.exe (консоль не закрываем).
4. Запускаем kursach.py
	Использованные библиотеки:
	import certifi 
	import urllib3
	import pymongo
	from urllib.parse import quote
	from time import gmtime, strftime
5. Выбираем режим работы (1 - поиск вакансии и добавление в БД, 2 - извлечение записей с БД, 3 - форматировать БД)
6. Также после выбора режима 1 создается файл c расширением txt с найденными вакансиями
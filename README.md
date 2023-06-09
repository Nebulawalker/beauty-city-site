# beauty-city-site



## Как установить
Для написания скрипта использовался __Python 3.11.0__, подойдет 3.7 и выше

1. Склонировать репозиторий.
2. Создать виртуальное окружение.
```bash
python -m venv env
```
3. Активировать виртуальное окружение:

```bash
. env/bin/activate
```
   
4. Установить зависимости:
```bash
pip install -r requirements.txt
```
1. Переименовать файл `.env_example` в .env

```bash
mv .env_example .env
```

6. Отредактировать файл `.env`
Описание содержимого:
```text
SECRET_KEY=REPLACE_ME
DEBUG=True
ALLOWED_HOSTS=127.0.0.1
```
Доступны 3 переменные:
- `DEBUG` — дебаг-режим. Поставьте True, чтобы увидеть отладочную информацию в случае ошибки.
  В случае если `DEBUG = True`, используется тестовая база данных `test_db.sqlite3`
- `SECRET_KEY` — секретный ключ проекта
- `ALLOWED_HOSTS` — см [документацию Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts).

## Запуск отладочного сервера
Примените миграции:
```bash
python manage.py migrate
```
Создайте суперпользователя:
```bash
python manage.py createsuperuser
```
Запуск отладочного сервера:
```bash
python manage.py runserver
```

Сайт - http://127.0.0.1:8000/

Админка - http://127.0.0.1:8000/admin/
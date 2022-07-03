# Настройки для входа на сервер PostgreSQL, а также для создания новой
# БД для выполнения задания

pg_secret = {
    'db_host': '{YOUR_DATABASE_HOST}',  # Имя хоста: имя сервера или IP-адрес, на котором работает база данных
    'db_name': '{YOUR_DATABASE_NAME}',  # Имя БД, которая будет создана в ходе проекта
    'db_password': '{YOUR_DATABASE_PASSWORD}',  # Пароль для входа на сервер
    'db_port':  '{YOUR_DATABASE_PORT}',  # Имя порта
    'db_user': '{YOUR_DATABASE_USER}'  # Имя пользователя: значение по умолчанию для базы данных PostgreSQL – postgres
}
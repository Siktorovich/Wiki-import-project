<h1> Импорт данных цитат википедии и сервис для поиска статьи по точному совпадению наименования
(FastAPI, PostgreSQL и SQLAlchemy)</h1>

Проект доступен по ссылке <br>  
https://github.com/Siktorovich/Wiki-Service-Project.git

<h2>Подготовка</h2>
<p>Установите PostgreSQL и создайте там пользователя

Измените данные в файле postgresql_secret.py</p> 
<code>
pg_secret = {
    'db_host': {YOUR_DATABASE_HOST},  
    'db_name': {YOUR_DATABASE_NAME},
    'db_password': {YOUR_DATABASE_PASSWORD},  
    'db_port':  {YOUR_DATABASE_PORT},  
    'db_user': {YOUR_DATABASE_USER},  
}
</code>
<p>Создайте виртуальное окружение</p>
<code>python -m venv env</code>

<p>Активируйте виртуальное окружение</p>

<code>env/bin/activate <br></code>
<p>или </p>
<code>env\Scripts\activate <br></code>

<p>Установите необходимые инструменты для корректной работы проекта</p>
<code>pip install -r requirements.txt</code>

<p>Разархивируйте дамп данных Википедии в каталог проекта</p>

<h2>Импорт данных, создание БД и отношения</h2>

<p>Выполните</p>
<code>python main.py</code>

<h2>Запуск сервиса</h2>

<p>Выполните</p>
<code>python app.py</code>
<p>Uvicorn запустит сервис по адресу</p>
<a>http://127.0.0.1:8000</a>
<p>Для выполнения запроса введите его в адресную строку или через интерфейс FastAPI</p>
<p>Используйте CTRL+C для выхода</p>



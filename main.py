import json
import psycopg2
from postgresql_secret import pg_secret
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from models import Article
from database import SessionLocal, engine
from sqlalchemy.orm import Session, sessionmaker
import models



def fill_db(path):
    print(f'Creating TABLE {Article.__tablename__}...')
    models.Base.metadata.create_all(engine)
    print('TABLE created successfully')
    print('Filling content...')

    session = Session(bind=engine)

    list_of_dicts = [json.loads(line) for line in open(path, 'r')]  # Перевод JSON объекта в PYTHON объект

    for dict in list_of_dicts:
        temp_obj = Article()
        Article.language = 'Undefined'
        for keys, values in dict.items():  # Перебор ключей и значений в словарях и последующая их фильтрация
            if keys == 'category':
                temp_obj.category = values
            elif keys == 'title':
                temp_obj.title = values
            elif keys == 'auxiliary_text':
                temp_obj.auxiliary_text = values
            elif keys == 'create_timestamp':
                temp_obj.create_timestamp = values
            elif keys == 'timestamp':
                temp_obj.timestamp = values
            elif keys == 'language':
                temp_obj.language = values
            elif keys == 'wiki':
                temp_obj.wiki = values
            else:
                continue
        if temp_obj.language == 'Undefined':
            del temp_obj
        else:
            session.add(temp_obj)
            session.commit()


def db_create():  # Создание БД
    try:
        print('Creating Database...')

        connection = psycopg2.connect(
            user=pg_secret['db_user'],
            password=pg_secret['db_password'],
            host=pg_secret['db_host'],
            port=pg_secret['db_port'],
        )
        database = pg_secret['db_name']
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        # Курсор для выполнения операций с базой данных
        cursor = connection.cursor()
        sql_create_database = f'create database {database}'
        cursor.execute(sql_create_database)
        print("Database created successfully in PostgreSQL")

    except (Exception, Error) as error:
        print("Error at work PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Connecting with PostgreSQL closed")


def main():
    db_create()  # Вызов функции создания БД
    path = 'ruwikiquote-20220627-cirrussearch-general.json'  # Путь к файлу, из которого нужно импортировать данные
    fill_db(path)  # Вызов функции импорта данных


if __name__ == '__main__':
    main()



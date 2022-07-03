from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from postgresql_secret import pg_secret

engine = create_engine(f'postgresql://{pg_secret["db_user"]}:{pg_secret["db_password"]}@'
                       f'{pg_secret["db_host"]}:{pg_secret["db_port"]}/{pg_secret["db_name"]}',
                       echo=False)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()



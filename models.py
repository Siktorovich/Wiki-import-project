from database import Base
from sqlalchemy import String, Integer, Column, Text, Date
import time

class Article(Base):
    __tablename__ = 'wiki_project'

    id = Column(Integer, primary_key=True)
    category = Column(Text)
    title = Column(String(255))
    auxiliary_text = Column(Text)
    create_timestamp = Column(Date)
    timestamp = Column(Date)
    language = Column(String(2))
    wiki = Column(String(20))


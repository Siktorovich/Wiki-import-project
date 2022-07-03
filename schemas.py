from datetime import date
from pydantic import BaseModel


class Article(BaseModel):
    id: int
    category: str
    title: str
    auxiliary_text: str
    create_timestamp: date
    timestamp: date
    language: str
    wiki: str

    class Config:
        orm_mode = True

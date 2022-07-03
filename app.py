from fastapi import FastAPI, status, HTTPException
import uvicorn
from typing import List
from database import SessionLocal, engine
import models, schemas
from starlette.responses import RedirectResponse
import database
import json

app = FastAPI()

db = SessionLocal()

# @app.on_event("startup")
# async def startup():
#     # когда приложение запускается устанавливаем соединение с БД
#     await database.connect()
#
#
# @app.on_event("shutdown")
# async def shutdown():
#     # когда приложение останавливается разрываем соединение с БД
#     await database.disconnect()


@app.get("/")
def main():
    return RedirectResponse(url="/docs/")


# @app.get('/wiki', response_model=List[schemas.Article], status_code=200)
# def get_all_articles():
#     articles = db.query(models.Article).all()
#
#     return articles


@app.get('/wiki/{article_title}', response_model=schemas.Article, status_code=status.HTTP_200_OK)
def get_an_article(article_title: str):
    article = db.query(models.Article).filter(models.Article.title == article_title).first()
    return article


@app.get('/wiki/{article_title}?pretty', status_code=status.HTTP_200_OK)
def get_an_article_pretty(article_title: str):
    article = db.query(models.Article).filter(models.Article.title == article_title).first()
    for key, value in article.items():
        return "{0}: {1}".format(key, value)
     # json.dumps(article, indent=4, sort_keys=True)


if __name__ == '__main__':
    uvicorn.run('app:app', port=8000, host='127.0.0.1', reload=True)

# @app.put('/item/{item_id}', response_model=schemas.Article, status_code=status.HTTP_200_OK)
# def update_an_item(item_id: int, item: Item):
#     item_to_update = db.query(models.Item).filter(models.Item.id == item_id).first()
#     item_to_update.name = item.name
#     item_to_update.price = item.price
#     item_to_update.description = item.description
#     item_to_update.on_offer = item.on_offer
#
#     db.commit()
#
#     return item_to_update
#

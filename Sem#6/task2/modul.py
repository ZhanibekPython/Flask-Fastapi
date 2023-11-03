from typing import List
import databases
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from sqlalchemy import Table, create_engine, Column, Integer, String, MetaData
from pydantic import BaseModel, Field

app = FastAPI()

DATABASE_url = 'sqlite:///task2.db'
database = databases.Database(DATABASE_url)
metadata = MetaData()
engine = create_engine(DATABASE_url)
metadata.create_all(engine)


@app.on_event('startup')
async def db_connection():
    await database.connect()


@app.on_event('shutdown')
async def db_disconnection():
    await database.disconnect()


user = Table(
    "user",
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(30), nullable=False),
    Column('surname', String(30), nullable=False),
    Column('birth_date', String(10), nullable=False),
    Column('email', String(50), unique=True),
    Column('adres', String(80))
)


class User(BaseModel):
    id: int
    name: str = Field(..., ge=2)
    surname: str = Field(..., ge=2)
    birth_date: str = Field(..., max_length=10, pattern="(19|20)[0-9]{2}-"
                                                        "(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])")
    email: str = Field(None, max_length=50, pattern="(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\."
                                                    "[a-zA-Z0-9-.]+$)")
    adres: str = Field(None, ge=5)


@app.get("/", response_class=HTMLResponse)
def index():
    return "<h1> Welcome to task2 </h1>"


@app.post("/users/", response_model=User)
def add_user(user: User):
    res = user.insert().values(name=user.name, surname=user.surname,
                                birth_date=user.birth_date, email=user.email, adres=user.adres)
    for_writing = database.execute(res)
    return {"user": User}


if __name__ == '__main__':
    metadata.create_all(engine)
# Необходимо создать API для управления списком задач.
# Каждая задача должна содержать заголовок и описание.
# Для каждой задачи должна быть возможность
# указать статус (выполнена/не выполнена).
#
# API должен содержать следующие конечные точки:
# — GET /tasks — возвращает список всех задач.
# — GET /tasks/{id} — возвращает задачу с указанным идентификатором.
# — POST /tasks — добавляет новую задачу.
# — PUT /tasks/{id} — обновляет задачу с указанным идентификатором.
# — DELETE /tasks/{id} — удаляет задачу с указанным идентификатором.
#
# Для каждой конечной точки необходимо проводить валидацию данных
# запроса и ответа. Для этого использовать библиотеку Pydantic.

from fastapi import FastAPI
from sqlalchemy import create_engine, Table, Column, String, Integer, MetaData, Boolean, Text
from pydantic import BaseModel
from typing import Optional, List
from fastapi.responses import HTMLResponse

app = FastAPI(title='Seminar_5_HW')

engine = create_engine('mysql:///homework.db')
connection = engine.connect()

metadata = MetaData()

tasks = Table('tasks', metadata,
              Column('id', Integer, primary_key=True),
              Column('title', String, nullable=False),
              Column('description', Text),
              Column('status', Boolean)

class Task(BaseModel):
    id: int
    title: str
    description: Optional[str]
    status: Optional[bool]


@app.get('/', response_class=HTMLResponse)
def index():
    return '<h1> Main page </h1>'

@app.get('/tasks', response_class=List[Task]):
def tasks():
    return
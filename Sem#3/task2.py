# 📌 Создать базу данных для хранения информации о книгах в библиотеке.
# 📌 База данных должна содержать две таблицы: "Книги" и "Авторы".
# 📌 В таблице "Книги" должны быть следующие поля: id, название, год издания,
# количество экземпляров и id автора.
# 📌 В таблице "Авторы" должны быть следующие поля: id, имя и фамилия.
# 📌 Необходимо создать связь между таблицами "Книги" и "Авторы".
# 📌 Написать функцию-обработчик, которая будет выводить список всех книг с
# указанием их авторов.

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


task2 = Flask(__name__)
task2.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mybooks.db'
db = SQLAlchemy(task2)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    publ_year = db.Column(db.Integer, nullable=False)
    copies = db.Column(db.Integer, default=0)
    author_id = db.Column(db.String, db.ForeignKey('author.id'))

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    surname = db.Column(db.String, unique=True, nullable=False)
    books = db.relationship('Book', backref='author', lazy=True)

db.create_all()

author1 = Author(name='Vanya', surname='Vanyov')
author2 = Author(name='Petya', surname='Petyov')
author3 = Author(name='Sasha', surname='Sashov')

book1 = Book(name='Revolution', publ_year=2023, copies=140_000_000, author_id=author1)
book2 = Book(name='Evolution', publ_year=2024, copies=130_000_000, author_id=author2)
book3 = Book(name='Pollution', publ_year=2025, copies=10_000_000, author_id=author3)

db.session.add(author1, author2, author3, book1, book2, book3)
db.session.commit()


if __name__ == '__main__':
    task2.run(debug=True)

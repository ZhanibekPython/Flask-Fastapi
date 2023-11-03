# 📌 Создать страницу, на которой будет форма для ввода имени
# и электронной почты
# 📌 При отправке которой будет создан cookie файл с данными
# пользователя
# 📌 Также будет произведено перенаправление на страницу
# приветствия, где будет отображаться имя пользователя.
# 📌 На странице приветствия должна быть кнопка "Выйти"
# 📌 При нажатии на кнопку будет удален cookie файл с данными
# пользователя и произведено перенаправление на страницу
# ввода имени и электронной почты.

from flask import Flask, render_template, request, redirect, url_for, flash


hw = Flask(__name__)
hw.secret_key = b'a48a3265879cf995f7bc31b8bfd469d6ddfb118c30fb076c48172fa2e434dcb5'


@hw.route('/main')
@hw.route('/')
def main():
    return render_template('base.html')


if __name__ == '__main__':
    hw.run()
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from pathlib import Path

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/greet', methods=['POST'])
def greet():
    if request.method == 'POST':
        username = request.form['username']
        return render_template('greet.html', username=username)
    else:
        return redirect(url_for('index'))


@app.route('/photo/')
def photo():
    return render_template('photo_form.html')


@app.route('/task3/', methods=['GET', 'POST'])
def task3():
    check = {'Masha': 111, 'Dasha': 111, 'Sasha': 111, 'Kasha': 111}
    if request.method == "post":
        l = request.form.get('login')
        p = request.form.get('password')
        if l in check.keys() and p == check['l']:
            return redirect(url_for('greet.html', username=l))
        else:
            flash('Произошла ошибка', 'danger')
            return redirect(url_for('task3'))
    return render_template('task3.html')


@app.route('/task4', methods=['GET', 'POST'])
def task4():
    if request.method == 'POST':
        text = request.form['text']
        word_count = len(text.split())
        return redirect(url_for('result', word_count=word_count))
    return render_template('task4.html')


@app.route('/result/<int:word_count>')
def result(word_count):
    return f"""Количество слов в тексте: {word_count}"""


@app.route('/task5', methods=['GET', 'POST'])
def task5():
    if request.method == 'POST':
        n1 = request.form.get('n1')
        n2 = request.form.get('n2')
        oper = request.form.get('oper')
        if oper in '+_/*':
            if oper == '+':
                sum_nums = int(n1) + int(n2)
                return redirect(url_for('calc', res=sum_nums))
            elif oper == '-':
                min_nums = int(n1) - int(n2)
                return redirect(url_for('calc', res=min_nums))
            elif oper == '*':
                mult_nums = int(n1) * int(n2)
                return redirect(url_for('calc', res=mult_nums))
            elif oper == '/':
                div_nums = int(n1) / int(n2)
                return redirect(url_for('calc', res=div_nums))
            else:
                flash('Допустимые операции - +, -, /, *', 'danger')
                return redirect(url_for('task5'))
    return render_template('task5.html')


@app.route('/calc/<int:res>')
def calc(res):
    return render_template('task5_back.html', res=res)



if __name__ == '__main__':
    app.run(debug=True)

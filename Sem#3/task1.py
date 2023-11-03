from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from models import db, Student, Department

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mysite.db'
db = SQLAlchemy(app)

@app.route('/')
def index():
    # db.create_all()
    return render_template('base.html', title = 'Приветствие')

@app.route('/register/', methods=['POST', 'GET'])
def register():
    if request.method == 'post':
        name = request.form['name']
        surname = request.form['surname']
        age = request.form['age']
        gender = request.form['gender']
        group = request.form['group']
        department = request.form['department']
        student = Student(name=name, surname=surname, age=age, group=group, gender=gender, dep=department)
        db.session.add(student)
        db.session.commit()
    return render_template('register.html')

if __name__ == '__main__':
   app.run(debug=True)
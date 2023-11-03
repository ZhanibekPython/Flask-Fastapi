from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Student(db.Model):
    __tablename__ = 'Students'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    surname = db.Column(db.String(80), unique=True, nullable=False)
    age = db.Column(db.Integer)
    gender = db.Column(db.Enum('male', 'female'))
    group = db.Column(db.String, nullable=False)
    departments = db.Column(db.String(80), db.ForeignKey('department.id'))

    def __repr__(self):
        return f'users {self.id}'

class Department(db.Model):
    __tablename__ = 'Departments'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    dep_id = db.relationship('Student', backref='department', lazy=True)


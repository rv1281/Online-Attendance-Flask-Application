from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=func.now())
    status = db.Column(db.String(20))
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    student = db.relationship('Student', backref=db.backref('attendances', lazy=True))

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    roll_number = db.Column(db.Integer, unique=True)
    attended = db.Column(db.Integer, default=0)
    missed = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', back_populates='student_relationships')

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    firstName = db.Column(db.String(20))
    lastName = db.Column(db.String(20))
    student_relationships = db.relationship('Student', viewonly=True, back_populates='user', overlaps='user, user_relationship')
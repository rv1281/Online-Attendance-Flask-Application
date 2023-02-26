from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from . import db
from . models import User, Attendance, Student
import json


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])

def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Login successful.', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.dashboard'))
            else:
                flash('Incorrect password. Try again.', category='error')
        else:
            flash('User not found.', category='error')
    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('views.home'))


@auth.route('/sign_up', methods=['GET', 'POST'])

def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email is already in use. Please choose another.', category= 'error')
        elif len(email) < 4:
            flash('Email is too short.', category='error')
        elif len(firstName) < 2:
            flash('First name must be greater than 2 characters.', category='error')
        elif len(lastName) <2:
            flash('Last name must be greater than 2 characters.', category='error')
        elif len(password1) < 8:
            flash('Password must be greater than 8 characters.', category='error')
        elif password1 != password2:
            flash('Passwords do not match.', category='error')
        else:
            new_user = User(email=email, firstName=firstName, lastName=lastName,password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account successfully created.', category='success')
            return redirect(url_for('views.home'))


    return render_template("sign_up.html", user=current_user)

#Marking of attendance

@auth.route('/mark_attendance', methods=['GET', 'POST'])
@login_required
def mark_attendance():
    students = Student.query.all()
    if request.method == 'POST':
        student_id = request.form.get('student_id')
        student = Student.query.filter_by(id=student_id).first()
        attendance_status = request.form.get('attendance')
        if attendance_status == 'Present':
            attendance = Attendance(status=attendance_status, student_id=student_id)
            db.session.add(attendance)
            db.session.commit()
            student.attended += 1
            db.session.commit()
            flash("Attendance marked successfully!", "success")
        else:
            attendance = Attendance(status=attendance_status, student_id=student_id)
            db.session.add(attendance)
            db.session.commit()
            student.missed += 1
            db.session.commit()
            flash("Attendance marked successfully!", "success")
    return render_template('mark_attendance.html', user=current_user, students=students)


@auth.route('/view_attendance', methods=['GET', 'POST'])
@login_required
def view_attendance():
    students = Student.query.all()
    attendance_data = []
    for student in students:
        attended = Attendance.query.filter_by(student_id=student.id, status="Present").count()
        missed = Attendance.query.filter_by(student_id=student.id, status="Absent").count()
        total = attended + missed
        if total == 0:
            percentage = 0
        else:
            percentage = (attended / total) * 100
        attendance_data.append({
            "name": student.name,
            "roll_number": student.roll_number,
            "attended": attended,
            "missed": missed,
            "percentage": percentage,
            "id": student.id
        })
    return render_template('view_attendance.html', user=current_user, attendance_data=attendance_data)

@auth.route('/add_student', methods=['GET', 'POST'])
@login_required
def add_student():
    if request.method == 'POST':
        name = request.form.get('name')
        roll_number = request.form.get('roll_number')
        if not name or not roll_number:
            flash('Name and roll number are required', category='error')
            return redirect(url_for('auth.add_student'))
        if not roll_number.isdigit():
            flash('Roll number must be a valid integer', category='error')
            return redirect(url_for('auth.add_student'))
        if roll_number <= '0':
            flash('Roll number cannot be less than or equal to 0')
            return redirect(url_for('auth.add_student'))
        student = Student.query.filter_by(roll_number=roll_number).first()
        if student:
            flash('A student with this roll number already exists', category='error')
            return redirect(url_for('auth.add_student'))
        new_student = Student(name=name, roll_number=roll_number,user_id=current_user.id)
        db.session.add(new_student)
        db.session.commit()
        flash('Student added successfully', category='success')
        return redirect(url_for('auth.add_student'))
    return render_template('add_student.html', user=current_user)

@auth.route('/delete-student/<int:id>', methods=['POST'])
def delete_student(id):
    student = Student.query.get(id)
    if student:
        if student.user_id == current_user.id:
            db.session.delete(student)
            db.session.commit()
            flash('Student deleted successfully', category='success')
        else:
            flash('You are not authorized to delete this student.', 'danger')

    return redirect(request.referrer)
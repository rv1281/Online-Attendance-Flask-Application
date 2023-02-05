
# Online Attendance Flask Application

This is a basic Flask-based application that allows a teacher to sign up, log in, add students, and mark their attendance.

The application uses HTML and CSS along with Bootstrap for designing the user interface. Bootstrap provides a responsive and user-friendly design which makes the application easily accessible on various devices and screen sizes.


## Tech Stack

The Online Attendance Flask Application uses the following technologies:

- Flask: a micro web framework for Python
- Flask-Login: a Flask extension that provides user session management
- Flask-SQLAlchemy: a Flask extension that provides support for SQLAlchemy, a SQL toolkit and Object-Relational Mapping (ORM) library for Python
- SQLAlchemy: a SQL toolkit and ORM library for Python
- Werkzeug: a WSGI utility library for Python used by Flask as the underlying technology for the development server and debugger

## Installation

Install my-project with npm

- Clone the repository to your local machine

```python
    git clone https://github.com/[username]/Online-Attendance-Flask-Application.git
```
- Create a virtual environment and activate it

```python
    python3 -m venv venv

    source venv/bin/activate
```
- Install the required packages
```python
    pip install -r requirements.txt
```
- Set the environment variables
```python
    export FLASK_APP=app
    export FLASK_ENV=development
```
- Run the application
```python
    flask run
```
    
## Usage

After running the application, open your web browser and go to http://localhost:5000. From there, you can sign up as a teacher and log in to the application. You will then be able to add students and mark their attendance.
The application has a simple user interface that allows the teacher to add students, view their profiles, and mark their attendance. The attendance information is stored in a SQLite database, which is managed using SQLAlchemy.

The Flask-Login module is used to handle user authentication, and users can log in with their email address and password. The application also provides a secure password hashing mechanism using the Werkzeug library.

To run the application, simply install the required packages using pip, and then run the app.py file. The application will be available at http://localhost:5000.

It's a simple project that can be used as a starting point for a more complex online attendance system. With some modifications and additional features, it can be turned into a full-fledged application that can be used by schools, colleges, or any other organizations to manage their student attendance.

## Database

The application uses SQLite as its database and creates the database automatically as soon as the main.py script is run. The teacher's name, email, and password are stored in the database upon sign up, and the students' names and roll numbers are added to the database when the teacher logs in and adds them. The attendance is also stored in the database.

## Screenshots

Homepage

![Homepage](https://github.com/rv1281/Online-Attendance-Flask-Application/blob/main/screenshots/Homepage.jpg)

Sign-Up

![SignUp](https://github.com/rv1281/Online-Attendance-Flask-Application/blob/main/screenshots/SignUp.jpg)

Login

![Login](https://github.com/rv1281/Online-Attendance-Flask-Application/blob/main/screenshots/Login.jpg)

User-Dashboard

![Dashboard](https://github.com/rv1281/Online-Attendance-Flask-Application/blob/main/screenshots/Dashboard.jpg)

Add-Student Page

![Add Student](https://github.com/rv1281/Online-Attendance-Flask-Application/blob/main/screenshots/Add%20Student.jpg)

Mark Attendance Page

![Mark Attendance](https://github.com/rv1281/Online-Attendance-Flask-Application/blob/main/screenshots/MarkAttendance.jpg)

View Attendance Page

![View Attendance](https://github.com/rv1281/Online-Attendance-Flask-Application/blob/main/screenshots/View%20Attendance.jpg)

Databases

![Database-User](https://github.com/rv1281/Online-Attendance-Flask-Application/blob/main/screenshots/Database.jpg)

![Database-Student](https://github.com/rv1281/Online-Attendance-Flask-Application/blob/main/screenshots/Database2.jpg)

![Database-Attendance](https://github.com/rv1281/Online-Attendance-Flask-Application/blob/main/screenshots/Database3.jpg)

## Contributions

The Online Attendance Flask Application is open source and always looking for contributions to make it better. Whether you are a beginner or an experienced developer, you can help by fixing bugs, adding new features, or improving documentation.

Some ways to contribute include:

- Fixing bugs: If you come across a bug, you can submit a fix to help improve the application.

- Adding new features: If you have an idea for a new feature, you can submit a pull request with your implementation.

- Improving documentation: If you find any errors or unclear sections in the documentation, you can submit a fix to improve it.

- Testing: You can test the application and report any bugs or issues you come across.

To contribute, simply fork the repository, make your changes, and then submit a pull request. Before submitting a pull request, make sure to test your changes thoroughly and ensure that they are properly documented.
The development team will review your changes and provide feedback before merging them into the main codebase.

Please note that all contributions should follow the project's code of conduct and should adhere to the project's coding standards and guidelines.

I welcome all contributions, big or small, and appreciate your help in making the Online Attendance Flask Application even better!

from functools import wraps

from flask import request, render_template, redirect, url_for, escape, session

from simple_app import app, db
from simple_app.models import UserProfile


def valid_login(username, password):
    """ User login validation function """
    if username and password:
        profile = UserProfile.query.filter_by(username=username).first()
        if profile and profile.password == password:
            return True


def log_the_user_in(username):
    """ User login function """
    session['logged_in'] = True
    session['username'] = username


def login_required(f):
    """ Login required decorator to protect resources from anonymous access """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('logged_in'):
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function


@app.route('/')
@login_required
def index():
    return redirect(url_for('profile'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if session.get('logged_in'):
        return redirect(url_for('profile'))
    error = None
    if request.method == 'POST':
        username = escape(request.form.get('username'))
        password = escape(request.form.get('password'))
        if valid_login(username, password):
            log_the_user_in(username)
            return redirect(url_for('profile'))
        else:
            error = 'Invalid username/login'
    return render_template('login.html', error=error)


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    error = None
    if request.method == 'POST':
        username = escape(request.form.get('username'))
        if username and not UserProfile.query.filter_by(
                username=username).first():
            password = escape(request.form.get('password'))
            password2 = escape(request.form.get('password2'))
            if password and password == password2:
                lastname = escape(request.form.get('lastname'))
                firstname = escape(request.form.get('firstname'))
                if lastname and firstname:
                    user = UserProfile(
                        username=username,
                        password=password,
                        lastname=lastname,
                        firstname=firstname)
                    db.session.add(user)
                    db.session.commit()
                    log_the_user_in(username)
                    return redirect(url_for('profile'))
                else:
                    error = 'Lastname/Firstname fields are empty'
            else:
                error = 'Passwords not match/or passwords fields are empty'
        else:
            error = 'Username already exists/or username field is empty'
    return render_template('registration.html', error=error)


@app.route('/logout', methods=['POST'])
@login_required
def logout():
    session.pop('username', None)
    session.pop('logged_in', None)
    return redirect(url_for('login'))


@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    error = None
    username = escape(session.get('username'))
    user = UserProfile.query.filter_by(username=username).first()
    if request.method == 'POST':
        password = escape(request.form.get('password'))
        password2 = escape(request.form.get('password2'))
        if password and password == password2:
            lastname = escape(request.form.get('lastname'))
            firstname = escape(request.form.get('firstname'))
            if lastname and firstname:
                user.password = password
                user.lastname = lastname
                user.firstname = firstname
                db.session.commit()
            else:
                error = 'Lastname/Firstname fields are empty'
        else:
            error = 'Passwords not match/or passwords fields are empty'
    return render_template('profile.html', user=user, error=error)

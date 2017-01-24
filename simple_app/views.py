from flask import request, render_template

from simple_app import app


@app.route('/')
def index():
    return 'Hello World!'


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'], request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/login'
    return render_template('login.html', error=error)


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    pass


@app.route('/logout', methods=['POST'])
def logout():
    pass


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    pass

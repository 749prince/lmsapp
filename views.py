from flask import render_template, redirect, url_for, flash
from app import app, db
from model import User
from forms import LoginForm

@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        # Query the database for the user
        user = User.query.filter_by(username=username).first()

        # Password verification logic (consider using hashing in production)
        if user and user.password == password:
            flash('Login Successful', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check your username and password', 'danger')

    return render_template('login.html', form=form)

@app.route('/home')
def home():
    return render_template('home.html')




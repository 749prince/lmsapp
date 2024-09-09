from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with your actual secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:7070983825Qw%40%23@localhost/prince'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import routes from views.py
from views import *

if __name__ == '__main__':
    app.run(debug=True)

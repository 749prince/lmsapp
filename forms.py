from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=50)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=200)])
    submit = SubmitField('Login')

class AdminForm(FlaskForm):
    action = SelectField('Action', choices=[('add', 'Add Program'), ('view', 'View Programs')])
    submit = SubmitField('Submit')

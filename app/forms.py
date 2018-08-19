from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, Length


class LoginEmailForm(Form):
    login_email = StringField('login_email',
                              validators=[DataRequired(), Email(), Length(5, 120)],
                              render_kw={"placeholder": "Enter your email"})
    login_password = PasswordField('login_password',
                                 validators=[DataRequired(), Length(3)],
                                 render_kw={"placeholder": "Enter your email"})

class RegistrationForm(Form):
    email = StringField('email',
                        validators=[DataRequired(), Email(), Length(5, 120)],
                        render_kw={"placeholder": "Enter your email"})
    password = PasswordField('password',
                           validators=[DataRequired(), Length(3)],
                           render_kw={"placeholder": "Enter your password"})

class SearchForm(Form):
    search_field = StringField('search',
                               validators=[DataRequired()],
                               render_kw={"placeholder": "Enter your phrase"})

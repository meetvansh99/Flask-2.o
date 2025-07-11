from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,Length

class Registration(FlaskForm):
    name=StringField("Your name",validators=[DataRequired()])
    email=StringField("Your email",validators=[DataRequired(),Email()])
    password=PasswordField("Your password",validators=[DataRequired(),Length(min=6)])
    submit=SubmitField("Registor")
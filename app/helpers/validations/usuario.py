from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField
from wtforms.validators import InputRequired, Email, Length

class FormularioCreacionUsuario(FlaskForm):
    email = StringField('email', validators=[
        InputRequired(message="El campo de email esta vacío."),
        Length(max=30, message="El email no puede superar los 30 caracteres."),
        Email(message="El formato del correo electrónico no es válido.")
    ])
    username = StringField('username', validators=[
        InputRequired(message="El campo de nombre de usuario esta vacío."),
        Length(max=30, message="El nombre de usuario no puede superar los 30 caracteres.")
    ])
    password = StringField('password', validators=[
        InputRequired(message="El campo de contraseña esta vacío"),
        Length(max=30, message="La contraseña no puede superar los 30 caracteres.")
    ])
    firstname = StringField('firstname', validators=[
        InputRequired(message="El campo de nombre esta vacío"),
        Length(max=30, message="El nombre no puede superar los 30 caracteres.")
    ])
    lastname = StringField('lastname', validators=[
        InputRequired(message="El campo de apellido esta vacío"),
        Length(max=30, message="El apellido no puede superar los 30 caracteres.")
    ])

class FormularioActualizarUsuario(FlaskForm):
    email = StringField('email', validators=[
        InputRequired(message="El campo correo electrónico esta vacío."),
        Length(max=30, message="El correo electrónico no puede superar los 30 caracteres."),
        Email(message="El formato del correo electrónico no es válido.")
    ])
    username = StringField('username', validators=[
        InputRequired(message="El campo de nombre de usuario esta vacío."),
        Length(max=30, message="El nombre de usuario no puede superar los 30 caracteres.")
    ])
    password = StringField('password', validators=[
        InputRequired(message="El campo de contraseña esta vacío"),
        Length(max=30, message="La contraseña no puede superar los 30 caracteres.")
    ])
    firstname = StringField('firstname', validators=[
        InputRequired(message="El campo de nombre esta vacío"),
        Length(max=30, message="El nombre no puede superar los 30 caracteres.")
    ])
    lastname = StringField('lastname', validators=[
        InputRequired(message="El campo de apellido esta vacío"),
        Length(max=30, message="El apellido no puede superar los 30 caracteres.")
    ])
  
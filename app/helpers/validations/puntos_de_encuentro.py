from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField
from wtforms.validators import InputRequired, Email, Length

class FormularioCreacionPuntoDeEncuentro(FlaskForm):
    nombre = StringField('nombre', validators=[
        InputRequired(message="El campo de nombre esta vacío."),
        Length(max=150, message="El nombre no puede superar los 150 caracteres."),
    ])
    direccion = StringField('direccion', validators=[
        InputRequired(message="El campo de dirección esta vacío."),
        Length(max=150, message="La dirección no puede superar los 150 caracteres.")
    ])
    longitud = StringField('longitud', validators=[
        InputRequired(message="El campo de longitud esta vacío"),
        Length(max=30, message="La longitud no puede superar los 30 caracteres.")
    ])
    latitud = StringField('latitud', validators=[
        InputRequired(message="El campo de latitud esta vacío"),
        Length(max=30, message="La latitud no puede superar los 30 caracteres.")
    ])
    telefono = StringField('telefono', validators=[
        InputRequired(message="El campo de teléfono esta vacío"),
        Length(max=30, message="El teléfono no puede superar los 30 caracteres.")
    ])
    email = StringField('email', validators=[
        InputRequired(message="El campo correo electronico esta vacío."),
        Length(max=150, message="El correo electrónico no puede superar los 150 caracteres."),
        Email(message="El formato del correo electrónico no es válido.")
    ])

class FormularioActualizarPuntoDeEncuentro(FlaskForm):
    nombre = StringField('nombre', validators=[
        InputRequired(message="El campo de nombre esta vacío."),
        Length(max=150, message="El nombre no puede superar los 150 caracteres."),
    ])
    direccion = StringField('direccion', validators=[
        InputRequired(message="El campo de dirección esta vacío."),
        Length(max=150, message="La dirección no puede superar los 150 caracteres.")
    ])
    longitud = StringField('longitud', validators=[
        InputRequired(message="El campo de longitud esta vacío"),
        Length(max=30, message="La longitud no puede superar los 30 caracteres.")
    ])
    latitud = StringField('latitud', validators=[
        InputRequired(message="El campo de latitud esta vacío"),
        Length(max=30, message="La latitud no puede superar los 30 caracteres.")
    ])
    telefono = StringField('telefono', validators=[
        InputRequired(message="El campo de teléfono esta vacío"),
        Length(max=30, message="El teléfono no puede superar los 30 caracteres.")
    ])
    email = StringField('email', validators=[
        InputRequired(message="El campo correo electrónico esta vacío."),
        Length(max=150, message="El correo electrónico no puede superar los 150 caracteres."),
        Email(message="El formato del correo electrónico no es válido.")
    ])

  
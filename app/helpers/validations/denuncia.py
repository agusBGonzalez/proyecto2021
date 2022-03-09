from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField
from wtforms.validators import InputRequired, Email, Length

from app.models.denuncia import Denuncia

class FormularioCreacionDenuncia(FlaskForm):
    titulo = StringField("titulo", validators=[
        InputRequired(message="El campo título esta vacío."),
        Length(max=100, message="El título no puede superar los 250 caracteres.")
    ])
    descripcion = StringField('descripcion', validators=[
        InputRequired(message="El campo de descripción esta vacío."),
        Length(max=250, message="La descripción no puede superar los 250 caracteres.")
    ])
    latitud = StringField('latitud', validators=[
        InputRequired(message="El campo de latitud esta vacío."),
        Length(max=30, message="La latitud no puede superar los 30 caracteres.")
    ])
    longitud = StringField('longitud', validators=[
        InputRequired(message="El campo de longitud esta vacío."),
        Length(max=30, message="La longitud no puede superar los 30 caracteres.")
    ])
    apellido = StringField('apellido', validators=[
        InputRequired(message="El campo de apellido denunciante esta vacío."),
        Length(max=100, message="La descripción no puede superar los 100 caracteres.")
    ])
    nombre = StringField('nombre', validators=[
        InputRequired(message="El campo de nombre denunciante esta vacío."),
        Length(max=100, message="La descripción no puede superar los 100 caracteres.")
    ])
    telcel = StringField('telcel', validators=[
        InputRequired(message="El campo del teléfono/celular del denunciante esta vacío."),
        Length(max=100, message="La descripción no puede superar los 100 caracteres.")
    ])
    email = StringField('email', validators=[
        InputRequired(message="El campo de email del denunciante esta vacío."),
        Length(max=100, message="El email no puede superar los 100 caracteres."),
        Email(message="El formato del correo electrónico no es válido.")
    ])

class AsignarUsuarioDenuncia(FlaskForm):
    idusuario = IntegerField("idusuario", validators=[
        InputRequired(message="Falta el atributo 'id'.")
    ])


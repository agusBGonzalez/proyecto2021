from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField
from wtforms.validators import InputRequired, Email, Length

class FormularioCreacionRecorridoDeEvacuacion(FlaskForm):
    nombre = StringField('nombre', validators=[
        InputRequired(message="El campo de nombre esta vacío."),
        Length(max=100, message="El nombre del recorrido de evacuación no puede superar los 100 caracteres."),
    ])
    descripcion = StringField('descripcion', validators=[
        InputRequired(message="El campo de descripción esta vacío"),
        Length(max=350, message="El descripción no puede superar los 350 caracteres.")
    ])

class FormularioActualizarRecorridoDeEvacuacion(FlaskForm):
    nombre = StringField('nombre', validators=[
        InputRequired(message="El campo de nombre esta vacío."),
        Length(max=100, message="El nombre del recorrido de evacuación no puede superar los 100 caracteres."),
    ])
    descripcion = StringField('descripcion', validators=[
        InputRequired(message="El campo de descripción esta vacío"),
        Length(max=350, message="El descripción no puede superar los 350 caracteres.")
    ])
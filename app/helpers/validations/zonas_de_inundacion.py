from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField
from wtforms.validators import InputRequired, Email, Length

class FormularioCreacionZonaDeInundacion(FlaskForm):
    codigo = StringField("codigo", validators=[
        InputRequired(message="El campo código esta vacío."),
        Length(max=100, message="El código no puede superar los 250 caracteres.")
    ])
    nombre = StringField('nombre', validators=[
        InputRequired(message="El campo de descripción esta vacío."),
        Length(max=250, message="La descripción no puede superar los 250 caracteres.")
    ])
    color = StringField('color', validators=[
        InputRequired(message="Se debe seleccionar un color.")
    ])
    # longitud1 = StringField('longitud1', validators=[
    #     InputRequired(message="El campo de longitud esta vacío."),
    #     Length(max=30, message="La longitud no puede superar los 30 caracteres.")
    # ])
    # latitud1 = StringField('latitud1', validators=[
    #     InputRequired(message="El campo de latitud esta vacío."),
    #     Length(max=30, message="La latitud no puede superar los 30 caracteres.")
    # ])
    # longitud2 = StringField('longitud2', validators=[
    #     InputRequired(message="El campo de longitud esta vacío."),
    #     Length(max=30, message="La longitud no puede superar los 30 caracteres.")
    # ])
    # latitud2 = StringField('latitud2', validators=[
    #     InputRequired(message="El campo de latitud esta vacío."),
    #     Length(max=30, message="La latitud no puede superar los 30 caracteres.")
    # ])
    # longitud3 = StringField('longitud3', validators=[
    #     InputRequired(message="El campo de longitud esta vacío."),
    #     Length(max=30, message="La longitud no puede superar los 30 caracteres.")
    # ])
    # latitud3 = StringField('latitud3', validators=[
    #     InputRequired(message="El campo de latitud esta vacío."),
    #     Length(max=30, message="La latitud no puede superar los 30 caracteres.")
    # ])

class FormularioActualizarZonaDeInundacion(FlaskForm):
    codigo = StringField("codigo", validators=[
        InputRequired(message="El campo código esta vacío."),
        Length(max=100, message="El código no puede superar los 250 caracteres.")
    ])
    nombre = StringField('nombre', validators=[
        InputRequired(message="El campo de descripción esta vacío."),
        Length(max=250, message="La descripción no puede superar los 250 caracteres.")
    ])
    color = StringField('color', validators=[
        InputRequired(message="Se debe seleccionar un color.")
    ])
    longitud1 = StringField('longitud1', validators=[
        InputRequired(message="El campo de longitud esta vacío."),
        Length(max=30, message="La longitud no puede superar los 30 caracteres.")
    ])
    latitud1 = StringField('latitud1', validators=[
        InputRequired(message="El campo de latitud esta vacío."),
        Length(max=30, message="La latitud no puede superar los 30 caracteres.")
    ])
    longitud2 = StringField('longitud2', validators=[
        InputRequired(message="El campo de longitud esta vacío."),
        Length(max=30, message="La longitud no puede superar los 30 caracteres.")
    ])
    latitud2 = StringField('latitud2', validators=[
        InputRequired(message="El campo de latitud esta vacío."),
        Length(max=30, message="La latitud no puede superar los 30 caracteres.")
    ])
    longitud3 = StringField('longitud3', validators=[
        InputRequired(message="El campo de longitud esta vacío."),
        Length(max=30, message="La longitud no puede superar los 30 caracteres.")
    ])
    latitud3 = StringField('latitud3', validators=[
        InputRequired(message="El campo de latitud esta vacío."),
        Length(max=30, message="La latitud no puede superar los 30 caracteres.")
    ])

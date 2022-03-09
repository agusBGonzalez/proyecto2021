import flask
from flask.helpers import flash
from app.db import db
from app.models.usuario import Usuario
from flask import (
    _request_ctx_stack,
    current_app,
    request,
    session,
    url_for,
    has_request_context,
)


def authenticated(session):
    return session.get("user")


def create_google(user):
    nuevo_usuario = Usuario(
        username=user.username,
        email=user.email,
        password=user.username,
        activo=bool(0),
    )
    db.session.add(nuevo_usuario)
    db.session.commit()
    return


def login_google(user):
    usuario = Usuario.query.filter(Usuario.email == user.email).first()

    if usuario.activo:
        session["user"] = usuario    
        flash("La sesión se inicio correctamente.")
    else:
        flash("un Administrador debe habilitar tu cuenta")
    return

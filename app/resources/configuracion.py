from flask import redirect, render_template, request, url_for, abort, session, flash
from app.helpers.auth import authenticated
from app.helpers.permission import check_permission
from app.models.configuracion import Configuracion
from app.db import db


def index():
    if not authenticated(session):
        abort(401)

    if not check_permission(session, permission="configuracion_index"):
        abort(403)

    configuracion = Configuracion.query.first()
    return render_template("configuracion.html", configuracion=configuracion)


def update():
    if not authenticated(session):
        abort(401)

    if not check_permission(session, permission="configuracion_index"):
        abort(403)

    nueva_configuracion = Configuracion.query.get(1)

    nuevo_orden_usuarios = request.form["orden_usuarios"]
    nuevo_orden_puntos = request.form["orden_puntos"]
    nuevo_orden_zonas = request.form["orden_zonas"]
    nuevo_orden_recorridos = request.form["orden_recorridos"]
    nueva_cantidad_usuarios = request.form["cantidad_usuarios"]
    nueva_cantidad_puntos = request.form["cantidad_puntos"]
    nueva_cantidad_zonas = request.form["cantidad_zonas"]
    nueva_cantidad_recorridos = request.form["cantidad_recorridos"]
    nuevo_tema_privado = request.form["tema_privado"]
    nuevo_tema_publico = request.form["tema_publico"]

    nueva_configuracion.cantidad_usuarios = nueva_cantidad_usuarios
    nueva_configuracion.cantidad_puntos = nueva_cantidad_puntos
    nueva_configuracion.cantidad_zonas = nueva_cantidad_zonas
    nueva_configuracion.cantidad_recorridos = nueva_cantidad_recorridos
    nueva_configuracion.orden_usuarios = nuevo_orden_usuarios
    nueva_configuracion.orden_puntos = nuevo_orden_puntos
    nueva_configuracion.orden_zonas = nuevo_orden_zonas
    nueva_configuracion.orden_recorridos = nuevo_orden_recorridos
    nueva_configuracion.tema_publico = nuevo_tema_publico
    nueva_configuracion.tema_privado = nuevo_tema_privado

    db.session.commit()

    flash("La operación se llevó a cabo con éxito")
    return redirect(url_for("configuracion_index"))

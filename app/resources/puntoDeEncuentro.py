from os import putenv
import re
from flask import redirect, render_template, request, url_for, abort, session, flash
from app.helpers.auth import authenticated
from app.helpers.permission import check_permission
from app.helpers.validations.puntos_de_encuentro import FormularioActualizarPuntoDeEncuentro, FormularioCreacionPuntoDeEncuentro
from app.models.puntoDeEncuentro import PuntoDeEncuentro
from app.models.configuracion import Configuracion
from app.db import db
from sqlalchemy import and_



def index():
    if not authenticated(session):
        abort(401)

    if not check_permission(session, permission="punto_encuentro_index"):
        abort(403) 

    conf = Configuracion.query.first()
    page = request.args.get("page", 1, type=int)

    search_value = request.form.get("search")

    if not search_value:
        search_value = request.args.get("search")

    if request.method == "GET" and search_value:
        select_value = request.args.get("select")
        select = select_value
        if select_value == "Publicado":
            select_value = 1
        else:
            select_value = 0
        search = "%{}%".format(search_value)

        if conf.orden_puntos == "ascendente":
            puntos = (
                PuntoDeEncuentro.query.filter(
                    PuntoDeEncuentro.nombre.like(search),
                    PuntoDeEncuentro.estado == select_value,
                )
                .order_by(PuntoDeEncuentro.nombre.asc())
                .paginate(page=page, per_page=conf.cantidad_puntos)
            )
            search = search.replace("%", "")

            return render_template(
                "puntos.html",
                puntos=puntos,
                search=search,
                select=select,
                configuracion=conf,
            )
        else:
            puntos = (
                PuntoDeEncuentro.query.filter(
                    PuntoDeEncuentro.nombre.like(search),
                    PuntoDeEncuentro.estado == select_value,
                )
                .order_by(PuntoDeEncuentro.nombre.desc())
                .paginate(page=page, per_page=conf.cantidad_puntos)
            )
            search = search.replace("%", "")

            return render_template(
                "puntos.html",
                puntos=puntos,
                search=search,
                select=select,
                configuracion=conf,
            )

    if conf.orden_puntos == "ascendente":
        puntos = PuntoDeEncuentro.query.order_by(
            PuntoDeEncuentro.nombre.asc()
        ).paginate(page=page, per_page=conf.cantidad_puntos)

        return render_template("puntos.html", puntos=puntos, configuracion=conf)
    else:
        puntos = PuntoDeEncuentro.query.order_by(
            PuntoDeEncuentro.nombre.desc()
        ).paginate(page=page, per_page=conf.cantidad_puntos)

        return render_template("puntos.html", puntos=puntos, configuracion=conf)


def create():
    if not authenticated(session):
        abort(401)

    if not check_permission(session, permission="punto_encuentro_new"):
        abort(403)

    # codigo de wtforms
    form = FormularioCreacionPuntoDeEncuentro()
    
    if form.validate_on_submit():
        existe_nombre = PuntoDeEncuentro.query.filter(
            PuntoDeEncuentro.nombre == request.form["nombre"]
            ).first()
        if existe_nombre:
            flash("Ya hay un punto de encuentro registrado con el nombre ingresado.")
            return redirect(url_for("puntos_index"))
        existe_coordenada = PuntoDeEncuentro.query.filter(
            PuntoDeEncuentro.lat == request.form["latitud"],
            PuntoDeEncuentro.long == request.form["longitud"],
            ).first()
        if existe_coordenada:
            flash("Ya hay un punto de encuentro registrado con la latitud y la longitud ingresadas.")
            return redirect(url_for("puntos_index"))
        nuevo_punto_de_encuentro = PuntoDeEncuentro(
            nombre=request.form.get("nombre"),
            direccion=request.form.get("direccion"),
            long=request.form.get("longitud"),
            lat=request.form.get("latitud"),
            estado=bool(1),
            telefono=request.form.get("telefono"),
            email=request.form.get("email"),
        )
        flash("Se creó exitosamente el punto de encuentro.")
        db.session.add(nuevo_punto_de_encuentro)
        db.session.commit()
    else:
        for x in range(0, len(form.errors)):
            error_msg = "".join(list(form.errors.values())[x]).strip("'[]")
            flash(error_msg, "error")

    return redirect(url_for("puntos_index"))

def updateEstado(id):
    if not authenticated(session):
        abort(401)

    if not check_permission(session, permission="punto_encuentro_index"):
        abort(403) 

    punto = PuntoDeEncuentro.query.get(id)
    punto.estado = not punto.estado
    db.session.commit()
    flash("Se actualizó el estado del punto de encuentro seleccionado.")
    return redirect(url_for("puntos_index"))

def update(id):
    if not authenticated(session):
        abort(401)

    if not check_permission(session, permission="punto_encuentro_update"):
        abort(403)

    form = FormularioActualizarPuntoDeEncuentro()

    if form.validate_on_submit():
        existe_nombre = PuntoDeEncuentro.query.filter(
            and_(
                PuntoDeEncuentro.nombre == request.form["nombre"],
                PuntoDeEncuentro.id != id,
            )
        ).first()
        if existe_nombre:
            flash("Ya hay un punto de encuentro registrado con el nombre ingresado.")
            return redirect(url_for("puntos_index"))
        existe_coordenada = PuntoDeEncuentro.query.filter(
            and_(
                PuntoDeEncuentro.long == request.form["longitud"],
                PuntoDeEncuentro.lat == request.form["latitud"],
                PuntoDeEncuentro.id != id,
            )
        ).first()
        if existe_coordenada:
            flash("Ya hay un punto de encuentro registrado con la latitud y la longitud ingresadas.")
            return redirect(url_for("puntos_index"))
        punto_de_encuentro = PuntoDeEncuentro.query.get(id)
        punto_de_encuentro.nombre = request.form["nombre"]
        punto_de_encuentro.direccion = request.form["direccion"]
        punto_de_encuentro.long = request.form["longitud"]
        punto_de_encuentro.lat = request.form["latitud"]
        punto_de_encuentro.telefono = request.form["telefono"]
        punto_de_encuentro.email = request.form["email"]

        db.session.commit()
        flash("Se actualizó exitosamente el punto de encuentro.")
    else:
        for x in range(0, len(form.errors)):
            error_msg = "".join(list(form.errors.values())[x]).strip("'[]")
            flash(error_msg, "error")
        
    return redirect(url_for("puntos_index"))

def delete(id):
    if not authenticated(session):
        abort(401)

    if not check_permission(session, permission="punto_encuentro_destroy"):
        abort(403)

    punto_de_encuentro = PuntoDeEncuentro.query.get(id)
    db.session.delete(punto_de_encuentro)
    db.session.commit()

    flash("Se eliminó exitosamente el punto de encuentro.")

    return redirect(url_for("puntos_index"))


def crear_punto():
    if not authenticated(session):
        abort(401)

    if not check_permission(session, permission="punto_encuentro_new"):
        abort(403)

    conf = Configuracion.query.first()

    return render_template("crear_punto.html", configuracion=conf)


def modificar_punto(id):
    if not authenticated(session):
        abort(401)

    if not check_permission(session, permission="punto_encuentro_update"):
        abort(403)

    conf = Configuracion.query.first()

    punto_de_encuentro = PuntoDeEncuentro.query.get(id)

    return render_template("modificar_punto.html", configuracion=conf, punto=punto_de_encuentro)
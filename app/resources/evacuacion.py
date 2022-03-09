from flask import redirect, render_template, request, url_for, abort, session, flash
from sqlalchemy.sql.sqltypes import Boolean
from app.helpers.auth import authenticated
from app.helpers.validations.recorrido_de_evacuacion import (
    FormularioActualizarRecorridoDeEvacuacion,
    FormularioCreacionRecorridoDeEvacuacion,
)
from app.models.evacuacion import Evacuacion
from app.models.evacuacion import CoordenadasEvacuacion
from app.models.configuracion import Configuracion
from app.db import db
from sqlalchemy import and_, or_
from app.helpers.permission import check_permission
import ast


def index():
    if not authenticated(session):
        abort(401)

    if not check_permission(session, permission="ruta_evacuacion_index"):
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

        if conf.orden_recorridos == "ascendente":
            evacuacion = (
                Evacuacion.query.filter(
                    or_(
                        Evacuacion.nombre.like(search),
                        Evacuacion.descripcion.like(search),
                    ),
                    Evacuacion.estado == select_value,
                )
                .order_by(Evacuacion.nombre.asc())
                .paginate(page=page, per_page=conf.cantidad_recorridos)
            )
            search = search.replace("%", "")

            return render_template(
                "recorridoEvacuacion.html",
                evacuacion=evacuacion,
                search=search,
                select=select,
                configuracion=conf,
            )
        else:
            evacuacion = (
                Evacuacion.query.filter(
                    or_(
                        Evacuacion.nombre.like(search),
                        Evacuacion.descripcion.like(search),
                    ),
                    Evacuacion.estado == select_value,
                )
                .order_by(Evacuacion.nombre.desc())
                .paginate(page=page, per_page=conf.cantidad_recorridos)
            )
            search = search.replace("%", "")

            return render_template(
                "recorridoEvacuacion.html",
                evacuacion=evacuacion,
                search=search,
                select=select,
                configuracion=conf,
            )

    if conf.orden_recorridos == "ascendente":
        evacuacion = Evacuacion.query.order_by(Evacuacion.nombre.asc()).paginate(
            page=page, per_page=conf.cantidad_recorridos
        )

        return render_template(
            "recorridoEvacuacion.html", evacuacion=evacuacion, configuracion=conf
        )
    else:
        evacuacion = Evacuacion.query.order_by(Evacuacion.nombre.desc()).paginate(
            page=page, per_page=conf.cantidad_recorridos
        )

        return render_template(
            "recorridoEvacuacion.html", evacuacion=evacuacion, configuracion=conf
        )


def create():
    # posiblemente las coordenasas se pueden repetir

    if not authenticated(session):
        abort(401)
    if not check_permission(session, permission="ruta_evacuacion_new"):
        abort(403)

    # codigo de wtforms
    form = FormularioCreacionRecorridoDeEvacuacion()

    if form.validate_on_submit():
        existe_nombre = Evacuacion.query.filter(
            Evacuacion.nombre == request.form["nombre"]
        ).first()
        if existe_nombre:
            flash("Ya hay un recorrido de evacuación registrado con el nombre ingresado.")
            return redirect(url_for("evacuacion_index"))
        if not request.form["coordenadas"]:
            flash("Se deben cargar coordenadas para registrar el recorrido de evacuación.")
            return redirect(url_for("evacuacion_index"))    
        nuevo_recorrido = Evacuacion(
            nombre=request.form["nombre"],
            descripcion=request.form["descripcion"],
            estado=bool(1),
        )
        db.session.add(nuevo_recorrido)
        coordenadas = ast.literal_eval(request.form["coordenadas"])
        if len(coordenadas)<3:
            flash("Se deben seleccionar al menos 3 coordenadas para registrar el recorrido.")
            return redirect(url_for("evacuacion_index"))
        for coordenada in coordenadas:
            db.session.add(
                CoordenadasEvacuacion(
                    lat=coordenada[0],
                    long=coordenada[1],
                    evacuacion=nuevo_recorrido,
                )
            )
        db.session.commit()
        flash("Se creó exitosamente un nuevo recorrido de evacuación.")

    else:

        for x in range(0, len(form.errors)):
            error_msg = "".join(list(form.errors.values())[x]).strip("'[]")
            flash(error_msg, "error")

    return redirect(url_for("evacuacion_index"))


def update(id):
    if not authenticated(session):
        abort(401)
    if not check_permission(session, permission="ruta_evacuacion_update"):
        abort(403)

    form = FormularioActualizarRecorridoDeEvacuacion()

    if form.validate_on_submit():
        existe_nombre = Evacuacion.query.filter(
            and_(Evacuacion.nombre == request.form["nombre"], Evacuacion.id != id)
        ).first()
        if existe_nombre:
            flash("Ya hay un punto de encuentro registrado con el nombre ingresado.")
            return redirect(url_for("evacuacion_index"))
        if not request.form["coordenadas"]:
            flash("Se deben cargar coordenadas para registrar el recorrido de evacuación.")
            return redirect(url_for("evacuacion_index"))
        
        evacuacion = Evacuacion.query.get(id)
        evacuacion.nombre = (request.form["nombre"],)
        evacuacion.descripcion = (request.form["descripcion"],)
        coordenadas = ast.literal_eval(request.form["coordenadas"])
        if len(coordenadas)<3:
            flash("Se deben seleccionar al menos 3 coordenadas para registrar el recorrido.")
            return redirect(url_for("evacuacion_index"))
        db.session.delete(evacuacion)
        db.session.commit()

        evacuacion = Evacuacion(
            nombre=request.form["nombre"],
            descripcion=request.form["descripcion"],
            estado=bool(request.form["estado"]),
        )
        db.session.add(evacuacion)
        db.session.commit()

        coordenadas = ast.literal_eval(request.form["coordenadas"])
        for coordenada in coordenadas:
            db.session.add(
                CoordenadasEvacuacion(
                    lat=coordenada[0],
                    long=coordenada[1],
                    evacuacion=evacuacion,
                )
            )

        db.session.commit()

        flash("Se actualizó exitosamene el recorrido de evacuación.")

    else:

        for x in range(0, len(form.errors)):
            error_msg = "".join(list(form.errors.values())[x]).strip("'[]")
            flash(error_msg, "error")

    return redirect(url_for("evacuacion_index"))


def delete(id):
    if not authenticated(session):
        abort(401)

    if not check_permission(session, permission="ruta_evacuacion_destroy"):
        abort(403)
    borrarRecorridoEvacuacion = Evacuacion.query.get(id)
    db.session.delete(borrarRecorridoEvacuacion)
    db.session.commit()

    flash("Se borró exitosamente el recorrido de evacuación.")

    return redirect(url_for("evacuacion_index"))


def show(id):
    if not authenticated(session):
        abort(401)
    if not check_permission(session, permission="ruta_evacuacion_show"):
        abort(403)
    conf = Configuracion.query.first()
    evacuacion = Evacuacion.query.get(id)
    coords = 0

    for e in evacuacion.coordenadas:
        coords = coords + 1

    return render_template(
        "evacuacion_show.html", evacuacion=evacuacion, configuracion=conf, coords=coords
    )


def crear_recorrido():
    if not authenticated(session):
        abort(401)

    if not check_permission(session, permission="ruta_evacuacion_new"):
        abort(403)

    conf = Configuracion.query.first()

    return render_template("crear_recorrido.html", configuracion=conf)


def modificar_recorrido(id):
    if not authenticated(session):
        abort(401)

    if not check_permission(session, permission="ruta_evacuacion_update"):
        abort(403)

    conf = Configuracion.query.first()
    evacuacion = Evacuacion.query.get(id)
    return render_template(
        "modificar_recorrido.html",
        configuracion=conf,
        evacuacion=evacuacion,
    )

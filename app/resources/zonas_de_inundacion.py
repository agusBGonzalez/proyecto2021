from flask import redirect, render_template, request, url_for, abort, session, flash
from app.helpers.auth import authenticated
from app.helpers.permission import check_permission
from app.helpers.validations.zonas_de_inundacion import (
    FormularioCreacionZonaDeInundacion,
)
from app.models.zonas_de_inundacion import ZonaDeInundacion
from app.models.zonas_de_inundacion import CoordenadasZona
from app.db import db
from sqlalchemy import and_
from app.models.configuracion import Configuracion
import os
import csv
import ast


def index():

    if not authenticated(session):
        abort(401)

    if not check_permission(session, permission="zona_inundacion_index"):
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

        if conf.orden_zonas == "ascendente":
            zonas = (
                ZonaDeInundacion.query.filter(
                    ZonaDeInundacion.nombre.like(search),
                    ZonaDeInundacion.estado == select_value,
                )
                .order_by(ZonaDeInundacion.nombre.asc())
                .paginate(page=page, per_page=conf.cantidad_zonas)
            )
            search = search.replace("%", "")

            return render_template(
                "zonas.html",
                zonas=zonas,
                search=search,
                select=select,
                configuracion=conf,
            )
        else:
            zonas = (
                ZonaDeInundacion.query.filter(
                    ZonaDeInundacion.nombre.like(search),
                    ZonaDeInundacion.estado == select_value,
                )
                .order_by(ZonaDeInundacion.nombre.desc())
                .paginate(page=page, per_page=conf.cantidad_zonas)
            )
            search = search.replace("%", "")

            return render_template(
                "zonas.html",
                zonas=zonas,
                search=search,
                select=select,
                configuracion=conf,
            )

    if conf.orden_zonas == "ascendente":
        zonas = ZonaDeInundacion.query.order_by(ZonaDeInundacion.nombre.asc()).paginate(
            page=page, per_page=conf.cantidad_zonas
        )

        return render_template("zonas.html", zonas=zonas, configuracion=conf)
    else:
        zonas = ZonaDeInundacion.query.order_by(
            ZonaDeInundacion.nombre.desc()
        ).paginate(page=page, per_page=conf.cantidad_zonas)

        return render_template("zonas.html", zonas=zonas, configuracion=conf)


def create():

    if not authenticated(session):
        abort(401)

    if not check_permission(session, permission="zona_inundacion_new"):
        abort(403)

    # codigo de wtforms
    form = FormularioCreacionZonaDeInundacion()

    if form.validate_on_submit():
        existe_nombre = ZonaDeInundacion.query.filter(
            ZonaDeInundacion.nombre == request.form["nombre"]
        ).first()
        if existe_nombre:
            flash(
                "Ya existe una zona de inundación registrada con el nombre ingresado."
            )
            return redirect(url_for("zonas_index"))
        existe_codigo = ZonaDeInundacion.query.filter(
            ZonaDeInundacion.codigo == request.form["codigo"]
        ).first()
        if existe_codigo:
            flash(
                "Ya existe una zona de inundación registrada con el código ingresado."
            )
            return redirect(url_for("zonas_index"))
        if not request.form["coordenadas"]:
            flash("Se deben cargar coordenadas para registrar la zona de inundación.")
            return redirect(url_for("zonas_index"))

        nueva_zona = ZonaDeInundacion(
            codigo=request.form["codigo"],
            nombre=request.form["nombre"],
            estado=bool(request.form["estado"]),
            color=request.form["color"],
        )

        coordenadas = ast.literal_eval(request.form["coordenadas"])
        if len(coordenadas)<3:
            flash("Se deben seleccionar al menos 3 coordenadas para registrar la zona.")
            return redirect(url_for("zonas_index"))
        db.session.add(nueva_zona)
        for coordenada in coordenadas:
            db.session.add(
                CoordenadasZona(
                    lat=coordenada[0],
                    long=coordenada[1],
                    zona=nueva_zona,
                )
            )

        db.session.commit()
        flash("Se creó exitosamente una nueva zona de inundación.")

    else:
        for x in range(0, len(form.errors)):
            error_msg = "".join(list(form.errors.values())[x]).strip("'[]")
            flash(error_msg, "error")

    return redirect(url_for("zonas_index"))


def update(id):

    if not authenticated(session):
        abort(401)

    if not check_permission(session, permission="zona_inundacion_update"):
        abort(403)

    # codigo de wtforms
    form = FormularioCreacionZonaDeInundacion()

    if form.validate_on_submit():
        existe_nombre = ZonaDeInundacion.query.filter(
            and_(
                ZonaDeInundacion.nombre == request.form["nombre"],
                ZonaDeInundacion.id != id,
            )
        ).first()
        if existe_nombre:
            flash(
                "Ya existe una zona de inundación registrada con el nombre ingresado."
            )
            return redirect(url_for("zonas_index"))
        existe_codigo = ZonaDeInundacion.query.filter(
            and_(
                ZonaDeInundacion.codigo == request.form["codigo"],
                ZonaDeInundacion.id != id,
            )
        ).first()
        if existe_codigo:
            flash("Ya existe una zona de inundación registrada con el código ingresado.")
            return redirect(url_for("zonas_index"))
        if not request.form["coordenadas"]:
            flash("Se deben cargar coordenadas para registrar la zona de inundación.")
            return redirect(url_for("zonas_index"))
        
        zona = ZonaDeInundacion.query.get(id)
        
        coordenadas = ast.literal_eval(request.form["coordenadas"])
        if len(coordenadas)<3:
            flash("Se deben seleccionar al menos 3 coordenadas para registrar la zona.")
            return redirect(url_for("zonas_index"))

        db.session.delete(zona)
        db.session.commit()

        zona = ZonaDeInundacion(
            codigo=request.form["codigo"],
            nombre=request.form["nombre"],
            estado=bool(request.form["estado"]),
            color=request.form["color"],
        )
        db.session.add(zona)
        db.session.commit()

        for coordenada in coordenadas:
            db.session.add(
                CoordenadasZona(
                    lat=coordenada[0],
                    long=coordenada[1],
                    zona=zona,
                )
            )

        db.session.commit()

        flash("Se actualizó exitosamente la zona de inundación.")

    else:
        for x in range(0, len(form.errors)):
            error_msg = "".join(list(form.errors.values())[x]).strip("'[]")
            flash(error_msg, "error")

    return redirect(url_for("zonas_index"))


def delete(id):

    if not authenticated(session):
        abort(401)

    if not check_permission(session, permission="zona_inundacion_destroy"):
        abort(403)

    zona = ZonaDeInundacion.query.get(id)
    db.session.delete(zona)
    db.session.commit()

    flash("Se eliminó exitosamente la zona de inundación.")

    return redirect(url_for("zonas_index"))


def show(id):
    if not authenticated(session):
        abort(401)

    if not check_permission(session, permission="zona_inundacion_show"):
        abort(403)

    conf = Configuracion.query.first()
    zona = ZonaDeInundacion.query.get(id)
    coords = 0

    for coordenada in zona.coordenadas:
        coords = coords + 1

    return render_template(
        "zona_show.html", zona=zona, configuracion=conf, coords=coords
    )


def importing():
    if not authenticated(session):
        abort(401)

    if not check_permission(session, permission="zona_inundacion_new"):
        abort(403)

    archivo = request.files["archivo_csv"]

    if not archivo:
        flash("Por favor, seleccione un archivo.")
        return redirect(url_for("zonas_index"))

    ext = os.path.splitext(archivo.filename)
    if ext[1] == ".csv":
        dir_archivo = os.path.join(os.getcwd(), "app/static/uploads", archivo.filename)

        zonas_no_cargadas = 0

        archivo.save(dir_archivo)
        with open(dir_archivo, newline="") as archivo_csv:
            lectura = csv.reader(archivo_csv, delimiter=",")
            header = next(lectura)
            for row in lectura:

                existe_nombre = ZonaDeInundacion.query.filter(
                    ZonaDeInundacion.nombre == row[0]
                ).first()
                
                if not existe_nombre:
                    nueva_zona = ZonaDeInundacion(
                        codigo="",
                        nombre=row[0],
                        estado=False,
                        color="#000000",
                    )
                    db.session.add(nueva_zona)
                    db.session.commit()

                    coordenadas = ast.literal_eval(row[1])
                    for coordenada in coordenadas:
                        db.session.add(
                            CoordenadasZona(
                                lat=coordenada[0],
                                long=coordenada[1],
                                zona=nueva_zona,
                            )
                        )

                    db.session.commit()
                else:
                    zonas_no_cargadas = zonas_no_cargadas + 1
                    
        os.remove(dir_archivo)

        if zonas_no_cargadas:
            flash("Hubo {} zonas que no fueron cargadas porque ya se encuentran en el sistema.".format(zonas_no_cargadas))

        flash("Archivo procesado correctamente!")
        return redirect(url_for("zonas_index"))

    else:
        flash("Se debe de seleccionar archivos con extensión .csv")
        return redirect(url_for("zonas_index"))


def crear_zona():
    if not authenticated(session):
        abort(401)

    if not check_permission(session, permission="zona_inundacion_new"):
        abort(403)

    conf = Configuracion.query.first()

    return render_template("crear_zona.html", configuracion=conf)


def modificar_zona(id):
    if not authenticated(session):
        abort(401)

    if not check_permission(session, permission="zona_inundacion_update"):
        abort(403)

    conf = Configuracion.query.first()
    zona = ZonaDeInundacion.query.get(id)

    return render_template(
        "modificar_zona.html",
        configuracion=conf,
        zona=zona,
    )
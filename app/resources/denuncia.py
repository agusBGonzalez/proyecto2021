from flask import redirect, render_template, request, url_for, abort, session, flash
from datetime import datetime
from flask_session import Session
from sqlalchemy.sql.functions import now
from app.helpers.validations.denuncia import FormularioCreacionDenuncia, AsignarUsuarioDenuncia
from app.models.denuncia import Categoria, ComentariosSeguimiento, Denuncia
from app.models.usuario import Usuario
from app.models.configuracion import Configuracion
from app.models.rol import Rol
from app.helpers.auth import authenticated
from app.models.configuracion import Configuracion
from app.db import db
from app.helpers.permission import check_permission
from datetime import datetime


def index():
    if not authenticated(session):
        abort(401)

    if not check_permission(session, permission="denuncias_index"):
        abort(403)

    page = request.args.get("page", 1, type=int)
    conf = Configuracion.query.first()
    roles = Rol.query.all()
    usuarios = Usuario.query.all()
    categorias=Categoria.query.all()

    search_value = request.form.get("search")
    if not search_value:
        search_value = request.args.get("search")

    if request.method == "GET" and search_value:
        select_value = request.args.get("select")
        select = select_value

        if conf.orden_usuarios == "ascendente":
            if select_value == "Titulo":
                search = "%{}%".format(search_value)
                denuncias = ( Denuncia.query.filter(
                    Denuncia.titulo.like(search),
                ).order_by(Denuncia.titulo.asc())
                .paginate(page=page, per_page=conf.cantidad_usuarios)
                )
                search = search.replace("%", "")

            elif select_value == "Estado":
                search = "%{}%".format(search_value)
                denuncias = ( Denuncia.query.filter(
                    Denuncia.estado.like(search),
                ).order_by(Denuncia.estado.asc())
                .paginate(page=page, per_page=conf.cantidad_usuarios)
                )
                search = search.replace("%", "")

            elif select_value == "Fecha":
                search = "%{}%".format(search_value)
                denuncias = ( Denuncia.query.filter(
                    Denuncia.fecha_creacion.like(search),
                ).order_by(Denuncia.fecha_creacion.asc())
                .paginate(page=page, per_page=conf.cantidad_usuarios)
                )
                search = search.replace("%", "")
            else:
                search = "%{}%".format(search_value)
                denuncias = ( Denuncia.query.filter(
                    Denuncia.titulo.like(search),
                ).order_by(Denuncia.email.desc())
                .paginate(page=page, per_page=conf.cantidad_usuarios)
                )
                search = search.replace("%", "")

            return render_template(
                "denuncias.html",
                denuncias=denuncias,
                search=search,
                select=select,
                configuracion=conf,
                usuarios=usuarios,
                categorias=categorias
            )
        else:
            if select_value == "Titulo":
                search = "%{}%".format(search_value)
                denuncias = ( Denuncia.query.filter(
                    Denuncia.titulo.like(search),
                ).order_by(Denuncia.titulo.desc())
                .paginate(page=page, per_page=conf.cantidad_usuarios)
                )
                search = search.replace("%", "")

            elif select_value == "Estado":
                search = "%{}%".format(search_value)
                denuncias = ( Denuncia.query.filter(
                    Denuncia.estado.like(search),
                ).order_by(Denuncia.estado.desc())
                .paginate(page=page, per_page=conf.cantidad_usuarios)
                )
                search = search.replace("%", "")

            elif select_value == "Fecha":
                search = "%{}%".format(search_value)
                denuncias = ( Denuncia.query.filter(
                    Denuncia.fecha_creacion.like(search),
                ).order_by(Denuncia.fecha_creacion.desc())
                .paginate(page=page, per_page=conf.cantidad_usuarios)
                )
                search = search.replace("%", "")
            else:
                search = "%{}%".format(search_value)
                denuncias = ( Denuncia.query.filter(
                    Denuncia.titulo.like(search),
                ).order_by(Denuncia.email.desc())
                .paginate(page=page, per_page=conf.cantidad_usuarios)
                )
                search = search.replace("%", "")

            return render_template(
                "denuncias.html",
                denuncias=denuncias,
                search=search,
                select=select,
                configuracion=conf,
                usuarios=usuarios,
                categorias=categorias
            )

    if conf.orden_usuarios == "ascendente":
        denuncias = Denuncia.query.order_by(
            Denuncia.titulo.asc()
        ).paginate(page=page, per_page=conf.cantidad_usuarios)

        return render_template("denuncias.html", denuncias=denuncias, configuracion=conf,usuarios=usuarios,categorias=categorias)
    else:
        denuncias = Denuncia.query.order_by(
            Denuncia.titulo.desc()
        ).paginate(page=page, per_page=conf.cantidad_usuarios)

        return render_template("denuncias.html", denuncias=denuncias, configuracion=conf,usuarios=usuarios,categorias=categorias)

    
def create():
    conf = Configuracion.query.first()
    estado_aux = ""
    usuario_aux = None
    fecha_cierre_aux = ""
    if not authenticated(session):
        estado_aux = "Sin confirmar"
    else:
        estado_aux = "Resuelta"
        usuario_aux = session["user"].id
        fecha_cierre_aux = datetime.today().strftime('%Y-%m-%d')
    # codigo de wtforms
    form = FormularioCreacionDenuncia()
    #agregar validacion del id de la categoria, aca y en asignar usuario
    if form.validate_on_submit():
        aux_categoria = int(request.form["categoria"])
        nueva_denuncia = Denuncia(
            titulo=request.form["titulo"],
            fecha_creacion=datetime.today().strftime('%Y-%m-%d'),
            fecha_cierre=fecha_cierre_aux,
            descripcion=request.form["descripcion"],
            latitud=request.form["latitud"],
            longitud=request.form["longitud"],
            estado=estado_aux,
            apellido_denunciante=request.form["apellido"],
            nombre_denunciante=request.form["nombre"],
            telcel_denunciante=request.form["telcel"],
            email_denunciante=request.form["email"],
            categoria_id=aux_categoria,
            usuario_id=usuario_aux
        )
        db.session.add(nueva_denuncia)
        db.session.commit()

        flash("La denuncia se creó correctamente.")

    else:
        for x in range(0, len(form.errors)):
            error_msg = "".join(list(form.errors.values())[x]).strip("'[]")
            flash(error_msg, "error")

    return redirect(url_for("home"))


def asignar_usuario(id):

    form = AsignarUsuarioDenuncia()
    if form.validate_on_submit():
        usuario = Usuario.query.get(int(request.form["idusuario"]))
        denuncia = Denuncia.query.get(id)
        denuncia.usuario_id = usuario.id
        denuncia.estado = "En curso"
        usuario.denuncias.append(denuncia)
        usuario.comentario=""
        db.session.commit()
        flash("Se asignó correctamente el usuario a la denuncia.")
    else:
        for x in range(0, len(form.errors)):
            error_msg = "".join(list(form.errors.values())[x]).strip("'[]")
            flash(error_msg, "error")

    return redirect(url_for("denuncias_index"))


def delete(id):
    if not authenticated(session):
        abort(401)

    if not check_permission(session, permission="denuncias_destroy"):
        abort(403)
    if not authenticated(session):
        abort(401)

    denuncia = Denuncia.query.get(id)
    db.session.delete(denuncia)
    db.session.commit()
    flash("Se eliminó exitosamente la denuncia.")
    
    return redirect(url_for("denuncias_index"))

def seguimiento(id):
    if not authenticated(session):
        abort(401)

    if not check_permission(session, permission="denuncias_update"):
        abort(403)
    denuncia = Denuncia.query.get(id)
    respuesta = request.form["respuesta"]
    if respuesta:
        denuncia.estado = "Resuelta"
        denuncia.fecha_cierre=datetime.today().strftime('%Y-%m-%d')
        denuncia.comentario.append(ComentariosSeguimiento(comentario=request.form["comentario"], denuncia_id=id))
        flash("Se actualizó el estado de la denuncia a Resuelta.")
    else:
        if (denuncia.contador < 2):
            denuncia.contador=denuncia.contador+1
            denuncia.comentario.append(ComentariosSeguimiento(comentario=request.form["comentario"], denuncia_id=id))
            flash("Se contabilizo la llamada Realizada.")
        else:
            denuncia.estado = "Cerrada"
            denuncia.fecha_cierre=datetime.today().strftime('%Y-%m-%d')
            denuncia.comentario.append(ComentariosSeguimiento(comentario=request.form["comentario"], denuncia_id=id))
            denuncia.comentario.append(ComentariosSeguimiento(comentario="No fue posible contactar al denunciante", denuncia_id=id))
            flash("Se actualizó el estado de la denuncia a cerrrada.")
    db.session.commit()
    return redirect(url_for("denuncias_index"))

def mis_denuncias():
    usuarios = Usuario.query.all()
    categorias=Categoria.query.all()
    page = request.args.get("page", 1, type=int)
    conf = Configuracion.query.first()
    denuncias = ( Denuncia.query.filter(
        Denuncia.usuario_id == session["user"].id
        ).order_by(Denuncia.fecha_creacion.desc())
        .paginate(page=page, per_page=conf.cantidad_usuarios)
        )
    return render_template(
                "denuncias.html",
                denuncias=denuncias,
                configuracion=conf,
                usuarios=usuarios,
                categorias=categorias
            )

def show(id):
    if not authenticated(session):
        abort(401)
    conf = Configuracion.query.first()
    denuncia = Denuncia.query.get(id)

    return render_template(
        "denuncia_show.html",denuncia=denuncia, configuracion=conf
    )
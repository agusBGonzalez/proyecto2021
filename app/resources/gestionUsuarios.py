from flask import redirect, render_template, request, url_for, abort, session, flash
from sqlalchemy.sql.expression import false
from app.helpers.auth import authenticated
from app.models.usuario import Usuario
from app.models.configuracion import Configuracion
from app.models.rol import Rol
from app.models.permiso import Permiso
from app.db import db
from sqlalchemy import and_
from app.helpers.validations.usuario import FormularioCreacionUsuario, FormularioActualizarUsuario


def index():
    if not authenticated(session):
        abort(401)

    if not has_permission(session["user"].id, permission="usuario_index"):
        abort(403)

    page = request.args.get("page", 1, type=int)
    conf = Configuracion.query.first()
    roles = Rol.query.all()

    search_value = request.form.get("search")

    if not search_value:
        search_value = request.args.get("search")

    if request.method == "GET" and search_value:
        select_value = request.args.get("select")
        select = select_value
        if select_value == "Activo":
            select_value = 1
        else:
            select_value = 0
        search = "%{}%".format(search_value)

        if conf.orden_usuarios == "ascendente":
            users = (
                Usuario.query.filter(
                    Usuario.username.like(search), Usuario.activo == select_value
                )
                .order_by(Usuario.email.asc())
                .paginate(page=page, per_page=conf.cantidad_usuarios)
            )
            search = search.replace("%", "")

            return render_template(
                "gestionDeUsuarios.html",
                usuarios=users,
                search=search,
                select=select,
                configuracion=conf,
                roles=roles,
            )
        else:
            users = (
                Usuario.query.filter(
                    Usuario.username.like(search), Usuario.activo == select_value
                )
                .order_by(Usuario.email.desc())
                .paginate(page=page, per_page=conf.cantidad_usuarios)
            )
            search = search.replace("%", "")

            return render_template(
                "gestionDeUsuarios.html",
                usuarios=users,
                search=search,
                select=select,
                configuracion=conf,
                roles=roles,
            )

    if conf.orden_usuarios == "ascendente":
        users = Usuario.query.order_by(Usuario.email.asc()).paginate(
            page=page, per_page=conf.cantidad_usuarios
        )

        return render_template(
            "gestionDeUsuarios.html",
            usuarios=users,
            configuracion=conf,
            roles=roles,
        )
    else:
        users = Usuario.query.order_by(Usuario.email.desc()).paginate(
            page=page, per_page=conf.cantidad_usuarios
        )

        return render_template(
            "gestionDeUsuarios.html",
            usuarios=users,
            configuracion=conf,
            roles=roles,
        )


def create():
    if not authenticated(session):
        abort(401)

    if not has_permission(session["user"].id, permission="usuario_index"):
        abort(403)

    # codigo de wtforms
    form = FormularioCreacionUsuario()
    if form.validate_on_submit():
        existe_username = Usuario.query.filter(Usuario.username == request.form["username"]).first()
        if existe_username:
            flash("El nombre de usuario ingresado ya se encuentra registrado.")
            return redirect(url_for("user_index"))
        existe_email = Usuario.query.filter(Usuario.email == request.form["email"]).first()
        if existe_email:
            flash("El email ingresado ya se encuentra registrado.")
            return redirect(url_for("user_index"))
        #if request.form[str("rol.id")] == "":
        #    flash("Se debe seleccionar un rol.")
        #    return False
        nuevo_usuario = Usuario(
            email=request.form["email"],
            username=request.form["username"],
            password=request.form["password"],
            firstname=request.form["firstname"],
            lastname=request.form["lastname"],
            activo=bool(1),
        )
        roles = Rol.query.all()
        for rol in roles:
            if request.form.get(str(rol.id)):
                nuevo_usuario.roles.append(rol)

        db.session.add(nuevo_usuario)
        db.session.commit()
        flash("Se creó correctamente el usuario en el sistema.")
    else:
        for x in range(0, len(form.errors)):
            error_msg = "".join(list(form.errors.values())[x]).strip("'[]")
            flash(error_msg, "error")

    return redirect(url_for("user_index"))

def updateEstado(id):
    if not authenticated(session):
        abort(401)

    if not has_permission(session["user"].id, permission="usuario_index"):
        abort(403)

    usuario = Usuario.query.get(id)
    usuario.activo = not usuario.activo
    db.session.commit()
    flash("Se actualizó el estado del usuario seleccionado.")
    return redirect(url_for("user_index"))


def update(id):
    if not authenticated(session):
        abort(401)

    if not has_permission(session["user"].id, permission="usuario_index"):
        abort(403)

    form = FormularioActualizarUsuario()
    if form.validate_on_submit():
        existeUsername = Usuario.query.filter(
            and_(Usuario.username == request.form["username"], Usuario.id != id)
            ).first()
        if existeUsername:
            flash("No se puede actualizar debido a que ya existe este Nombre de Usuario.")
            return redirect(url_for("user_index"))
        existeEmail = Usuario.query.filter(
            and_(Usuario.email == request.form["email"], Usuario.id != id)
            ).first()
        if existeEmail:
            flash("No se puede actualizar debido a que ya existe este Email.")
            return redirect(url_for("user_index"))
        usuario = Usuario.query.get(id)
        usuario.email = request.form["email"]
        usuario.username = request.form["username"]
        usuario.password = request.form["password"]
        usuario.firstname = request.form["firstname"],
        usuario.lastname = request.form["lastname"],

        roles = Rol.query.all()
        for rol in roles:
            if request.form.get(str(rol.id)):
                usuario.roles.append(rol)
        db.session.commit()
        flash("Se actualizó exitosamente el usuario.")
    else:
        for x in range(0, len(form.errors)):
            error_msg = "".join(list(form.errors.values())[x]).strip("'[]")
            flash(error_msg, "error")

    return redirect(url_for("user_index"))


def delete(id):
    if not authenticated(session):
        abort(401)

    if not has_permission(session["user"].id, permission="usuario_index"):
        abort(403)

    borrar_usuario = Usuario.query.get(id)
    db.session.delete(borrar_usuario)
    db.session.commit()

    flash("Se borró exitosamente el usuario seleccionado.")
    return redirect(url_for("user_index"))


def has_permission(user_id, permission):
    usuario = Usuario.query.get(user_id)

    for rol in usuario.roles:
        for permiso in rol.permisos:
            if permiso.nombre == permission:
                return True
    return False


def has_rol(user_id, rol):
    usuario = Usuario.query.get(user_id)

    for un_rol in usuario.roles:
        if un_rol.nombre == rol:
            return True
    return False

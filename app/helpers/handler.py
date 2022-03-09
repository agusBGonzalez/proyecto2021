from flask import render_template, jsonify, request
from app.models.configuracion import Configuracion


def not_found_error(e):
    kwargs = {
        "error_name": "404 Not Found Error",
        "error_description": "El servidor no puede encontrar el recurso solicitado.",
    }
    if request.path.startswith("/api/"):
        return jsonify(kwargs), 404
    else:
        conf = Configuracion.query.first()
        return render_template("error.html", **kwargs, configuracion=conf), 404


def unauthorized_error(e):
    kwargs = {
        "error_name": "401 Unauthorized Error",
        "error_description": "No está autorizado para acceder a la URL.",
    }
    conf = Configuracion.query.first()
    return render_template("error.html", **kwargs, configuracion=conf), 401


def forbidden_error(e):
    kwargs = {
        "error_name": "403 Forbidden Error",
        "error_description": "Se le niega el acceso a esta acción.",
    }
    conf = Configuracion.query.first()
    return render_template("error.html", **kwargs, configuracion=conf), 403 


def internal_server_error(e):
    kwargs = {
        "error_name": "500 Internal Server Error",
        "error_description": "el servidor encontró una condición inesperada que le impide completar la petición.",
    }
    if request.path.startswith("/api/"):
        return jsonify(kwargs), 500
    else:
        conf = Configuracion.query.first()
        return render_template("error.html", **kwargs, configuracion=conf), 500 

def bad_request(e):
    kwargs = {
        "error_name": "400 Bad Request",
        "error_description": "El servidor no puede procesar la petición debido a que se produjo un error del cliente.",
    }
    if request.path.startswith("/api/"):
        return jsonify(kwargs), 400
    else:
        conf = Configuracion.query.first()
        return render_template("error.html", **kwargs, configuracion=conf), 400
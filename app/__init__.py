from os import path, environ, urandom
import os
from flask import Flask, app, render_template, g, Blueprint
from flask_cors import CORS
from flask_session import Session
from config import config
from app import db
from app.helpers import handler
from app.helpers import auth as helper_auth
from app.helpers import permission as helper_permission
from app.helpers import rol as helper_rol
from app.resources import auth
from app.resources import puntoDeEncuentro
from app.resources import gestionUsuarios
from app.resources import configuracion
from app.resources import evacuacion
from app.resources import zonas_de_inundacion
from app.resources import denuncia
from app.models.denuncia import Categoria
from app.models.configuracion import Configuracion
from app.models.puntoDeEncuentro import PuntoDeEncuentro
from app.resources.api.zonas import zonas_api
from flask_wtf.csrf import CSRFProtect, CSRFError
from app.resources.api.puntos import puntos_api
from app.resources.api.evacuacion import evacuacion_api
from app.resources.api.denuncias import denuncias_api
from app.resources.api.categorias import categorias_api
import os
#diego
from oauthlib.oauth2 import WebApplicationClient
from flask_login import (LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
    )

# Diego Configuration
GOOGLE_CLIENT_ID = '601314239994-k5rm5bcocthfrpmcr7ti2e0ofqo9qs3k.apps.googleusercontent.com'
GOOGLE_CLIENT_SECRET = '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'
GOOGLE_DISCOVERY_URL = (
    "https://accounts.google.com/.well-known/openid-configuration"
)

def create_app(environment="development"):
    # Configuración inicial de la app
    app = Flask(__name__)
    CORS(app)
    
    #Diego
    app.secret_key = environ.get("SECRET_KEY") or urandom(24)
    
    # OAuth 2 client setup
    client = WebApplicationClient(GOOGLE_CLIENT_ID)
    
    login_manager = LoginManager()
    login_manager.init_app(app)
    
    
    @login_manager.user_loader
    def load_user(user_id):
        return gestionUsuarios.get(user_id)


    # Carga de la configuración
    env = environ.get("FLASK_ENV", environment)
    app.config.from_object(config[env])

    # Protección CSRF
    csrf = CSRFProtect(app)
    app.config["WTF_CSRF_TIME_LIMIT"] = None
    app.config["WTF_CSRF_ENABLED"] = False

    # Server Side session
    app.config["SESSION_TYPE"] = "filesystem"
    Session(app)

    # Configure db
    db.init_app(app)

    # Funciones que se exportan al contexto de Jinja2
    # Esta primera funcion me va a ayudar a identificar la sesion de un usuario
    app.jinja_env.globals.update(is_authenticated=helper_auth.authenticated)
    app.jinja_env.globals.update(check_permission=helper_permission.check_permission)
    app.jinja_env.globals.update(check_rol=helper_rol.check_rol)

    # Autenticación
    # app.add_url_rule("/iniciar_sesion", "auth_login", auth.login)
    app.add_url_rule("/cerrar_sesion", "auth_logout", auth.logout)
    app.add_url_rule(
        "/autenticacion", "auth_authenticate", auth.authenticate, methods=["POST"]
    )
    app.add_url_rule(
        "/login/callback", "auth_callback", auth.callback, methods=["GET"]
    )
    app.add_url_rule("/login", "login_google", auth.login)

    # Rutas de Punto de Encuentro
    app.add_url_rule("/puntos", "puntos_index", puntoDeEncuentro.index, methods=["GET", "POST"])
    app.add_url_rule("/puntos/crear_punto", "punto_crear", puntoDeEncuentro.crear_punto, methods=["GET", "POST"])
    app.add_url_rule("/puntos/modificar_punto/<id>", "punto_modificar", puntoDeEncuentro.modificar_punto, methods=["GET", "POST"])
    app.add_url_rule("/puntos/create", "puntos_create", puntoDeEncuentro.create, methods=["GET", "POST"])
    app.add_url_rule("/puntos/update/<id>", "puntos_update", puntoDeEncuentro.update, methods=["PUT", "POST", "GET"])
    app.add_url_rule("/puntos/updateEstado/<id>", "puntos_updateEstado", puntoDeEncuentro.updateEstado, methods=["PUT", "POST", "GET"])
    app.add_url_rule("/puntos/delete/<id>", "puntos_delete", puntoDeEncuentro.delete, methods=["DELETE", "GET", "POST"])

    # Rutas de Usuarios
    app.add_url_rule("/usuarios", "user_index", gestionUsuarios.index, methods=["GET", "POST"])
    app.add_url_rule("/usuarios/create", "user_create", gestionUsuarios.create, methods=["GET" , "POST"])
   # app.add_url_rule("/usuarios/create_google", "user_create_google", gestionUsuarios.create_google, methods=["GET" , "POST"])

    app.add_url_rule("/usuarios/update/<id>", "user_update", gestionUsuarios.update, methods=["PUT", "POST", "GET"])
    app.add_url_rule("/usuarios/updateEstado/<id>", "user_updateEstado", gestionUsuarios.updateEstado, methods=["PUT", "POST", "GET"])
    app.add_url_rule("/usuarios/delete/<id>", "user_delete", gestionUsuarios.delete, methods=["DELETE", "GET", "POST"])
   
    # Ruta de configuracion
    app.add_url_rule("/configuracion","configuracion_index", configuracion.index)
    app.add_url_rule("/configuracion","configuracion_update", configuracion.update, methods=["POST"])
   
    # Rutas de recorrido de evacuacion
    app.add_url_rule("/recorridoEvacuacion", "evacuacion_index", evacuacion.index,  methods=["GET", "POST"])
    app.add_url_rule("/recorridoEvacuacion/create", "evacuacion_create", evacuacion.create, methods=["GET" , "POST"])
    app.add_url_rule("/recorridoEvacuacion/crear", "evacuacion_crear", evacuacion.crear_recorrido, methods=["GET" , "POST"])
    app.add_url_rule("/recorridoEvacuacion/modificar_recorrido/<id>", "recorrido_modificar", evacuacion.modificar_recorrido, methods=["GET", "POST"])
    app.add_url_rule("/recorridoEvacuacion/update/<id>", "evacuacion_update", evacuacion.update, methods=["PUT", "POST", "GET"])
    app.add_url_rule("/recorridoEvacuacion/delete/<id>", "evacuacion_delete", evacuacion.delete, methods=["DELETE", "GET", "POST"])
    app.add_url_rule("/recorridoEvacuacion/<id>", "evacuacion_show", evacuacion.show, methods=["GET"])

    # Rutas de configuracion
    app.add_url_rule("/configuracion", "configuracion_index", configuracion.index)
    app.add_url_rule("/configuracion", "configuracion_update", configuracion.update, methods=["POST"])

    # Rutas de Zonas de Inundacion
    app.add_url_rule("/zonas", "zonas_index", zonas_de_inundacion.index, methods=["GET", "POST"])
    app.add_url_rule("/zonas/crear_zona", "zona_crear", zonas_de_inundacion.crear_zona, methods=["GET", "POST"])
    app.add_url_rule("/zonas/modificar_zona/<id>", "zona_modificar", zonas_de_inundacion.modificar_zona, methods=["GET", "POST"])
    app.add_url_rule("/zonas/create", "zonas_create", zonas_de_inundacion.create, methods=["GET", "POST"])
    app.add_url_rule("/zonas/update/<id>", "zonas_update", zonas_de_inundacion.update, methods=["PUT", "GET", "POST"])
    app.add_url_rule("/zonas/delete/<id>", "zonas_delete", zonas_de_inundacion.delete, methods=["DELETE", "GET", "POST"])
    app.add_url_rule("/zonas/<id>", "zona_show", zonas_de_inundacion.show, methods=["GET"])
    app.add_url_rule("/zonas/import", "zonas_import", zonas_de_inundacion.importing, methods=["GET", "POST"])

    # Denuncias
    app.add_url_rule("/denuncias", "denuncias_index", denuncia.index, methods=["GET", "POST"])
    app.add_url_rule("/denuncias/create", "denuncia_create", denuncia.create, methods=["POST"])
    app.add_url_rule("/denuncias/seguimiento/<id>", "denuncia_seguimiento", denuncia.seguimiento, methods=["GET","POST"])
    app.add_url_rule("/denuncias/mis_denuncias", "mis_denuncias", denuncia.mis_denuncias, methods=["GET"])
    app.add_url_rule("/denuncias/asignar/<id>", "denuncia_asignar_usuario", denuncia.asignar_usuario, methods=["PUT", "POST", "GET"])
    app.add_url_rule("/denuncias/delete/<id>", "denuncia_delete", denuncia.delete, methods=["DELETE", "GET", "POST"])
    app.add_url_rule("/denuncias/<id>", "denuncia_show", denuncia.show, methods=["GET"])

    # Ruta para el Home (usando decorator)
    @app.route("/")
    def home():
        puntos = PuntoDeEncuentro.query.all()
        categorias = Categoria.query.all()
        conf = Configuracion.query.first()
        return render_template("home.html", configuracion=conf, puntos=puntos, categorias=categorias)

    # Rutas de API-REST (usando Blueprints)
    api = Blueprint("api", __name__, url_prefix="/api")
    api.register_blueprint(zonas_api)
    api.register_blueprint(puntos_api)
    api.register_blueprint(evacuacion_api)
    api.register_blueprint(denuncias_api)
    api.register_blueprint(categorias_api)


    app.register_blueprint(api)

    # Handlers
    app.register_error_handler(404, handler.not_found_error)
    app.register_error_handler(401, handler.unauthorized_error)
    app.register_error_handler(403, handler.forbidden_error)
    app.register_error_handler(500, handler.internal_server_error)
    app.register_error_handler(400, handler.bad_request)
    # Implementar lo mismo para el error 500

    # Retornar la instancia de app configurada
    return app

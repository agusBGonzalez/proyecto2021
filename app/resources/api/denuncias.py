from flask import jsonify, Blueprint, abort, request
from app.helpers.validations.json_denuncias import validacion_json_denuncias
from app.models.denuncia import Denuncia
from app.schemas.denuncias import DenunciaSchema
from app.models.configuracion import Configuracion
from app.db import db

denuncias_api = Blueprint("denuncias_api", __name__, url_prefix="/denuncias")


@denuncias_api.get("/")
def get_all():
    conf = Configuracion.query.first()
    page = int(request.args.get("page", 1))
    per_page = int(request.args.get("per_page", conf.cantidad_usuarios))
    denuncias_rows = Denuncia.query.filter(Denuncia.estado != None ).paginate(
        page=page, per_page=per_page
    )

    if denuncias_rows.items:
        denuncias = DenunciaSchema.dump(denuncias_rows, many=True)
        return jsonify(denuncias)
    else:
        abort(404)


@denuncias_api.get("/<id>")
def get_one(id):
    denuncias_rows = Denuncia.query.get(id)

    if denuncias_rows:
        denuncia = DenunciaSchema.dump(denuncias_rows)
        return jsonify(atributos=denuncia)
    else:
        abort(404)

@denuncias_api.get("/not-pages")
def get_all_not_pages():
    denuncias_rows = Denuncia.query.filter(Denuncia.estado == "Resuelta").all()

    if denuncias_rows:
        denuncias = DenunciaSchema.dump(denuncias_rows, many=True, pages=False)
        return jsonify(denuncias)
    else:
        abort(404)

@denuncias_api.post("/")
def create():
    denuncia = request.get_json()
    if validacion_json_denuncias(denuncia):
        new_denuncia = Denuncia(**request.get_json())
        db.session.add(new_denuncia)
        db.session.commit()
        return jsonify( DenunciaSchema.dump(new_denuncia)),201
    else:
        abort(400)

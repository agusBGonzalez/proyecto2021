from flask import jsonify, Blueprint, abort, request
from app.helpers.validations.json_denuncias import validacion_json_denuncias
from app.models.denuncia import Categoria
from app.schemas.categorias import CategoriasSchema
from app.models.configuracion import Configuracion
from app.db import db

categorias_api = Blueprint("categorias_api", __name__, url_prefix="/categorias")


@categorias_api.get("/")
def get_all():
    categorias_rows = Categoria.query.all()

    if categorias_rows:
        categorias =    CategoriasSchema.dump(categorias_rows, many=True, pages=False)
        return jsonify(categorias)
    else:
        abort(404)
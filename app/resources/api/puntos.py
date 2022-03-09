from flask import jsonify, Blueprint, abort, request
from app.models.puntoDeEncuentro import PuntoDeEncuentro
from app.schemas.puntos import PuntoSchema
from app.models.configuracion import Configuracion


puntos_api = Blueprint("puntos_api", __name__, url_prefix="/puntos-encuentro")


@puntos_api.get("/")
def get_all():
    conf = Configuracion.query.first()
    page = int(request.args.get("page", 1))
    per_page = int(request.args.get("per_page", conf.cantidad_zonas))
    puntos_rows = PuntoDeEncuentro.query.filter(PuntoDeEncuentro.estado == 1).paginate(page=page, per_page=per_page)

    if puntos_rows.items:
        puntos = PuntoSchema.dump(puntos_rows, many=True)
        return jsonify(puntos)
    else:
        abort(404)


@puntos_api.get("/not-pages")
def get_all_not_pages():
    puntos_rows = PuntoDeEncuentro.query.filter(PuntoDeEncuentro.estado == 1).all()

    if puntos_rows:
        puntos = PuntoSchema.dump(puntos_rows, many=True, pages=False)
        return jsonify(puntos)
    else:
        abort(404)


@puntos_api.get("/cant-pub")
def get_cant_pub():
    puntos_rows = PuntoDeEncuentro.query.filter(PuntoDeEncuentro.estado == 1).count()

    return jsonify({"cantidad_publicados": puntos_rows})


@puntos_api.get("/cant-despub")
def get_cant_despub():
    puntos_rows = PuntoDeEncuentro.query.filter(PuntoDeEncuentro.estado == 0).count()

    return jsonify({"cantidad_despublicados": puntos_rows})
from re import I
from flask import jsonify, Blueprint, abort, request
from app.models.zonas_de_inundacion import ZonaDeInundacion
from app.schemas.zonas import ZonaSchema
from app.models.configuracion import Configuracion
from app.models.zonas_de_inundacion import CoordenadasZona

zonas_api = Blueprint("zonas_api", __name__, url_prefix="/zonas-inundables")


@zonas_api.get("/")
def get_all():
    conf = Configuracion.query.first()
    page = int(request.args.get("page", 1))
    per_page = int(request.args.get("per_page", conf.cantidad_zonas))
    zonas_rows = ZonaDeInundacion.query.filter(ZonaDeInundacion.estado == 1).paginate(
        page=page, per_page=per_page
    )

    if zonas_rows.items:
        zonas = ZonaSchema.dump(zonas_rows, many=True)
        return jsonify(zonas)
    else:
        abort(404)


@zonas_api.get("/<id>")
def get_one(id):
    zona_row = ZonaDeInundacion.query.get(id)

    if zona_row:
        zona = ZonaSchema.dump(zona_row)
        return jsonify(atributos=zona)
    else:
        abort(404)


@zonas_api.get("/<id>/latlng")
def get_no_latlng(id):
    zona_row = ZonaDeInundacion.query.get(id)

    if zona_row and zona_row.estado:
        zona = ZonaSchema.dump(zona_row, latlng=False)
        return jsonify(atributos=zona)
    else:
        abort(404)


@zonas_api.get("/not-pages")
def get_all_not_pages():
    zonas_rows = ZonaDeInundacion.query.filter(ZonaDeInundacion.estado == 1).all()

    if zonas_rows:
        zonas = ZonaSchema.dump(zonas_rows, many=True, pages=False)
        return jsonify(zonas)
    else:
        abort(404)


@zonas_api.get("/not-pages-latlng")
def get_all_not_latlng():
    zonas_row = ZonaDeInundacion.query.filter(ZonaDeInundacion.estado == 1).all()

    if zonas_row:
        zonas = ZonaSchema.dump(zonas_row, many=True, pages=False, latlng=False)
        return jsonify(zonas)
    else:
        abort(404)


@zonas_api.get("/cant-pub")
def get_cant_pub():
    zonas_rows = ZonaDeInundacion.query.filter(ZonaDeInundacion.estado == 1).count()

    return jsonify({"cantidad_publicados": zonas_rows})


@zonas_api.get("/cant-despub")
def get_cant_despub():
    zonas_rows = ZonaDeInundacion.query.filter(ZonaDeInundacion.estado == 0).count()

    return jsonify({"cantidad_despublicados": zonas_rows})


@zonas_api.get("/max-coords")
def get_max_coords():
    zonas = ZonaDeInundacion.query.all()
    max_coords = 0
    zona_max = ''
    for zona in zonas:
        aux = CoordenadasZona.query.filter(CoordenadasZona.zona_id == zona.id).count()
        if aux > max_coords:
            max_coords = aux
            zona_max = zona

    return jsonify({"zona_info": ZonaSchema.dump(zona_max), "cant_coords": max_coords})


@zonas_api.get("/min-coords")
def get_min_coords():
    zonas = ZonaDeInundacion.query.all()
    min_coords = 9999999
    zona_min = ''
    for zona in zonas:
        aux = CoordenadasZona.query.filter(CoordenadasZona.zona_id == zona.id).count()
        if aux < min_coords:
            min_coords = aux
            zona_min = zona

    return jsonify({"zona_info": ZonaSchema.dump(zona_min), "cant_coords": min_coords})
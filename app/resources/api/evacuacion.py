from flask import jsonify, Blueprint, abort, request
from app.models.evacuacion import Evacuacion
from app.schemas.evacuacion import EvacuacionSchema
from app.models.configuracion import Configuracion
from app.models.evacuacion import CoordenadasEvacuacion


evacuacion_api = Blueprint("evacuacion_api", __name__, url_prefix="/recorrido-evacuacion")


@evacuacion_api.get("/")
def get_all():
    conf = Configuracion.query.first()
    page = int(request.args.get("page", 1))
    per_page = int(request.args.get("per_page", conf.cantidad_recorridos))
    recorridos_rows = Evacuacion.query.paginate(page=page, per_page=per_page)

    if recorridos_rows.items:
        recorridos = EvacuacionSchema.dump(recorridos_rows, many=True)
        return jsonify(recorridos)
    else:
        abort(404)


@evacuacion_api.get("/<id>")
def get_one(id):
    recorridos_rows = Evacuacion.query.get(id)

    if recorridos_rows:
        recorrido = EvacuacionSchema.dump(recorridos_rows)
        return jsonify(atributos=recorrido)
    else:
        abort(404)

# muestra todas las coordenas de la id x despues el estado, id y descripcion
@evacuacion_api.get("/<id>/latlng")
def get_no_latlng(id):
    recorridos_rows = Evacuacion.query.get(id)

    if recorridos_rows and recorridos_rows.estado:
        recorrido = EvacuacionSchema.dump(recorridos_rows, latlng=False)
        return jsonify(atributos=recorrido)
    else:
        abort(404)

#muestra sin paginacion
@evacuacion_api.get("/not-pages")
def get_all_not_pages():
    recorridos_rows = Evacuacion.query.filter(Evacuacion.estado == 1).all()

    if recorridos_rows:
        recorridos = EvacuacionSchema.dump(recorridos_rows, many=True, pages=False)
        return jsonify(recorridos)
    else:
        abort(404)

# muestra todas las coordenas despues el estado, id y descripcion (sin paginacion)
@evacuacion_api.get("/not-pages-latlng")
def get_all_not_latlng():
    recorridos_row = Evacuacion.query.filter(Evacuacion.estado == 1).all()

    if recorridos_row:
        recorridos = EvacuacionSchema.dump(recorridos_row, many=True, pages=False, latlng=False)
        return jsonify(recorridos)
    else:
        abort(404)


@evacuacion_api.get("/cant-pub")
def get_cant_pub():
    recorridos_rows = Evacuacion.query.filter(Evacuacion.estado == 1).count()

    return jsonify({"cantidad_publicados": recorridos_rows})


@evacuacion_api.get("/cant-despub")
def get_cant_despub():
    recorridos_rows = Evacuacion.query.filter(Evacuacion.estado == 0).count()

    return jsonify({"cantidad_despublicados": recorridos_rows})

# devuelve la informacion del recorrido con mayor coordenasdas y cantidad
@evacuacion_api.get("/max-coords")
def get_max_coords():
    recorridos = Evacuacion.query.all()
    max_coords = 0
    recorrido_max = ''
    for recorrido in recorridos:
        aux = CoordenadasEvacuacion.query.filter(CoordenadasEvacuacion.evacuacion_id == recorrido.id).count()
        if aux > max_coords:
            max_coords = aux
            recorrido_max = recorrido

    return jsonify({"recorrido_info": EvacuacionSchema.dump(recorrido_max), "cant_coords": max_coords})

# devuelve la informacion del recorrido con menor coordenasdas y cantidad
@evacuacion_api.get("/min-coords")
def get_min_coords():
    recorridos = Evacuacion.query.all()
    min_coords = 9999999
    recorrido_min = ''
    for recorrido in recorridos:
        aux = CoordenadasEvacuacion.query.filter(CoordenadasEvacuacion.evacuacion_id == recorrido.id).count()
        if aux < min_coords:
            min_coords = aux
            recorrido_min = recorrido

    return jsonify({"recorrido_info": EvacuacionSchema.dump(recorrido_min), "cant_coords": min_coords})
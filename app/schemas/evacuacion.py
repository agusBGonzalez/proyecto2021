class EvacuacionSchema(object):
    @classmethod
    def dump(cls, obj, many=False, pages=True, latlng=True):
        if many:
            if pages:
                return cls._serialize_collection_pages(obj,latlng)
            else:
                return cls._serialize_collection(obj, latlng)
        else:
            return cls._serialize(obj,latlng)

    @classmethod
    def _serialize_collection_pages(cls, pagination, latlng):
        return {
            "recorrido_evacuacion": [cls._serialize(item,latlng) for item in pagination.items],
            "total": pagination.total,
            "pagina": pagination.page,
        }

    @classmethod
    def _serialize_collection(cls, collection, latlng):
        return {
            "recorrido_evacuacion": [cls._serialize(item, latlng) for item in collection]
        }

    @classmethod
    def _serialize(cls, obj, latlng):
        diccionario ={attr.name: getattr(obj, attr.name) for attr in obj.__table__.columns}
        diccionario.update(EvacuacionSchema._serialize_coordenadas(obj.coordenadas, latlng))
        return diccionario

    @classmethod
    def _serialize_coordenadas(cls, collection, latlng):
        return {"coordenadas": [cls._serialize_coordenada(item, latlng) for item in collection]}

    @classmethod
    def _serialize_coordenada(cls, obj, latlng):
        if latlng:
            return {attr.name: getattr(obj, attr.name) for attr in obj.__table__.columns}
        else:
            return [getattr(obj, "lat"), getattr(obj, "long")]
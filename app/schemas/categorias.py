
class CategoriasSchema(object):
    @classmethod
    def dump(cls, obj, many=False, pages=True):
        if many:
            if pages:
                return cls._serialize_collection_pages(obj)
            else:
                return cls._serialize_collection(obj)
        else:
            return cls._serialize(obj)

    @classmethod
    def _serialize_collection_pages(cls, pagination):
        return {
            "categorias": [cls._serialize(item) for item in pagination.items]
        }

    @classmethod
    def _serialize_collection(cls, collection):
        return {
            "categorias": [cls._serialize(item) for item in collection]
        }

    @classmethod
    def _serialize(cls, obj):
        return{attr.name: getattr(obj, attr.name) for attr in obj.__table__.columns}
        

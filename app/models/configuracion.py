from sqlalchemy import Column, Integer, String
from app.db import db


class Configuracion(db.Model):
    __tablename__ = "configuracion"
    id = Column(Integer, primary_key=True)
    cantidad_usuarios = Column(Integer)
    cantidad_puntos = Column(Integer)
    cantidad_zonas = Column(Integer)
    cantidad_recorridos = Column(Integer)
    orden_usuarios = Column(String(20))
    orden_puntos = Column(String(20))
    orden_zonas = Column(String(20))
    orden_recorridos = Column(String(20))
    tema_publico = Column(String(20))
    tema_privado = Column(String(20))

    # updated_at
    # created_at

    def __init__(self, cantidad_usuarios=None, cantidad_puntos=None, cantidad_zonas=None, cantidad_recorridos=None, orden_usuarios=None, orden_puntos=None, orden_zonas=None, orden_recorridos=None, temaPublico=None, temaPrivado=None):
        self.cantidad_usuarios = cantidad_usuarios
        self.cantidad_puntos = cantidad_puntos
        self.cantidad_zonas = cantidad_zonas
        self.cantidad_recorridos = cantidad_recorridos
        self.orden_usuarios = orden_usuarios
        self.orden_puntos = orden_puntos
        self.orden_zonas = orden_zonas
        self.orden_recorridos = orden_recorridos
        self.tema_publico = temaPublico
        self.tema_privado = temaPrivado

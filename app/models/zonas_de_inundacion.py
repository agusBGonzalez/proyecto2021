from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db import db


class ZonaDeInundacion(db.Model):
    __tablename__ = "zonas_de_inundacion"
    id = Column(Integer, primary_key=True)
    codigo = Column(String(150))
    nombre = Column(String(150))
    estado = Column(Boolean)
    color= Column(String(7))
    coordenadas = relationship('CoordenadasZona', backref='zona', lazy=True, cascade="all, delete, delete-orphan")


    def __init__(
        self,
        codigo=None,
        nombre=None,
        estado=None,
        color=None,
    ):
        self.codigo = codigo
        self.nombre = nombre
        self.estado = estado
        self.color = color


class CoordenadasZona(db.Model):
    id = Column(Integer, primary_key=True)
    lat = Column(String(30))
    long = Column(String(30))
    zona_id = Column(Integer, ForeignKey("zonas_de_inundacion.id"), nullable=False)
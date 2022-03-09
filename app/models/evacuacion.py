from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.sql.expression import true
from sqlalchemy.orm import relationship

from app.db import db


class Evacuacion(db.Model):
    __tablename__ = "ruta_de_evacuacion"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), unique=True)
    descripcion = Column(String(350))
    estado = Column(Boolean)
    coordenadas = relationship(
        "CoordenadasEvacuacion",
        backref="evacuacion",
        lazy=True,
        cascade="all, delete, delete-orphan",
    )

    # updated_at
    # created_at

    def __init__(
        self,
        nombre=None,
        descripcion=None,
        estado=None,
    ):
        self.nombre = nombre
        self.descripcion = descripcion
        self.estado = estado


class CoordenadasEvacuacion(db.Model):
    id = Column(Integer, primary_key=True)
    lat = Column(String(30))
    long = Column(String(30))
    evacuacion_id = Column(Integer, ForeignKey("ruta_de_evacuacion.id"), nullable=False)

    # updated_at
    # created_at

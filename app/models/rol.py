from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db import db


rol_tiene_permiso = db.Table(
    "rol_tiene_permiso",
    Column("rol_id", Integer, ForeignKey("roles.id")),
    Column("permiso_id", Integer, ForeignKey("permisos.id")),
)


class Rol(db.Model):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(30), unique=True)
    # updated_at
    # created_at
    permisos = relationship(
        "Permiso",
        secondary=rol_tiene_permiso,
        backref=db.backref("roles", lazy="dynamic"),
        lazy="dynamic",
    )

    def __init__(self, nombre=None):
        self.nombre = nombre
        
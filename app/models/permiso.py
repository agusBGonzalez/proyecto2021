from sqlalchemy import Column, Integer, String
from app.db import db 


class Permiso(db.Model):
    __tablename__ = "permisos"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(30), unique=True)
    # updated_at
    # created_at

    def __init__(self, nombre=None):
        self.nombre = nombre
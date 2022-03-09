from sqlalchemy import Column, Integer, String, Boolean
from app.db import db 


class PuntoDeEncuentro(db.Model):
    __tablename__ = "puntos_de_encuentro"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(150),unique=True)
    direccion = Column(String(150))
    # coordenadas = Column(String(150),unique=True)
    lat = Column(String(30))
    long = Column(String(30))
    estado = Column(Boolean)
    # updated_at
    # created_at
    telefono = Column(String(30))
    email = Column(String(150))

    def __init__(self, nombre=None, direccion=None, long=None, lat=None, estado=None, telefono=None, email=None):
        self.nombre = nombre
        self.direccion = direccion
        self.long = long
        self.lat = lat
        self.estado = estado
        self.telefono = telefono
        self.email = email
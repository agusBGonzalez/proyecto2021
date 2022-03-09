from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Date
from app.db import db 
from datetime import datetime


class Denuncia(db.Model):
    __tablename__ = "denuncias"
    id = Column(Integer, primary_key=True)
    titulo = Column(String(100))
    categoria_id = Column(Integer, ForeignKey("categorias.id"), nullable=False)
    fecha_creacion = Column(String(10))
    fecha_cierre = Column(String(10))
    descripcion = Column(String(250))
    latitud = Column(String(30))
    longitud = Column(String(30))
    estado = Column(String(100))
    apellido_denunciante = Column(String(100))
    nombre_denunciante = Column(String(100))
    telcel_denunciante = Column(String(100))
    email_denunciante = Column(String(100))
    contador = Column(Integer)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    comentario = relationship('ComentariosSeguimiento', backref='denuncia', lazy=True, cascade="all, delete, delete-orphan")
    # updated_at
    # created_at

    def __init__(self, titulo=None, categoria_id=None, fecha_creacion=datetime.today().strftime('%Y-%m-%d'), fecha_cierre=None, descripcion=None, latitud=None, longitud=None, estado="sin confirmar", apellido_denunciante=None, nombre_denunciante=None, telcel_denunciante=None, email_denunciante=None, usuario_id=None):
        self.titulo = titulo
        self.categoria_id = categoria_id
        self.fecha_creacion = fecha_creacion
        self.fecha_cierre = fecha_cierre
        self.descripcion = descripcion
        self.latitud = latitud
        self.longitud = longitud
        self.estado = estado
        self.apellido_denunciante = apellido_denunciante
        self.nombre_denunciante= nombre_denunciante
        self.telcel_denunciante = telcel_denunciante
        self.email_denunciante = email_denunciante
        self.contador = 0
        self.usuario_id = usuario_id

class Categoria(db.Model):
    __tablename__ = "categorias"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    denuncias = relationship('Denuncia', backref='categoria', lazy=True)

class ComentariosSeguimiento(db.Model):
    id = Column(Integer, primary_key=True)
    comentario = Column(String(256))
    denuncia_id = Column(Integer, ForeignKey("denuncias.id"), nullable=False)


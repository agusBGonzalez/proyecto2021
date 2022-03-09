from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db import db


usuario_tiene_rol = db.Table(
    "usuario_tiene_rol",
    Column("usuario_id", Integer, ForeignKey("usuarios.id")),
    Column("rol_id", Integer, ForeignKey("roles.id")),
)

usuario_tiene_denuncia = db.Table(
    "usuario_tiene_denuncia",
    Column("usuario_id", Integer, ForeignKey("usuarios.id")),
    Column("denuncia_id", Integer, ForeignKey("denuncias.id")),
    )

class Usuario(db.Model):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True)
    email = Column(String(30), unique=True)
    username = Column(String(30), unique=True)
    password = Column(String(30))
    activo = Column(Boolean)
    # updated_at
    # created_at
    firstname = Column(String(30))
    lastname = Column(String(30))
    roles = relationship(
        "Rol",
        secondary=usuario_tiene_rol,
        backref=db.backref("usuarios", lazy="dynamic"),
        lazy="dynamic",
    )
    denuncias = relationship(
        "Denuncia",
        secondary=usuario_tiene_denuncia,
        backref=db.backref("denuncias", lazy="dynamic"),
        lazy="dynamic",
    )

    def __init__(
        self,
        id_=None,
        email=None,
        username=None,
        password=None,
        activo=None,
        firstname=None,
        lastname=None,
        profile_pic=None
    ):
        self.id_ = id_
        self.email = email
        self.username = username
        self.password = password
        self.activo = activo
        self.firstname = firstname
        self.lastname = lastname
        self.profile_pic = profile_pic

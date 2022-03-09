from flask import request, session
from app.models.puntoDeEncuentro import PuntoDeEncuentro
from app.models.configuracion import Configuracion
from app.models.usuario import Usuario
from app.models.permiso import Permiso
from app.models.rol import Rol
from app.models.denuncia import Categoria
from app.models.evacuacion import Evacuacion
from app.models.evacuacion import CoordenadasEvacuacion
from app.db import db


# inicializo la base de datos
# creo el primer punto de encuentro
NuevoPDE_1 = PuntoDeEncuentro(
    nombre="Plaza Moreno",
    direccion="13 e/50 y 54",
    # coordenadas="-00000,-000000",
    long="-57.954488",
    lat="-34.921486",
    estado=bool(1),
    telefono="221-123456",
    email="plazaMoreno@gmail.com",
)
db.session.add(NuevoPDE_1)
db.session.commit()

# creo el segundo punto de encuentro
NuevoPDE_2 = PuntoDeEncuentro(
    nombre="Parque Alberti",
    direccion="25 e/37 y 39",
    # coordenadas="-00001,-000001",
    long="-57.980634",
    lat="-34.922274",
    estado=bool(1),
    telefono="221-123456",
    email="parqueAlberti@gmail.com",
)

db.session.add(NuevoPDE_2)
db.session.commit()

# creo el tercer punto de encuentro
NuevoPDE_3 = PuntoDeEncuentro(
    nombre="Plaza Güemes",
    direccion="38 y 19",
    # coordenadas="-00002,-000002",
    long="-57.974438",
    lat="-34.916994",
    estado=bool(1),
    telefono="221-123456",
    email="plazaGüemes@gmail.com",
)

db.session.add(NuevoPDE_3)
db.session.commit()

# creo el cuarto punto de encuentro
NuevoPDE_4 = PuntoDeEncuentro(
    nombre="Plaza Belgrano",
    direccion="13 e/39 y 40",
    # coordenadas="-00003,-000003",
    long="-57.966097",
    lat="-34.912250",
    estado=bool(1),
    telefono="221-123456",
    email="plazaBelgrano@gmail.com",
)

db.session.add(NuevoPDE_4)
db.session.commit()

# creo el tercer punto de encuentro
NuevoPDE_5 = PuntoDeEncuentro(
    nombre="Plaza Olazabal",
    direccion="7 y 38",
    # coordenadas="-00004,-000004",
    long="-57.961791",
    lat="-34.905471",
    estado=bool(1),
    telefono="221-123456",
    email="plazaOlazabal@gmail.com",
)

db.session.add(NuevoPDE_5)
db.session.commit()

# creo el sexto punto de encuentro
NuevoPDE_6 = PuntoDeEncuentro(
    nombre="Plaza Alsina",
    direccion="1 y 38",
    # coordenadas="-00005,-000005",
    long="-57.955813",
    lat="-34.899669",
    estado=bool(1),
    telefono="221-123456",
    email="plazaAlsina@gmail.com",
)

db.session.add(NuevoPDE_6)
db.session.commit()

# creo el septimo punto de encuentro
NuevoPDE_7 = PuntoDeEncuentro(
    nombre="Plaza 19 de Noviembre",
    direccion="25 y 44",
    # coordenadas="-00006,-000006",
    long="-57.973950",
    lat="-34.927718",
    estado=bool(1),
    telefono="221-123456",
    email="plaza19Noviembre@gmail.com",
)

db.session.add(NuevoPDE_7)
db.session.commit()

# creo el octavo punto de encuentro
NuevoPDE_8 = PuntoDeEncuentro(
    nombre="Parque San Martín",
    direccion="25 e/50 y 54",
    # coordenadas="-00007,-000007",
    long="-57.967932",
    lat="-34.933235",
    estado=bool(1),
    telefono="221-123456",
    email="parqueSanMartin@gmail.com",
)

db.session.add(NuevoPDE_8)
db.session.commit()

# creo el noveno punto de encuentro
NuevoPDE_9 = PuntoDeEncuentro(
    nombre="Plaza Juan Domingo Perón",
    direccion="38 y 19",
    # coordenadas="-00008,-000008",
    long="-57.960092",
    lat="-34.937888",
    estado=bool(1),
    telefono="221-123456",
    email="plazaJuanD.Peron@gmail.com",
)

db.session.add(NuevoPDE_9)
db.session.commit()

# creo el decimo punto de encuentro
NuevoPDE_10 = PuntoDeEncuentro(
    nombre="Parque Castelli",
    direccion="25 e/65 y 67",
    # coordenadas="-00009,-000009",
    long="-57.954105",
    lat="-34.942838",
    estado=bool(1),
    telefono="221-123456",
    email="parqueCastelli@gmail.com",
)

db.session.add(NuevoPDE_10)
db.session.commit()

# creo el onceavo punto de encuentro
NuevoPDE_11 = PuntoDeEncuentro(
    nombre="Parque Saavedra",
    direccion="13 e/64 y 68",
    # coordenadas="-00010,-000010",
    long="-57.941782",
    lat="-34.930965",
    estado=bool(1),
    telefono="221-123456",
    email="parqueSaavedra@gmail.com",
)

db.session.add(NuevoPDE_11)
db.session.commit()

# creo el doceavo punto de encuentro
NuevoPDE_12 = PuntoDeEncuentro(
    nombre="Plaza Matheu",
    direccion="1 y 66",
    # coordenadas="-00011,-000011",
    long="-57.929083",
    lat="-34.920395",
    estado=bool(1),
    telefono="221-123456",
    email="plazaMatheu@gmail.com",
)

db.session.add(NuevoPDE_12)
db.session.commit()

# creo el terceavo punto de encuentro
NuevoPDE_13 = PuntoDeEncuentro(
    nombre="Plaza Dardo Rocha",
    direccion="7 y 60",
    # coordenadas="-00012,-000012",
    long="-57.941030",
    lat="-34.920805",
    estado=bool(1),
    telefono="221-123456",
    email="plazaDardoRocha@gmail.com",
)

db.session.add(NuevoPDE_13)
db.session.commit()

# creo el catorceavo punto de encuentro
NuevoPDE_14 = PuntoDeEncuentro(
    nombre="Plaza San Martin",
    direccion="7 e/50 y 54",
    # coordenadas="-00013,-000013",
    long="-57.948579",
    lat="-34.915163",
    estado=bool(1),
    telefono="221-123456",
    email="plazaSanMartin@gmail.com",
)

db.session.add(NuevoPDE_14)
db.session.commit()

# creo el quinceavo punto de encuentro
NuevoPDE_15 = PuntoDeEncuentro(
    nombre="Plaza Italia",
    direccion="7 y 44",
    # coordenadas="-00014,-000014",
    long="-57.955286",
    lat="-34.910679",
    estado=bool(1),
    telefono="221-123456",
    email="plazaItalia@gmail.com",
)

db.session.add(NuevoPDE_15)
db.session.commit()

# creo permisos
# usuario_index: permite a un admin y solo un admin ingresar al index de usuarios y a todas las acciones sobre un usuario.
usuario_index = Permiso(nombre="usuario_index")

# configuracion_index: permite a un admin y solo a un admin ingresar a la seccion de configuracion y atodas las acciones sobre la configuracion del sistema
configuracion_index = Permiso(nombre="configuracion_index")

# punto_encuentro_index: permite acceder al index (listado) del módulo.
punto_encuentro_index = Permiso(nombre="punto_encuentro_index")

# punto_encuentro_new: permite cargar una zona inundable.
punto_encuentro_new = Permiso(nombre="punto_encuentro_new")

# punto_encuentro_destroy: permite borrar una zona inundable.
punto_encuentro_destroy = Permiso(nombre="punto_encuentro_destroy")

# punto_encuentro_update: permite actualizar una zona inundable.
punto_encuentro_update = Permiso(nombre="punto_encuentro_update")

# ruta_evacuacion_index permite acceder al index(listado) del modilo
ruta_evacuacion_index = Permiso(nombre="ruta_evacuacion_index")

# ruta_evacuacion_new permite cargar una ruta de evacuacion
ruta_evacuacion_new = Permiso(nombre="ruta_evacuacion_new")

# ruta_evacuacion_destruy: permite borrar una ruta de evacuacion
ruta_evacuacion_destroy = Permiso(nombre="ruta_evacuacion_destroy")

# ruta_evacuacion_update: permite actualizar una ruta de evacuacion
ruta_evacuacion_update = Permiso(nombre="ruta_evacuacion_update")

# ruta_evacuacion_show: permite ver una ruta de evacuacion en concreto
ruta_evacuacion_show = Permiso(nombre="ruta_evacuacion_show")

# zona_index: permite acceder al index de las zonas de inundacion.
zona_inundacion_index = Permiso(nombre="zona_inundacion_index")

# zona_new: permite crear una zona de inundacion.
zona_inundacion_new = Permiso(nombre="zona_inundacion_new")

# zona_update: permite modificar una zona.
zona_inundacion_update = Permiso(nombre="zona_inundacion_update")

# zona_destroy: permite eliminar una zona.
zona_inundacion_destroy = Permiso(nombre="zona_inundacion_destroy")

# zona_show: permite ver una zona de inundacion.
zona_inundacion_show = Permiso(nombre="zona_inundacion_show")

# agrego los permisos a la base de datos
db.session.add(usuario_index)
db.session.add(configuracion_index)
db.session.add(punto_encuentro_index)
db.session.add(punto_encuentro_new)
db.session.add(punto_encuentro_destroy)
db.session.add(punto_encuentro_update)
db.session.add(ruta_evacuacion_index)
db.session.add(ruta_evacuacion_new)
db.session.add(ruta_evacuacion_destroy)
db.session.add(ruta_evacuacion_update)
db.session.add(ruta_evacuacion_show)
db.session.add(zona_inundacion_index)
db.session.add(zona_inundacion_new)
db.session.add(zona_inundacion_update)
db.session.add(zona_inundacion_destroy)
db.session.add(zona_inundacion_show)
db.session.commit()

# denuncias_index: permite acceder al index (listado) del módulo.
denuncias_index = Permiso(nombre="denuncias_index")

# denuncias_new: permite cargar una zona inundable.
denuncias_new = Permiso(nombre="denuncias_new")

# denuncias_update: permite actualizar una zona inundable.
denuncias_update = Permiso(nombre="denuncias_update")

# denuncias_destroy: permite borrar una zona inundable.
denuncias_destroy = Permiso(nombre="denuncias_destroy")

#agrego los permisos de las denuncias a la base de datos
db.session.add(denuncias_index)
db.session.add(denuncias_new)
db.session.add(denuncias_update)
db.session.add(denuncias_destroy)
db.session.commit()


# creo roles
# rol administrador con sus permisos
rol_administrador = Rol(nombre="administrador")
# esto es la relacion de un rol administrador con sus permisos
#-------------------AG denuncias--------------------
rol_administrador.permisos.append(denuncias_index)
rol_administrador.permisos.append(denuncias_new)
rol_administrador.permisos.append(denuncias_update)
rol_administrador.permisos.append(denuncias_destroy)
#---------------------------------------------------
rol_administrador.permisos.append(usuario_index)
rol_administrador.permisos.append(configuracion_index)
rol_administrador.permisos.append(punto_encuentro_index)
rol_administrador.permisos.append(punto_encuentro_new)
rol_administrador.permisos.append(punto_encuentro_destroy)
rol_administrador.permisos.append(punto_encuentro_update)
rol_administrador.permisos.append(ruta_evacuacion_index)
rol_administrador.permisos.append(ruta_evacuacion_new)
rol_administrador.permisos.append(ruta_evacuacion_destroy)
rol_administrador.permisos.append(ruta_evacuacion_update)
rol_administrador.permisos.append(ruta_evacuacion_show)
rol_administrador.permisos.append(zona_inundacion_index)
rol_administrador.permisos.append(zona_inundacion_new)
rol_administrador.permisos.append(zona_inundacion_update)
rol_administrador.permisos.append(zona_inundacion_destroy)
rol_administrador.permisos.append(zona_inundacion_show)

# rol operador
rol_operador = Rol(nombre="operador")
#-------------------AG denuncias--------------------
rol_operador.permisos.append(denuncias_index)
rol_operador.permisos.append(denuncias_new)
rol_operador.permisos.append(denuncias_update)

#---------------------------------------------------
rol_operador.permisos.append(punto_encuentro_index)
rol_operador.permisos.append(punto_encuentro_new)
rol_operador.permisos.append(punto_encuentro_update)
rol_operador.permisos.append(ruta_evacuacion_index)
rol_operador.permisos.append(ruta_evacuacion_new)
rol_operador.permisos.append(ruta_evacuacion_update)
rol_operador.permisos.append(ruta_evacuacion_show)
rol_operador.permisos.append(zona_inundacion_index)
rol_operador.permisos.append(zona_inundacion_new)
rol_operador.permisos.append(zona_inundacion_update)
rol_operador.permisos.append(zona_inundacion_show)

# agrego los roles a la base de datos
db.session.add(rol_administrador)
db.session.add(rol_operador)
db.session.commit()

# creacion de usuario administrador
administrador = Usuario(
    email="admin@gmail.com",
    username="administrador",
    password="1234",
    activo=bool(1),
    firstname="Marco",
    lastname="Cristofano",
)
# relaciono el usuario admin con el rol administrador
administrador.roles.append(rol_administrador)

db.session.add(administrador)
db.session.commit()

# creacion de usuario operador
operador = Usuario(
    email="operador@gmail.com",
    username="operador",
    password="1234",
    activo=bool(1),
    firstname="operador",
    lastname="operador",
)
# relaciono el usuario operador con el rol operador
operador.roles.append(rol_operador)

db.session.add(operador)
db.session.commit()

# configuracion de la pagina
configuracion = Configuracion(
    cantidad_usuarios=5,
    cantidad_puntos=5,
    cantidad_zonas=5,
    cantidad_recorridos=5,
    orden_usuarios="ascendente",
    orden_puntos="ascendente",
    orden_zonas="ascendente",
    orden_recorridos="ascendente",
    temaPublico="theme3.css",
    temaPrivado="theme3.css",
)
db.session.add(configuracion)
db.session.commit()

# AG creo la categoria 1
categoria1 = Categoria(nombre="alcantarilla tapada")
db.session.add(categoria1)


# AG creo la categoria 2
categoria2 = Categoria(nombre="perdida de agua")
db.session.add(categoria2)

# AG creo la categoria 3
categoria3 = Categoria(nombre="accidente vehicular")
db.session.add(categoria3)


# AG creo la categoria 4
categoria4 = Categoria(nombre="alumbrado roto")
db.session.add(categoria4)

db.session.commit()
# recorridos de evacuacion

recorrido_1 = Evacuacion(
    nombre="la plata centro",
    descripcion="Se empieza en Plaza Mariano Moreno, por avenida 53, se toma la calle 15, luego avenida 51 para tomar calle 16, de ahi directo a diagonal 73, tomamos, luego de llegar a Plaza Azcuenaga, la avenida 44 hasta Plaza 19 de noviembre.",
    estado=bool(1),
)
db.session.add(recorrido_1)
db.session.commit()

coordenada_1 = CoordenadasEvacuacion(
    lat=-34.922686,
    long=-57.954791,
    evacuacion=recorrido_1,
)
coordenada_2 = CoordenadasEvacuacion(
    lat=-34.923698,
    long=-57.955993,
    evacuacion=recorrido_1,
)
coordenada_3 = CoordenadasEvacuacion(
    lat=-34.922836,
    long=-57.957259,
    evacuacion=recorrido_1,
)
coordenada_4 = CoordenadasEvacuacion(
    lat=-34.923812,
    long=-57.958278,
    evacuacion=recorrido_1,
)
coordenada_5 = CoordenadasEvacuacion(
    lat=-34.923293,
    long=-57.958954,
    evacuacion=recorrido_1,
)
coordenada_6 = CoordenadasEvacuacion(
    lat=-34.921683,
    long=-57.961057,
    evacuacion=recorrido_1,
)
coordenada_7 = CoordenadasEvacuacion(
    lat=-34.921912,
    long=-57.966572,
    evacuacion=recorrido_1,
)
coordenada_8 = CoordenadasEvacuacion(
    lat=-34.922501,
    long=-57.966819,
    evacuacion=recorrido_1,
)
coordenada_9 = CoordenadasEvacuacion(
    lat=-34.922695,
    long=-57.967570,
    evacuacion=recorrido_1,
)
coordenada_10 = CoordenadasEvacuacion(
    lat=-34.922572,
    long=-57.968278,
    evacuacion=recorrido_1,
)
coordenada_11 = CoordenadasEvacuacion(
    lat=-34.927046,
    long=-57.973158,
    evacuacion=recorrido_1,
)
db.session.add(coordenada_1)
db.session.add(coordenada_2)
db.session.add(coordenada_3)
db.session.add(coordenada_4)
db.session.add(coordenada_5)
db.session.add(coordenada_6)
db.session.add(coordenada_7)
db.session.add(coordenada_8)
db.session.add(coordenada_9)
db.session.add(coordenada_10)
db.session.add(coordenada_11)

db.session.commit()

recorrido_2 = Evacuacion(
    nombre="la plata centro 2",
    descripcion="Se empieza por Plaza Mariano Moreno, tomando la avenida 13 hasta Plaza Juan Manuel de Rosas, luego se toma la avenida 60 hasta Plaza Hipolito Yrigoyen, por ultimo, nos dirigimos por la diagonal 74 hasta Parque Castelli.",
    estado=bool(1),
)
db.session.add(recorrido_2)
db.session.commit()

coordenada_1 = CoordenadasEvacuacion(
    lat=-34.922344,
    long=-57.953325,
    evacuacion=recorrido_2,
)
coordenada_2 = CoordenadasEvacuacion(
    lat=-34.926047,
    long=-57.948368,
    evacuacion=recorrido_2,
)
coordenada_3 = CoordenadasEvacuacion(
    lat=-34.927041,
    long=-57.948304,
    evacuacion=recorrido_2,
)
coordenada_4 = CoordenadasEvacuacion(
    lat=-34.931527,
    long=-57.953207,
    evacuacion=recorrido_2,
)
coordenada_5 = CoordenadasEvacuacion(
    lat=-34.931967,
    long=-57.952982,
    evacuacion=recorrido_2,
)
coordenada_6 = CoordenadasEvacuacion(
    lat=-34.932679,
    long=-57.953046,
    evacuacion=recorrido_2,
)
coordenada_7 = CoordenadasEvacuacion(
    lat=-34.932978,
    long=-57.953818,
    evacuacion=recorrido_2,
)
coordenada_8 = CoordenadasEvacuacion(
    lat=-34.941017,
    long=-57.953335,
    evacuacion=recorrido_2,
)

db.session.add(coordenada_1)
db.session.add(coordenada_2)
db.session.add(coordenada_3)
db.session.add(coordenada_4)
db.session.add(coordenada_5)
db.session.add(coordenada_6)
db.session.add(coordenada_7)
db.session.add(coordenada_8)

db.session.commit()

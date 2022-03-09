import re
from app.db import db
from app.models.denuncia import Categoria

def validacion_json_denuncias(denuncia):
    if (not "titulo" in denuncia) or (not re.match('^[a-zA-ZÀ-ÿ\s0-9]{4,100}$',denuncia["titulo"])):
        return False
    if (not "descripcion" in denuncia) or (not re.match('.{7,250}',denuncia["descripcion"])):
        return False
    if (not "nombre_denunciante" in denuncia) or (not re.match('^[a-zA-ZÀ-ÿ\s]{4,100}$',denuncia["nombre_denunciante"])):
        return False  
    if (not "apellido_denunciante" in denuncia) or (not re.match('^[a-zA-ZÀ-ÿ\s]{4,100}$',denuncia["apellido_denunciante"])):
        return False
    if (not "email_denunciante" in denuncia) or (not re.match('^([a-zA-Z0-9_.+-]+)@([a-zA-Z0-9-]+)\.([a-z]{2,8})(\.[a-z]{2,8})?$',denuncia["email_denunciante"])):
        return False    
    if (not "telcel_denunciante" in denuncia) or (not re.match('^\d{7,14}',denuncia["telcel_denunciante"])):
        return False
    if (not "latitud" in denuncia) or (not re.match('^[+-]?(([1-8]?[0-9])(\.[0-9]{1,20})?|90(\.0{1,20})?)$',str(denuncia["latitud"]))):
        return False     
    if (not "longitud" in denuncia) or (not re.match('^[+-]?((([1-9]?[0-9]|1[0-7][0-9])(\.[0-9]{1,20})?)|180(\.0{1,20})?)$',str(denuncia["longitud"]))):
        return False
    if (not "categoria_id" in denuncia):
        return False                            
    categoria=Categoria.query.get(denuncia["categoria_id"])
    if not categoria:
        return False
    return True
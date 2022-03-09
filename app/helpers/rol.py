from app.resources.gestionUsuarios import has_rol

def check_rol(user_id, rol):
    return has_rol(user_id, rol)
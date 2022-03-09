from app.resources.gestionUsuarios import has_permission

def check_permission(session, permission):
    return has_permission(session["user"].id, permission)
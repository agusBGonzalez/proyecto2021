from flask import (
    redirect,
    render_template,
    request,
    url_for,
    abort,
    session,
    flash,
    Flask,
    json,
)
from app.models.usuario import Usuario

from app.helpers.validations.autenticacion import FormularioInicioSesion
from app.helpers.auth import create_google, login_google
from os import environ
import requests
from oauthlib.oauth2 import WebApplicationClient

from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
)
import json
import random

# Diego Configuration
GOOGLE_CLIENT_ID = (
    "601314239994-k5rm5bcocthfrpmcr7ti2e0ofqo9qs3k.apps.googleusercontent.com"
)
GOOGLE_CLIENT_SECRET = "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"
GOOGLE_DISCOVERY_URL = "https://accounts.google.com/.well-known/openid-configuration"


def get_google_provider_cfg():
    return requests.get(GOOGLE_DISCOVERY_URL).json()


client = WebApplicationClient(GOOGLE_CLIENT_ID)


def login():
    # Find out what URL to hit for Google login
    google_provider_cfg = get_google_provider_cfg()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]

    # Use library to construct the request for Google login and provide
    # scopes that let you retrieve user's profile from Google
    request_uri = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri="https://admin-grupo8.proyecto2021.linti.unlp.edu.ar/login/callback",
        scope=["openid", "email", "profile"],
    )
    return redirect(request_uri)


# @app.route("/login/callback")
def callback():
    # Get authorization code Google sent back to you
    code = request.args.get("code")

    google_provider_cfg = get_google_provider_cfg()
    token_endpoint = google_provider_cfg["token_endpoint"]
    token_url, headers, body = client.prepare_token_request(
        token_endpoint,
        authorization_response=request.url,
        redirect_url=request.base_url,
        code=code,
    )
    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET),
    )

    # Parse the tokens!
    client.parse_request_body_response(json.dumps(token_response.json()))

    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)
    if userinfo_response.json().get("email_verified"):
        unique_id = userinfo_response.json()["sub"]
        users_email = userinfo_response.json()["email"]
        picture = userinfo_response.json()["picture"]
        users_name = userinfo_response.json()["given_name"]
    else:
        return "User email not available or not verified by Google.", 400

    # Create a user in your db with the information provided
    # by Google
    user = Usuario(
        id_=unique_id, username=users_name, email=users_email, profile_pic=picture
    )

    existe_email = Usuario.query.filter(Usuario.email == user.email).first()

    existe_username = Usuario.query.filter(Usuario.username == user.username).first()
    if not existe_email:
        if existe_username:
            while existe_username.username == user.username:
                numero = random.randint(1, 999999)
                user.username = user.username + str(numero)    
        create_google(user)
        flash("Espere a que le activen la cuenta. Podra acceder a su cuenta con su email y la siguiente contraseña: "+ user.username)
    else:
        login_google(user)
    # Send user back to homepage
    return redirect(url_for("home"))


def authenticate():
    # codigo de wtforms
    form = FormularioInicioSesion()
    if form.validate_on_submit():
        params = request.form
        existeEmail = Usuario.query.filter(Usuario.email == params["email"]).first()

        if not existeEmail:
            flash("El email ingresado no esta registrado en el sistema.")
            return redirect(url_for("home"))

        active = Usuario.query.filter(
            Usuario.email == params["email"], Usuario.activo == "1"
        ).first()

        if not active:
            flash("La cuenta no esta habilitada.")
            return redirect(url_for("home"))

        user = Usuario.query.filter(
            Usuario.email == params["email"], Usuario.password == params["password"]
        ).first()

        if not user:
            flash("La clave es incorrecta.")
            return redirect(url_for("home"))

        session["user"] = user
        flash("La sesión se inicio correctamente.")

    else:
        for x in range(0, len(form.errors)):
            error_msg = "".join(list(form.errors.values())[x]).strip("'[]")
            flash(error_msg, "error")

    return redirect(url_for("home"))


def logout():
    del session["user"]

    session.clear()
    flash("La sesión se cerró correctamente.")

    return redirect(url_for("home"))

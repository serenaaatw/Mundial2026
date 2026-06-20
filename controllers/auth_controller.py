from flask import render_template,request,redirect,url_for,session
from models.cliente import Cliente
from models.administrador import Administrador
from models.db import db
from werkzeug.security import generate_password_hash,check_password_hash
from models.usuario import Usuario

#REGISTRO
# REGISTRO
def register():
    if request.method == "GET":
        return render_template("register.html")

    try:
        nombre = request.form["nombre"]
        email = request.form["email"]
        password = request.form["password"]

        if email == "":
            raise ValueError("El email no puede estar vacío")

        if "@" not in email:
            raise ValueError("El email debe contener @")

        if "." not in email:
            raise ValueError("El email debe contener un dominio válido")

        usuario_existente = Cliente.query.filter_by(
            email=email
        ).first()

        if usuario_existente:
            return "Email ya registrado"

        password_hash = generate_password_hash(password)

        nuevo_cliente = Cliente(
            nombre=nombre,
            email=email,
            password=password_hash,
            rol="CLIENTE"
        )

        db.session.add(nuevo_cliente)
        db.session.commit()

        return redirect(
            url_for("auth.login_route")
        )

    except ValueError as error:
        return f"Error: {error}"

#Login
def login(): 
    if request.method=="GET": 
        return render_template("login.html") 
    email=request.form["email"] 
    password=request.form["password"]

    usuario=Cliente.query.filter_by(email=email).first()
    if not usuario: 
        usuario=Administrador.query.filter_by(email=email).first()
        if not usuario: 
            return "usuario no existente"
    if not check_password_hash(usuario.password,password): 
        return "Contraseña incorrecta" 
    session["usuario_id"]=usuario.id 
    session["rol"]=usuario.rol 
    return redirect(url_for("partido.partidoproximos"))
def logout():
    session.clear()

    return redirect(
        url_for("auth.login_route")
    )
from flask import render_template,request,redirect,url_for,session
from models.cliente import Cliente
from models.db import db
from werkzeug.security import generate_password_hash,check_password_hash
from models.usuario import Usuario

#REGISTRO
def register():
    if request.method=="GET":
        return render_template("register.html")
    nombre=request.form["nombre"]
    email=request.form["email"]
    password=request.form["password"]
#validar email - ver perfil (tomy) para que no pongan cualquier cosa
#y validar cantidad de caracteres en la contraseña.
#importar re
#importar 
    usuario_existente=Cliente.query.filter_by(email=email).first()
    if usuario_existente:
        return "Email ya registrado"
    password_hash=generate_password_hash(password)

    nuevo_cliente=Cliente(
        nombre=nombre,
        email=email,
        password=password_hash,
        rol="CLIENTE"
    )
    db.session.add(nuevo_cliente)
    db.session.commit()
    return redirect(url_for("auth.login"))


#Login
def login():
    if request.method=="GET":
        return render_template("login.html")
    email=request.form["email"]
    password=request.form["password"]

    usuario=Usuario.query.filter_by(email=email).first()
    if not usuario:
        return "Usuario no encontrado"
    if not check_password_hash(usuario.password,password):
        return "Contraseña incorrecta"
    
    session["usuario_id"]=usuario.id 
    session["rol"]=usuario.rol
    
    
    #if usuario.rol=="ADMIN":
     #   return redirect(url_for("auth.admin_dashboard"))
    return redirect(url_for("partido.partidoproximos"))

def logout():
    session.clear()
    return redirect(url_for("auth.login"))
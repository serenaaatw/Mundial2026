from models.db import db
from models.usuario import Usuario
from flask import jsonify 
import re
import os
from werkzeug.utils import secure_filename
def ver_usuario(id):
    usuario = Usuario.query.get(id)
    if usuario:
        return usuario
    return {"ERROR": "El usuario no existe"}

def actualizar_perfil(id, data, foto = None):
    user = Usuario.query.get(id)
    tipos = {
        "nombre_usuario":str ,
        "mail_usuario":str ,
        "foto_perfil":str
    }
    if user:

        if foto and foto.filename != "":

            carpeta = "static/uploads"

            if not os.path.exists(carpeta):
                os.makedirs(carpeta)
            nombre_imagen = secure_filename(foto.filename)
            ruta = os.path.join(carpeta,nombre_imagen)
            foto.save(ruta)
            user.foto_perfil = ("uploads/" + nombre_imagen)
        for key, value in data.items():
            if key in tipos:
                value = tipos[key](value)
            if key == "mail_usuario":
                patron = r"^[\w\.-]+@[\w\.-]+\.\w+$"
                if not re.match(patron, value):
                    raise ValueError(
                        "El correo ingresado no es válido"
                    )
            setattr(user, key, value)
        db.session.commit()
        return user.serialize()
    return {"ERROR": "Usuario no encontrado"}






    
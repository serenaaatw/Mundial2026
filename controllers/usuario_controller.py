from models.db import db
from models.usuario import Usuario
import re
import os
from werkzeug.utils import secure_filename
from flask import session
from uuid import uuid4

def ver_usuario():
    id_usuario = session.get("usuario_id")

    if id_usuario:
        usuario = Usuario.query.get(id_usuario)
        if usuario:
            return usuario

    return {"ERROR": "El usuario no existe"}

def actualizar_perfil(data, foto=None):
    id_usuario = session.get("usuario_id")
    user = Usuario.query.get(id_usuario)
    tipos = {
        "nombre": str,
        "email": str,
        "foto_perfil": str
    }
    if user:
        if foto and foto.filename != "":
            carpeta = "static/uploads"
            if not os.path.exists(carpeta):
                os.makedirs(carpeta)
            nombre_imagen = str(uuid4()) + "_" + secure_filename(foto.filename)

            ruta = os.path.join(carpeta, nombre_imagen)
            if os.path.exists(ruta):
                raise ValueError(
                    "Ya existe una imagen con ese nombre, elegí otra"
                )
            foto.save(ruta)
            user.foto_perfil = "uploads/" + nombre_imagen
        for key, value in data.items():
            if key in tipos:
                value = tipos[key](value)
            if key == "email":

                patron = r"^[\w\.-]+@[\w\.-]+\.\w+$"

                if not re.match(patron, value):
                    raise ValueError(
                        "El correo ingresado no es válido"
                    )
            setattr(user, key, value)
        db.session.commit()
        return user.serialize()
    return {"ERROR": "Usuario no encontrado"}






    
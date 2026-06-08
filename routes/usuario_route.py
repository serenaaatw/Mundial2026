from controllers.usuario_controller import *
from flask import Blueprint, render_template, redirect, request, url_for

Usuario_bp = Blueprint("Usuario", __name__)

@Usuario_bp.route("/ver_usuario/<int:id>")
def verusuario(id):
    user = ver_usuario(id)
    return render_template("ver_perfil.html",  user = user)

@Usuario_bp.route("/ver_usuario/<int:id>/editar")
def editarformulario(id):
    user = ver_usuario(id)
    return render_template("editar_perfil.html", user = user)

@Usuario_bp.route("/ver_usuario/<int:id>", methods = ["POST"])
def actualizarperfil(id):
    data = request.form.to_dict()
    foto = request.files.get("foto_perfil")
    try:
        actualizar_perfil(id, data, foto)
        return redirect(url_for("Usuario.verusuario",id=id))
    except ValueError as e:
        user = ver_usuario(id)
        return render_template("editar_perfil.html", user = user, error = str(e))


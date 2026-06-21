from controllers.usuario_controller import *
from flask import Blueprint, render_template, redirect, request, url_for
from utils.auth import login_required

Usuario_bp = Blueprint("Usuario", __name__)

@Usuario_bp.route("/ver_usuario")
@login_required
def verusuario():
    user = ver_usuario()
    return render_template("ver_perfil.html",  user = user)

@Usuario_bp.route("/ver_usuario/editar")
@login_required
def editarformulario():
    user = ver_usuario()
    return render_template("editar_perfil.html", user = user)

@Usuario_bp.route("/ver_usuario", methods = ["POST"])
@login_required
def actualizarperfil():
    data = request.form.to_dict()
    foto = request.files.get("foto_perfil")
    try:
        actualizar_perfil(data, foto)
        return redirect(url_for("Usuario.verusuario"))
    except ValueError as e:
        user = ver_usuario()
        return render_template("editar_perfil.html", user = user, error = str(e))


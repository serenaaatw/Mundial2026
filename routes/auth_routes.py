from flask import Blueprint
from controllers.auth_controller import register,login,logout
from utils.auth import login_required

auth_bp=Blueprint("auth",__name__)
#ruta registro
@auth_bp.route("/register", methods=["GET","POST"])
def register_route():
    return register()

#ruta login
@auth_bp.route("/login",methods=["GET","POST"])
def login_route():
    return login()

#ruta cerrar sesion
@auth_bp.route("/logout")
@login_required
def logout_route():
    return logout()


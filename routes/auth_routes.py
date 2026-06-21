from flask import Blueprint
from controllers.auth_controller import register,login,logout

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
def logout_route():
    return logout()


from flask import Blueprint,redirect, session, render_template,url_for
from controllers.auth_controller import register,login,logout
auth_bp=Blueprint("auth",__name__)
#ruta registro
auth_bp.route("/register", methods=["GET","POST"])(register)

#ruta login
auth_bp.route("/login",methods=["GET","POST"])(login)

#ruta cerrar sesion
auth_bp.route("/logout")(logout)


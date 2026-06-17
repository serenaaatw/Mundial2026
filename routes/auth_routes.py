from flask import Blueprint,redirect, session, render_template,url_for
from controllers.auth_controller import register,login,logout
auth_bp=Blueprint("auth",__name__)
#ruta registro
auth_bp.route("/register", methods=["GET","POST"])(register)

#ruta login
auth_bp.route("/login",methods=["GET","POST"])(login)

#ruta cerrar sesion
auth_bp.route("/logout")(logout)

#dasboard administrador
@auth_bp.route("/admin")
def admin_dasboard():
    if session.get("rol")!="ADMIN":
        return redirect(url_for("auth.login"))
    return render_template("admin_dashboard.html")

#dashboar cliente
@auth_bp.route("/cliente")
def cliente_dashboard():
    if session.get("rol")!="CLIENTE":
        return redirect(url_for("auth.login"))
    return render_template("cliente_dasboard.html")
from functools import wraps
from flask import session, render_template
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "usuario_id" not in session:
            return render_template("error.html", mensaje="Debes iniciar sesión para acceder a esta página."), 401
        return f(*args, **kwargs)
    return decorated_function
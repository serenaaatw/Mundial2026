from flask import Flask
from models.db import db
from config.config import DATABASE_CONNECTION_URI
from routes.partido_route import partido_bp
<<<<<<< HEAD
from routes.auth_routes import auth_bp
from routes.usuario_route import Usuario_bp
=======
from routes.resultado_route import resultado_bp
from routes.auth_routes import auth_bp
from routes.usuario_route import Usuario_bp
import os
>>>>>>> 131c0ae2f7893a8052c42a82c09a6e6f8558420d

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


app.register_blueprint(partido_bp)
<<<<<<< HEAD
=======
app.register_blueprint(resultado_bp)
>>>>>>> 131c0ae2f7893a8052c42a82c09a6e6f8558420d
app.register_blueprint(auth_bp)
app.register_blueprint(Usuario_bp)

db.init_app(app)

with app.app_context():
    from models.equipo import Equipo
    from models.estadio import Estadio
    from models.partido import Partido
    from models.resultado import Resultado
    from models.usuario import Usuario
    from models.cliente import Cliente 
    from models.administrador import Administrador
    #db.drop_all()
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
    

from flask import Flask
from models.db import db
from config.config import DATABASE_CONNECTION_URI
from routes.equipo_route import equipo_bp
from routes.estadio_route import estadio_bp
from routes.partido_route import partido_bp

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.register_blueprint(equipo_bp)
app.register_blueprint(estadio_bp)
app.register_blueprint(partido_bp)

db.init_app(app)

with app.app_context():
    from models.equipo import Equipo
    from models.estadio import Estadio
    from models.partido import Partido
    #db.drop_all()
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
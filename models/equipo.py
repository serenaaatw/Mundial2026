from models.db import db

class Equipo(db.Model):
    __tablename__ = 'equipos'

    id = db.Column(db.Integer, primary_key=True)
    pais = db.Column(db.String(100), nullable=False)
    grupo = db.Column(db.String(1), nullable=False)
    bandera = db.Column(db.String(200), nullable=True)
    puntos= db.Column(db.Integer, nullable=False, default=0)

    def __init__(self, pais, bandera, grupo, puntos):
        self.pais = pais
        self.bandera = bandera
        self.grupo = grupo
        self.puntos = puntos

    def serialize(self):
        return {
            'id': self.id,
            'pais': self.pais,
            'grupo': self.grupo,
            'bandera': self.bandera,
            'puntos': self.puntos
        }
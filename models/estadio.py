from models.db import db

class Estadio(db.Model):
    __tablename__ = 'estadios'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    ciudad = db.Column(db.String(100), nullable=False)
    capacidad = db.Column(db.Integer, nullable=False)
    pais= db.Column(db.String(100), nullable=False)
    latitud = db.Column(db.Float, nullable=False)
    longitud = db.Column(db.Float, nullable=False)

    def __init__(self, nombre, ciudad, capacidad, pais, latitud, longitud):
        self.nombre = nombre
        self.ciudad = ciudad
        self.capacidad = capacidad
        self.pais = pais
        self.latitud = latitud
        self.longitud = longitud

    def serialize(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'ciudad': self.ciudad,
            'capacidad': self.capacidad,
            'pais': self.pais,
            'latitud': self.latitud,
            'longitud': self.longitud
        }
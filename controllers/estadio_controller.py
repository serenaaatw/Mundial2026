from models.db import db
from models.estadio import Estadio

def obtener_estadio(id_estadio):
    estadio = Estadio.query.get(id_estadio)
    if estadio:
        return estadio.serialize()
    return {"error": "Estadio no encontrado"}
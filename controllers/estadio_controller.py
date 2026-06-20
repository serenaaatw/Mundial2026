from models.estadio import Estadio

def ver_estadios():
    estadios= Estadio.query.all()
    return [estadio.serialize() for estadio in estadios]
from models.db import db
from models.partido import Partido
from models.equipo import Equipo
from models.estadio import Estadio

def crear_partido(data):
    nuevo_partido = Partido(**data)
    if nuevo_partido:
        db.session.add(nuevo_partido)
        db.session.commit()
        return nuevo_partido.serialize()
    return {"error": "No se pudo crear el partido"}

def obtener_partidos():
    partidos = Partido.query.all()
    for partido in partidos:
        partido.nombre_equipo1 = Equipo.query.get(partido.id_equipo1).pais
        partido.nombre_equipo2 = Equipo.query.get(partido.id_equipo2).pais
        partido.nombre_estadio = Estadio.query.get(partido.id_estadio).nombre
        partido.bandera_equipo1 = Equipo.query.get(partido.id_equipo1).bandera
        partido.bandera_equipo2 = Equipo.query.get(partido.id_equipo2).bandera
    return partidos

def obtener_partido(partido_id):
    partido = Partido.query.get(partido_id)
    if partido:
        return partido
    return {"error": "Partido no encontrado"}

def actualizar_partido(partido_id, data):
    partido = Partido.query.get(partido_id)
    TIPOS = {
        "id_equipo1": int,
        "id_equipo2": int,
        "id_estadio": int,
        "fecha": str,
        "hora": str,
        "estado": str,
        "etapa": str
    }
    
    if partido:
        if int(data["id_equipo1"]) == int(data["id_equipo2"]):
            raise ValueError("Un equipo no puede jugar contra sí mismo")
        for key, value in data.items():
            if key in TIPOS:
                value = TIPOS[key](value)
            setattr(partido, key, value)
        db.session.commit()
        return partido.serialize()
    return {"error": "Partido no encontrado"}

def eliminar_partido(partido_id):
    partido = Partido.query.get(partido_id)
    if partido:
        db.session.delete(partido)
        db.session.commit()
        return True
    return False
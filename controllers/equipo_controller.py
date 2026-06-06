from models.equipo import Equipo
from models.db import db

def crear_equipo(data):
    nuevo_equipo = Equipo(**data)
    if nuevo_equipo:
        db.session.add(nuevo_equipo)
        db.session.commit()
        return nuevo_equipo.serialize()
    return {"error": "No se pudo crear el equipo"}
    
def obtener_equipos():
    equipos = Equipo.query.all()
    return [equipo.serialize() for equipo in equipos]

def obtener_equipo(equipo_id):
    equipo = Equipo.query.get(equipo_id)
    if equipo:
        return equipo.serialize()
    return {"error": "Equipo no encontrado"}

def actualizar_equipo(equipo_id, data):
    equipo = Equipo.query.get(equipo_id)
    tipos= {
        "pais": str,
        "grupo": str,
        "bandera": str,
        "puntos": int
    }
    if equipo:
        for key, value in data.items():
            if key in tipos and isinstance(value, tipos[key]):
                setattr(equipo, key, value)
        db.session.commit()
        return equipo.serialize()
    return {"error": "Equipo no encontrado"}

def eliminar_equipo(equipo_id):
    equipo = Equipo.query.get(equipo_id)
    if equipo:
        db.session.delete(equipo)
        db.session.commit()
        return {"message": "Equipo eliminado"}
    return {"error": "Equipo no encontrado"}
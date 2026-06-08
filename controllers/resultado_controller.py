from models.db import db
from models.resultado import Resultado
from models.partido import Partido

def crear_resultado(partido_id, goles_equipo1, goles_equipo2):
    partido = Partido.query.get(partido_id)
    if not partido:
        return {"error": "Partido no encontrado"}, 404
    if goles_equipo1 < 0 or goles_equipo2 < 0:
        return {"error": "Los goles no pueden ser negativos"}, 400
    if Resultado.query.filter_by(partido_id=partido_id).first():
        return {"error": "Ya existe un resultado para este partido"}, 400
    resultado = Resultado(
        partido_id=partido_id,
        goles_equipo1=goles_equipo1,
        goles_equipo2=goles_equipo2
    )
    db.session.add(resultado)
    db.session.commit()
    return resultado.serialize(), 201
def obtener_Resultados():
    resultados = Resultado.query.all()
    return [resultado.serialize() for resultado in resultados], 200

def obtener_resultado(id_res):
    resultado = Resultado.query.get(id_res)
    if not resultado:
        return {"error": "Resultado no encontrado"}, 404
    return resultado.serialize(), 200
def actualizar_resultado(id_res, goles_equipo1, goles_equipo2):
    resultado = Resultado.query.get(id_res)
    if not resultado:
        return {"error": "Resultado no encontrado"}, 404
    if goles_equipo1 < 0 or goles_equipo2 < 0:
        return {"error": "Los goles no pueden ser negativos"}, 400
    resultado.goles_equipo1 = goles_equipo1
    resultado.goles_equipo2 = goles_equipo2
    db.session.commit()
    return resultado.serialize(), 200

def eliminar_resultado(id_res):
    resultado = Resultado.query.get(id_res)
    if not resultado:
        return {"error": "Resultado no encontrado"}, 404
    db.session.delete(resultado)
    db.session.commit()
    return {"mensaje": "Resultado eliminado correctamente"}, 200
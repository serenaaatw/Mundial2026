from models.db import db
from models.partido import Partido
from models.equipo import Equipo
from models.estadio import Estadio

def crear_partido(data):
    ESTADOS= ["programado", "suspendido", "finalizado"]
    ETAPAS= ["fase de grupos", "dieciseisavos de final", "cuartos de final", "octavos de final", 
             "semifinales", "final", "tercer y cuarto puesto"]
    
    from datetime import datetime
        
    try:
        fecha_hora = datetime.strptime(f"{data['fecha']} {data['hora']}", "%Y-%m-%d %H:%M:%S")
    except ValueError:
        raise ValueError("Fecha u hora inválida. Use YYYY-MM-DD y HH:MM:SS")

    if fecha_hora < datetime.now():
       raise ValueError("La fecha y hora no pueden ser anteriores al momento actual")
    if data["estado"].lower() not in ESTADOS:
        raise ValueError("Estados posibles: Programado, Suspendido, Finalizado")
        
    if data["etapa"].lower() not in ETAPAS:
      raise ValueError("Etapas posibles: Fase de Grupos, Dieciseisavos de final, Octavos de Final, Cuartos de Final, Semifinales, Final, Tercer y Cuarto puesto")
        
    if int(data["id_equipo1"])<1 or int(data["id_equipo2"]) <1:
        raise ValueError("Ingrese números positivos")
        
    if not Equipo.query.get(int(data["id_equipo1"])) or not Equipo.query.get(int(data["id_equipo2"])):
        raise ValueError("Ingrese equipos existentes")
        
    if not Estadio.query.get(int(data["id_estadio"])):
        raise ValueError("Ingrese un estadio existente")
        
    if int(data["id_equipo1"]) == int(data["id_equipo2"]):
        raise ValueError("Un equipo no puede jugar contra sí mismo")
    
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
    ESTADOS= ["programado", "suspendido", "finalizado"]
    ETAPAS= ["fase de grupos", "dieciseisavos de final", "cuartos de final", "octavos de final", 
             "semifinales", "final", "tercer y cuarto puesto"]
    
    if partido:
        from datetime import datetime
        
        try:
            fecha_hora = datetime.strptime(f"{data['fecha']} {data['hora']}", "%Y-%m-%d %H:%M:%S")

        except ValueError:
            raise ValueError("Fecha u hora inválida. Use YYYY-MM-DD y HH:MM:SS")

        if fecha_hora < datetime.now():
             raise ValueError("La fecha y hora no pueden ser anteriores al momento actual")
        if data["estado"].lower() not in ESTADOS:
            raise ValueError("Estados posibles: Programado, Suspendido, Finalizado")
        
        if data["etapa"].lower() not in ETAPAS:
            raise ValueError("Etapas posibles: Fase de Grupos, Dieciseisavos de final, Octavos de Final, Cuartos de Final, Semifinales, Final, Tercer y Cuarto puesto")
        
        if int(data["id_equipo1"])<1 or int(data["id_equipo2"]) <1:
            raise ValueError("Ingrese números positivos")
        
        if not Equipo.query.get(int(data["id_equipo1"])) or not Equipo.query.get(int(data["id_equipo2"])):
            raise ValueError("Ingrese equipos existentes")
        
        if not Estadio.query.get(int(data["id_estadio"])):
            raise ValueError("Ingrese un estadio existente")
        
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

def obtener_suspendidos():
    partidos_suspendidos = Partido.query.filter_by(estado='Suspendido').all()
    for partido in partidos_suspendidos:
        partido.nombre_equipo1 = Equipo.query.get(partido.id_equipo1).pais
        partido.nombre_equipo2 = Equipo.query.get(partido.id_equipo2).pais
        partido.nombre_estadio = Estadio.query.get(partido.id_estadio).nombre
        partido.bandera_equipo1 = Equipo.query.get(partido.id_equipo1).bandera
        partido.bandera_equipo2 = Equipo.query.get(partido.id_equipo2).bandera
    return partidos_suspendidos

def reprogramar_partido(partido_id, fecha, hora, estadio_id):
    partido = Partido.query.get(partido_id)

    if not partido:
        raise ValueError("Partido no encontrado")

    from datetime import datetime
    try:
        fecha_hora = datetime.strptime(
            f"{fecha} {hora}",
            "%Y-%m-%d %H:%M:%S")
        fecha_nueva = datetime.strptime(fecha,"%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Fecha u hora inválida")

    if fecha_hora < datetime.now():
        raise ValueError("La fecha y hora no pueden ser anteriores al momento actual")

    if fecha_nueva < partido.fecha:
        raise ValueError("La nueva fecha no puede ser anterior a la fecha original del partido")
    
    if not Estadio.query.get(estadio_id):
        raise ValueError("Ingrese un estadio existente")
    
    nuevo_partido = Partido(
        id_equipo1=partido.id_equipo1,
        id_equipo2=partido.id_equipo2,
        id_estadio=estadio_id,
        etapa=partido.etapa,
        fecha=fecha,
        hora=hora,
        estado="Reprogramado"
    )

    db.session.add(nuevo_partido)
    db.session.commit()

    return nuevo_partido.serialize()
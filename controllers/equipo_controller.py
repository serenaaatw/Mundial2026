from models.equipo import Equipo
 
def ver_equipos():
    equipos= Equipo.query.order_by(Equipo.grupo, Equipo.pais).all()
    return [equipo.serialize() for equipo in equipos]
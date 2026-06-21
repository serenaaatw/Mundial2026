from models.db import db
class Resultado(db.Model):
    __tablename__ = 'resultados'
    id_res= db.Column(db.Integer, primary_key=True)
    partido_id = db.Column(db.Integer, db.ForeignKey('partidos.id'), nullable=False)
    goles_equipo1 = db.Column(db.Integer, nullable=False)
    goles_equipo2 = db.Column(db.Integer, nullable=False)

    def __init__(self, partido_id, goles_equipo1, goles_equipo2):
        self.partido_id = partido_id
        self.goles_equipo1 = goles_equipo1
        self.goles_equipo2 = goles_equipo2
    def serialize(self):
        return {
            'id_res': self.id_res,
            'partido_id': self.partido_id,
            'goles_equipo1': self.goles_equipo1,
            'goles_equipo2': self.goles_equipo2
        }
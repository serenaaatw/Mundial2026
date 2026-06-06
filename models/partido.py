from models.db  import db

class Partido(db.Model):
    __tablename__ = 'partidos'

    id = db.Column(db.Integer, primary_key=True)
    id_equipo1= db.Column(db.Integer, db.ForeignKey('equipos.id'), nullable=False)
    id_equipo2= db.Column(db.Integer, db.ForeignKey('equipos.id'), nullable=False)
    id_estadio= db.Column(db.Integer, db.ForeignKey('estadios.id'), nullable=False)
    fecha = db.Column(db.Date, nullable=False)
    hora = db.Column(db.Time, nullable=False)
    estado = db.Column(db.Enum('Programado', 'Suspendido', 'Finalizado'), nullable=False, default='Programado')
    etapa= db.Column(db.Enum('Fase de Grupos', 'Octavos de Final', 'Cuartos de Final', 'Semifinales', 'Final'), nullable=False)

    def __init__(self, id_equipo1, id_equipo2, id_estadio, fecha, hora, estado, etapa):
        if id_equipo1 == id_equipo2:
            raise ValueError("Un equipo no puede jugar contra sí mismo")
        self.id_equipo1 = id_equipo1
        self.id_equipo2 = id_equipo2
        self.id_estadio = id_estadio
        self.fecha = fecha
        self.hora = hora
        self.estado = estado
        self.etapa = etapa

    def serialize(self):
        return {
            'id': self.id,
            'id_equipo1': self.id_equipo1,
            'id_equipo2': self.id_equipo2,
            'id_estadio': self.id_estadio,
            'fecha': self.fecha.isoformat(),
            'hora': self.hora.isoformat(),
            'estado': self.estado,
            'etapa': self.etapa
        }
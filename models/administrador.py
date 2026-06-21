from models.usuario import Usuario
from models.db import db
from datetime import date

class Administrador(Usuario):
    #agregar atributo de fecha de alta del administrador
    fecha_alta = db.Column(db.Date, default=date.today)
    #polomorfismo de herencia para identificar en el programa que objeto crear teniendo en cienta el atributo rol
    __mapper_args__ = {
        "polymorphic_identity": "ADMIN"
    }
    def serialize(self):
        data=super().serialize()
        data["fecha_alta"]=self.fecha_alta
        return data
#polimorfismo de herencia que muestra un atributo especifco del administrador más los de usuario

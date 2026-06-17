from models.usuario import Usuario
class Administrador(Usuario):
    #polomorfismo de herencia para identificar en el programa que objeto crear teniendo en cienta el atributo rol
    __mapper_args__ = {
        "polymorphic_identity": "ADMIN"
    }

    def crear_partido(self):
        return"Partido creado"

    def eliminar_usuario(self):
        return"Usuario eliminado"

    def ver_reportes(self):
        return"Mostrando reportes"
    
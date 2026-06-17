from models.db import db
class Usuario(db.Model):
    __tablename__="usuarios"
    id=db.Column(db.Integer,primary_key=True)
    nombre=db.Column(db.String(100),nullable=False)
    email=db.Column(db.String(200),unique=True, nullable=False)
    password=db.Column(db.String(20), nullable=False)
    rol=db.Column(db.String(20))
    #polomorfismo de herencia para identificar en el programa que objeto crear teniendo en cienta el atributo rol
    __mapper_args__={"polymorphic_on":rol,
                     "polymorphic_identity":"usuario"}
    def __init__(self,nombre,email,password,rol):
        self.nombre=nombre
        self.email=email
        self.password=password
        self.rol=rol
    def serialize(self):
        return {
            "id":self.id,
            "nombre":self.nombre,
            "email":self.email,
            "password":self.password,
            "rol":self.rol
        }
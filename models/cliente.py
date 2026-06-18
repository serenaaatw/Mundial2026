from models.usuario import Usuario
class Cliente(Usuario):
  #polomorfismo de herencia para identificar en el programa que objeto crear teniendo en cienta el atributo rol
   
   __mapper_args__={
      "polymorphic_identity":"CLIENTE"
   }
   def serialize(self):
      data=super().serialize()
      return data
   
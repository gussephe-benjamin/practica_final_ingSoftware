from Clases import Contacto
class Usuario:
    
    def __init__(self, alias, nombre):
        self.alias = alias
        self.nombre = nombre
        self.listaContactos = []
        self.mensajesEnviados = []
        self.mensajesRecibidos = []
        
    def agregarContacto (self, alias: str, nombre: str):
        pass
    def enviarMensaje (self, destinatario : Contacto, contenido: str):
        pass
    def verHistorialMensajes():
        pass
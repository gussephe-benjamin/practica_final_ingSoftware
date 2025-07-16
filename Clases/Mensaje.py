from Clases import Usuario
from datetime import datetime

class Mensaje:
    def __init__(self, remitente: Usuario, destinatario : Usuario, contenido : str):
        self.remitente = remitente
        self.destinatario = destinatario
        self.contenido = contenido
        self.fechaEnvio = datetime()
        
    def enviarMensaje(self):
        self.fechaEnvio = datetime.now()
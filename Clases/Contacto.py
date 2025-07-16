
from datetime import datetime

class Contacto:
    def __init__(self, alias: str):
        self.alias = alias
        self.fechaRegistro = datetime.now()
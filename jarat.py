from abc import ABC
from datetime import datetime

class Jarat(ABC):
    def __init__(self, jaratszam: str, celallomas: str, jegyar: int, indulasido:datetime):
        self.jaratszam = jaratszam
        self.celallomas = celallomas
        self.jegyar = jegyar
        self.indulasido = indulasido
        
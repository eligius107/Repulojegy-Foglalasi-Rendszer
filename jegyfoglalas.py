from jarat import Jarat

class JegyFoglalas:
    def __init__(self, nev:str, utazas: Jarat, idopont):
        self.utazas = utazas
        self.nev = nev
        if utazas.indulasido < idopont:
            raise Exception("A jegy nem foglalható, mivel a gép már elindult.")


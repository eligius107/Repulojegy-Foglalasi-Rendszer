from jegyfoglalas import JegyFoglalas
from jarat import Jarat
from belfoldijarat import BelfoldiJarat
from nemzetkozijarat import NemzetkoziJarat
from legitarsasag import LegiTarsasag
from datetime import datetime

foglalasok = []

def main():

    jarat1 = NemzetkoziJarat('FR123','Franciaország', 400, datetime.strptime("2025-06-21 14:30", "%Y-%m-%d %H:%M"))
    jarat2 = NemzetkoziJarat('US123','Amerikai Egyesült Államok', 700, datetime.strptime("2025-06-20 14:30", "%Y-%m-%d %H:%M"))
    jarat3 = BelfoldiJarat('HU123','Magyarország', 150, datetime.strptime("2025-06-23 10:30", "%Y-%m-%d %H:%M"))

    jaratok = []
    jaratok.append(jarat1)
    jaratok.append(jarat2)
    jaratok.append(jarat3)

    legitarsasag1 = LegiTarsasag('Singapore Airlines', jaratok)

    date_str = "2025-06-19 14:30"
    dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M")

    foglalas1 = JegyFoglalas('Sophia Martinez', jarat1, dt)
    foglalas2 = JegyFoglalas('Sophia Martinez', jarat2, dt)
    foglalas3 = JegyFoglalas('Jack Benton', jarat3, dt)
    foglalas4 = JegyFoglalas('Sally Taylor', jarat1, dt)
    foglalas5 = JegyFoglalas('Ray Carter', jarat3, dt)
    foglalas6 = JegyFoglalas('Frank Malcov', jarat2, dt)
    
    foglalas(foglalas1)
    foglalas(foglalas2)
    foglalas(foglalas3)
    foglalas(foglalas4)
    foglalas(foglalas5)
    foglalas(foglalas6)
    
    while True:
        print("1. Jegy foglalasa")
        print("2. Foglalas lemondasa")
        print("3. Foglalasok listazasa")
        print("4. Kilepes")

        valasztas = input("Muvelet? ")

        if valasztas == "1":
            
            nev = input("Ird meg a neved!")
            ido = datetime.now()
            jarat = input("Ird meg melyik jaratot valasztod!")
            if jarat == 'FR123':
                foglalas(JegyFoglalas(nev,jarat1,ido))
            elif jarat == 'US123':
                foglalas(JegyFoglalas(nev,jarat2,ido))
            elif jarat == 'HU123':
                foglalas(JegyFoglalas(nev,jarat3,ido))
            else:
                print("Hiba! Nincs ilyen jarat!")

        elif valasztas == "2":
            nev = input("Ird meg a neved!")
            lemondas(nev)
        elif valasztas == "3":
            listazas()
        elif valasztas == "4":
            print("Kilepes...")
            break
        else:
            print("Nem letezik ilyen muvelet!")

        

def listazas():
    print('--- Foglalasok listazasa ---')
    for foglalas in foglalasok:
        print(foglalas.nev, ":", foglalas.utazas.celallomas, ", ",foglalas.utazas.jaratszam, ", ",foglalas.utazas.jegyar)


def foglalas(foglalas: JegyFoglalas) -> int:
    foglalasok.append(foglalas)
    return foglalas.utazas.jegyar
    
def lemondas(nev: str) -> None:
    for foglalas in foglalasok:
        if foglalas.nev == nev:
            foglalasok.remove(foglalas)
    print("Foglalasok lemondva!")


if __name__ == "__main__":
    main()
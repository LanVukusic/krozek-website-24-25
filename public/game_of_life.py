import os
import time
import random

# Podatki o celici
MRTVA = "_"
ZIVA = "#"

# Podatki o mrezi
VRSTICE = 10
STOLPCI = 20


def ustvari_mrezo():
    mreza = []
    for _ in range(VRSTICE):
        vrstica = []
        for _ in range(STOLPCI):
            vrstica.append(MRTVA)
        mreza.append(vrstica)
    return mreza


def izpisi_mrezo(mreza):
    for vrstica in mreza:
        for celica in vrstica:
            print(celica, end="")
        print()


def nakljucne_celice(mreza):
    for vrstica in range(VRSTICE):
        for stolpec in range(STOLPCI):
            if random.random() < 0.3:
                mreza[vrstica][stolpec] = ZIVA


def prestej_zive_sosede(mreza, vr, st):
    s1 = mreza[vr - 1][st - 1]
    s2 = mreza[vr - 1][st]
    s3 = mreza[vr - 1][st + 1]
    s4 = mreza[vr][st - 1]
    s5 = mreza[vr][st + 1]
    s6 = mreza[vr + 1][st - 1]
    s7 = mreza[vr + 1][st]
    s8 = mreza[vr + 1][st + 1]

    sosedi = [s1, s2, s3, s4, s5, s6, s7, s8]

    zivi_sosedi = 0
    for celica in sosedi:
        if celica == ZIVA:
            zivi_sosedi += 1

    return zivi_sosedi


def naslednja_generacija(mreza):
    nova_mreza = ustvari_mrezo()

    for vrstica in range(1, VRSTICE - 1):
        for stolpec in range(1, STOLPCI - 1):
            zivi_sosedi = prestej_zive_sosede(mreza, vrstica, stolpec)
            if mreza[vrstica][stolpec] == ZIVA:
                if zivi_sosedi == 2 or zivi_sosedi == 3:
                    nova_mreza[vrstica][stolpec] = ZIVA
            else:
                if zivi_sosedi == 3:
                    nova_mreza[vrstica][stolpec] = ZIVA

    return nova_mreza


# Ustvarimo mrezo in nakljucno nastavimo celice
mreza = ustvari_mrezo()
nakljucne_celice(mreza)

# Za vedno (zanko prekinemo z uporabo Ctrl+C)
while True:
    # Izracunamo naslednjo generacijo
    mreza = naslednja_generacija(mreza)

    # Izbrisemo prejsnjo mrezo in izpisemo novo
    os.system("clear")
    izpisi_mrezo(mreza)

    # Pocakamo 0.5 sekunde
    time.sleep(0.5)

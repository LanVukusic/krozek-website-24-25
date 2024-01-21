---
title: "Game of Life"
description: "Game of Life"
pubDate: "jan 19 2024"
heroImage: "/blog-placeholder-2.jpg"
---

Implementacija Conway's Game of Life je dober projekt za začetnike, saj je potrebno uporabiti osnovne koncepte programiranja ter jih združiti v celoto.
Več o igri, si lahko preberete na [Wikipediji](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life), najbolj pomembne stvari pa so:

-   igra se odvaja na (2D) mreži, kjer vsako polje predstavlja celico,
-   celica je lahko živa ali mrtva,
-   stanje celice v naslednji generaciji je odvisno od trenutnega stanja celice in njenih sosedov in sicer:
    -   če je celica živa in ima 2 ali 3 žive sosede, ostane živa,
    -   če je celica mrtva in ima 3 žive sosede, oživi,
    -   v vseh ostalih primerih celica umre oz. ostane mrtva.

Pri implementaciji bomo poskušali uporabljati dobre prakse programiranja.

# Implementacija

Igra se odvaja na 2D mreži, ki jo bomo predstavili z `2D seznamom`. To je seznam, ki vsebuje druge sezname. Vsak podseznam predstavlja vrstico mreže, elementi v podseznamu pa predstavljajo celice v vrstici.

```
mreza = [
    [1, 2, 3], <- prva vrstica
    [4, 5, 6], <- druga vrstica
    [7, 8, 9], <- tretja vrstica
]    ^  ^  ^
     |  |  |
     |  |  tretji stolpec
     |  drugi stolpec
     prvi stolpec
```

Pri indeksiranju bomo prvo dobili vrstico, nato pa stolpec v tej vrstici - `mreza[vrstica][stolpec]`. V zgornjem primeru je `mreza[1]` seznam `[4, 5, 6]`, `mreza[1][2]` pa je `6`.
Ker bomo stanje izpisovali na zaslon, bomo stanje celice (živa oz. mrtva) predstavili s črkami. Da bomo lahko kasneje enostavno spremenili izgled izpisa, bomo na začetku programa definirali nekaj `konstant`. V Pythonu je dogovor, da se konstante pišejo z velikimi črkami. Načeloma jih lahko v programu spreminjamo, vendar se tega ne počne.

```python
# Podatki o celici
MRTVA = "_"
ZIVA = "#"

# Podatki o mreži
VRSTICE = 10
STOLPCI = 20
```

Dodali smo tudi konstanti, ki bosta določili velikost mreže.

## Ustvarjanje mreže

Ker bomo morali mrežo večkrat ustvariti, bomo to funkcionalnost napisali v funkciji, ki bo vrnila ustvarjeno mrežo. Vse celice v mreži bodo na začetku mrtve.

```python
def ustvari_mrezo():
    mreza = []
    for _ in range(VRSTICE):
        vrstica = []
        for _ in range(STOLPCI):
            vrstica.append(MRTVA)
        mreza.append(vrstica)
    return mreza

def ustvari_mrezo():
    return [[MRTVA for _ in range(STOLPCI)] for _ in range(VRSTICE)]
```

> Zgoraj sta napisana dva načina, kako lahko v Pythonu ustvarimo željeno mrežo. Možnosti je seveda še veliko. Če bom v nadaljevanju napisal več funkcij z istim imenom, pomeni da obe funkciji naredita isto stvar. Če sledite in pišete kodo je dovolj napisati samo eno od funkcij. V primeru, da napišete obe, bo Python uporabil tisto, ki je bila napisana zadnja.

## Izpis mreže

Mreže bomo morali vsak korak izpisati na zaslon. Ker bomo to počeli večkrat, bomo tudi to funkcionalnost napisali v funkciji.

```python
def izpisi_mrezo(mreza):
    for vrstica in mreza:
        for celica in vrstica:
            print(celica, end="")
        print()

def izpisi_mrezo(mreza):
    for vrstica in mreza:
        print("".join(vrstica))
```

Sedaj lahko ustvarimo mrežo in jo izpišemo.

```python
mreza = ustvari_mrezo()
izpisi_mrezo(mreza)

# Izpis (10 vrstic, 20 stolpcev):
____________________
____________________
____________________
____________________
____________________
____________________
____________________
____________________
____________________
____________________
```

## Naključne celice

Da bo igra bolj zanimiva, bomo na začetku naključno izbrali nekaj celic, ki bodo žive. To bomo naredili tako, da bomo celice v mreži naključno nastavili na `ZIVA`. Uporabili bomo Pythonovo standardno knjižnico `random`, ki nam omogoča delo z naključnimi števili.

```python
# Import ponavadi naredimo čisto na začetku programa
import random

# sledijo naše konstante in prejšnje funkcije
# ...

def nakljucne_celice(mreza):
    for vrstica in range(VRSTICE):
        for stolpec in range(STOLPCI):
            if random.random() < 0.3:
                mreza[vrstica][stolpec] = ZIVA
```

Funckija `random.random()` vrne naključno število med 0 in 1. Ker želimo, da je 30% celic živih, bomo celico nastavili na `ZIVA`, če je naključno število manjše od 0.3.

## Štetje živih sosedov

Osrednji del igre je štetje živih sosedov. Ponvono bomo logiko napisali v funkciji, ki bo vrnila število živih sosedov za celico na koordinatih `vr, st`.

```
            st - 1       st       st + 1
 vr - 1  |    s1    |    s2    |    s3    |
         ----------------------------------
   vr    |    s4    |          |    s5    |
         ----------------------------------
 vr + 1  |    s6    |    s7    |    s8    |
```

```python
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

def prestej_zive_sosede(mreza, vr, st):
    zivi_sosedi = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            zivi_sosedi += mreza[vr + i][st + j] == ZIVA
    return zivi_sosedi

def prestej_zive_sosede(mreza, vr, st):
    return sum([mreza[v][s] == ZIVA for v,s in [(vr-1, st-1), (vr-1, st), (vr-1, st+1), (vr, st-1), (vr, st+1), (vr+1, st-1), (vr+1, st), (vr+1, st+1)]])
```

Napisanih je nekaj primerov funkcij za štetje živih sosedov. Prva je napisana zelo na dolgo, najbolj primerna za začetnike. V drugi funkciji smo računanje malce posplošili (z lahkoto bi kodo spremenili, da namesto 3x3 sosedov gleda naprimer 5x5). Tretjo funkcijo sem napisal kot zanimivost, kaj lahko v Pythonu napišemo, je pa ne priporočam za začetnike. Poskušajte še sami napisati funkcijo za štetje živih sosedov.

## Naslednja generacija

Zdaj, ko znamo šteti žive sosede, lahko napišemo funkcijo, ki bo izračunala naslednjo generacijo. To bomo naredili tako, da bomo ustvarili novo mrežo. Nato bomo prešli čez vse celice v trenutni mreži in za vsako celico izračunali število živih sosedov. Glede na to število bomo nato nastavili ustrezno vrednost v novi mreži.

```python
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
```

> Pri sprehodu čez mrežo smo se izgonili prvi in zadnji vrstici ter stolpcu. Če tega nebi naredili, bi pri štetju živih sosedov prišlo do napake, saj bi poskušali dostopati do elementov, ki ne obstajajo. Poskušajte popraviti funkcijo `prestej_zive_sosede`, tako da bo delovala tudi na robu mreže (preden preverite če je določena celica živa ali mrtva, morate preveriti, če je njen indeks veljaven).

## Glavna zanka

Sedaj lahko z uporabo vseh napisanih funkcij napišemo še glavno zanko programa. V neskončni zanki bomo izračunali naslednjo generacijo, izbrisali prejšnjo mrežo ter izpisali novo. Na koncu pa bomo počakali še nekaj časa, da bomo lahko videli spremembe.
Potrebovali bomo še 2 importa iz Pythonove standardne knjižnice: `os` in `time`. Prvi nam bo omogočil brisanje zaslona, drugi pa čakanje.

```python
# Na začetku datoteke, poleg import random
import os
import time

# Konstante
# Funkcije
# ...

# Ustvarimo mrežo in naključno nastavimo celice
mreza = ustvari_mrezo()
nakljucne_celice(mreza)

# Za vedno (zanko prekinemo z uporabo Ctrl+C)
while True:
    # Izračunamo naslednjo generacijo
    mreza = naslednja_generacija(mreza)

    # Izbrišemo prejšnjo mrežo in izpišemo novo
    os.system("clear")
    izpisi_mrezo(mreza)

    # Počakamo 0.5 sekunde
    time.sleep(0.5)
```

S tem smo zaključili implementacijo Conway's Game of Life. Sedaj se lahko poigrate z začetnimi konstantami (velikost mreže, znak za živo in mrtvo celico, verjetnost, da je celica živa na začetku,...).
Poskušajte še sami kako izboljšati/spremeniti program, dodajte še kakšno funkcionalnost, napišite kakšno funkcijo drugače, `Ctrl+A delete` in začnite znova in probajte sami napisati program od začetka.
Mogoče si poglejte kakšno zunanjo knjižnico za risanje, da boste lahko igro prikazali na boljši način. Izberite si nov projekt in ga probajte implementirati. Ko se vam zatakne poglejte na Google, StackOverflow, Youtube, lahko pišete tudi nama.
Možnosti je neskončno, odvisno je samo od vaše volje za učenje in raziskovanje. Programirat se boste naučili tako, da sami pišete kodo, ob tem naletite na probleme, ki jih s pomočjo interneta poskušate rešiti. Samo poslušanje najine razlage ne bo dovolj.

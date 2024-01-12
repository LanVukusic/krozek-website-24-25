---
title: "Razredi"
description: "Razredi"
pubDate: "jan 13 2024"
heroImage: "/blog-placeholder-2.jpg"
---

Pri [podatkovnih strukturah](/blog/podatkovne-strukture/) smo spoznali terke, s katerimi smo opisali osebo.

```python
oseba = ("Matej", "Urbas", 2000, "Ljubljana", True)
```

Problem terk je, da ne moremo dostopati do elementov po imenu. Če želimo dostopati do imena, moramo vedeti, da je to prvi element terke.

```python
oseba[0] # "Matej"
```

Če bi želeli dostopati do elementov po imenu, bi lahko uporabili slovar.

```python
oseba = {
    "ime": "Matej",
    "priimek": "Urbas",
    "leto_rojstva": 2000,
    "kraj_rojstva": "Ljubljana",
    "student": True
}

oseba["ime"] # "Matej"
```

Kaj pa če bi želeli predstaviti osebo? Lahko bi definirali funkcijo `predstavi`, ki bi izpisala vse podatke o osebi.

```python
def predstavi(oseba):
    print(f"Sem {oseba['ime']} {oseba['priimek']}, rojen v {oseba['kraj_rojstva']} leta {oseba['leto_rojstva']}. Trenutno {'sem' if oseba['student'] else 'nisem'} študent.")

predstavi(oseba) # Sem Matej Urbas, rojen v Ljubljana leta 2000. Trenutno sem študent.

oseba2 = {
    "ime": "Janez",
    "priimek": "Novak",
    "leto_rojstva": 1990,
    "kraj_rojstva": "Maribor",
    "student": False
}

predstavi(oseba2) # Sem Janez Novak, rojen v Maribor leta 1990. Trenutno nisem študent.
```

Sedaj imamo podatkovno strukturo, ki hrani informacije o osebi in funkcijo, ki to osebo predstavi. Ti dve stvari bi bilo smiselno združiti v eno celoto. To lahko naredimo s pomočjo `razredov`.

## Razredi (class)

Razredi so sprva lahko dokaj zakomplicirani, tukaj bomo predstavili osnove, več pa seveda lahko najdete na Googlu oziroma v [uradni dokumentaciji](https://docs.python.org/3/tutorial/classes.html).

Razredi so nekakšen `blueprint` iz katerega lahko ustvarimo `objekte` (lahko si jih predstavljate kot bolj napredne slovarje), ki hranijo podatke in nudijo množico uporabnih funkcij nad temi podatki.

Razred definiramo z uporabo ključne besede `class` in imena razreda (v `CamelCase`). V razredu definiramo `metode`. To so funkcije, ki pripadajo razredu. Metode definiramo enako kot funkcije, le da jih definiramo znotraj razreda. Prvi parameter metode je vedno `self`, ki predstavlja trenutni objekt.

To je bilo kar veliko nove, zakomplicirane teorije, zato si poglejmo primer.

```python
class Oseba:
    def __init__(self, ime, priimek, leto_rojstva, kraj_rojstva, student):
        self.ime = ime
        self.priimek = priimek
        self.leto_rojstva = leto_rojstva
        self.kraj_rojstva = kraj_rojstva
        self.student = student

    def predstavi(self):
        print(f"Sem {self.ime} {self.priimek}, rojen v {self.kraj_rojstva} leta {self.leto_rojstva}. Trenutno {'sem' if self.student else 'nisem'} študent.")
```

Razred `Oseba` ima dve metodi: `__init__` in `predstavi`. Metoda `__init__` je posebna metoda, ki se izvede ob ustvarjanju objekta. Ta metoda se imenuje `konstruktor`. V konstruktorju definiramo spremenljivke, ki jih bo objekt hranil. Te spremenljivke imenujemo `atributi` objekta. Atribute definiramo z `self.ime_spremenljivke = vrednost`. `self` je objekt, ki ga ustvarjamo, torej `self.ime_spremenljivke` pomeni, da ustvarimo atribut `ime_spremenljivke` na objektu `self`.

Metoda `predstavi` je enaka kot funkcija `predstavi` iz prejšnjega primera, le da je definirana znotraj razreda in ima prvi parameter `self`.

Sedaj lahko ustvarimo objekt razreda `Oseba`.

```python
oseba1 = Oseba("Matej", "Urbas", 2000, "Ljubljana", True)
oseba1.predstavi() # Sem Matej Urbas, rojen v Ljubljana leta 2000. Trenutno sem študent.

oseba2 = Oseba("Janez", "Novak", 1990, "Maribor", False)
oseba2.predstavi() # Sem Janez Novak, rojen v Maribor leta 1990. Trenutno nisem študent.
```

Tukaj bomo končali. Razredi ponujajo še veliko drugih uporabnih funkcionalnosti, ki pa jih ne bomo podrobneje obravnavali.

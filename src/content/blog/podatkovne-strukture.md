---
title: "Podatkovne strukture"
description: "Podatkovne strukture"
pubDate: "jan 6 2024"
heroImage: "/blog-placeholder-2.jpg"
---

Do sedaj smo podatke v programu shranjevali s pomočjo [spremenljivk](/blog/osnove-pythona/) in [seznamov](/blog/seznami). S samo tema dvema načinoma shranjevanja podatkov lahko že rešimo vse možne izračunljive probleme. Python pa ima na voljo še veliko drugih načinov shranjevanja podatkov, ki so bolj primerni za določene probleme.

## Terke (tuple)

Terke so podobne seznamom, le da jih ne moremo spreminjati. To pomeni, da jih lahko uporabljamo za shranjevanje podatkov, ki se ne bodo spreminjali. Terke so definirane z oklepaji `()` in elementi so ločeni z vejico `,`. Do njihovih elementov dostopamo na enak način kot pri seznamih.

```python
terka = (1, "Matej", True)

print(terka[0]) # 1
print(terka[1]) # Matej
print(terka[2]) # True
```

Pri seznamih se poskušamo izogibati različnim tipom elementov, pri terkah pa ponavadi shranjujemo različne tipe elementov. Terke so uporabne, kadar želimo shraniti več podatkov, ki so med seboj povezani. Na primer, če želimo shraniti podatke o osebi, lahko uporabimo terko.

```python
oseba = ("Matej", "Urbas", 2000, "Ljubljana", True)
```

Terko lahko `razpakiramo` v več spremenljivk.

```python
oseba = ("Matej", "Urbas", 2000, "Ljubljana", True)

ime, priimek, leto_rojstva, kraj_rojstva, je_student = oseba

print(ime) # Matej
print(priimek) # Urbas
```

## Slovarji (dictionary)

Slovarji so podobni seznamom, le da imajo namesto indeksov ključe. Ključi so lahko poljubnega (`hashable`) tipa. Slovarji so definirani z zavitimi oklepaji `{}`. Ključ in vrednost sta ločena z dvopičjem `:`. Elementi so ločeni z vejico `,`. Do elementov dostopamo z uporabo ključa.

```python
slovar = {
    "ime": "Matej",
    "priimek": "Urbas",
    "starost": 23
}

print(slovar["ime"]) # Matej
print(slovar["priimek"]) # Urbas
print(slovar["starost"]) # 23
print(slovar["naslov"]) # KeyError: 'naslov'
```

Dodajanje novega ali spreminjanje stareg elementa v slovar je zelo enostavno.

```python
slov["naslov"] = "Tolmin"
```

### Uporabne metode slovarjev

Slovarji imajo nekaj metod, ki nam olajšajo delo z njimi:

-   `keys()` - vrne seznam vseh ključev slovarja
-   `values()` - vrne seznam vseh vrednosti slovarja
-   `items()` - vrne seznam vseh parov (terk) ključ-vrednost slovarja
-   `get(ključ)` - vrne vrednost ključa, če obstaja, sicer vrne `None`
-   `get(ključ, privzeta_vrednost)` - vrne vrednost ključa, če obstaja, sicer vrne privzeto vrednost

```python
slovar = {
    "ime": "Matej",
    "priimek": "Urbas",
    "starost": 23
}

print(slovar.keys()) # dict_keys(['ime', 'priimek', 'starost'])
print(slovar.values()) # dict_values(['Matej', 'Urbas', 23])
print(slovar.items()) # dict_items([('ime', 'Matej'), ('priimek', 'Urbas'), ('starost', 23)])
print(slovar.get("ime")) # Matej
print(slovar.get("naslov")) # None
print(slovar.get("naslov", "Tolmin")) # Tolmin
```

## Množice (set)

Množice so `neurejeni` seznami `unikatnih` elementov. Množice so definirane z zavitimi oklepaji `{}`. Elementi so ločeni z vejico `,`.

```python
mnozica1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
mnozica2 = {5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}

print(mnozica1.intersection(mnozica2)) # {5, 6, 7, 8, 9, 10}
print(mnozica1.union(mnozica2)) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}
print(mnozica1.difference(mnozica2)) # {1, 2, 3, 4}
```

Z množicami lahko hitreje preverimo ali element obstaja v množici.

```python
mnozica = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

print(1 in mnozica) # True
print(11 in mnozica) # False
```

To sicer zgleda enako kot pri seznamih, vendar je računska zahtevnost pri seznamu `O(n)`, pri množici pa `O(1)`. To pomeni, da je preverjanje ali element obstaja v množici veliko hitrejše kot pri seznamu. V podrobnosti se sicer ne bomo spuščali, temu je namenjeno več predmetov na fakulteti.

Tudi druge operacije z množicami so veliko hitrejše kot pri seznamih, imajo pa seveda nekaj omejitev:

-   elementi množice morajo biti `hashable` (števila, nizi, terke, ...)
-   množica ne more vsebovati več enakih elementov
-   zaporedje elementov v množici ni definirano
-   ...

## Iteracija čez podatkovne strukture

Vse podatkovne strukture, ki smo jih spoznali, so `iterable`. To pomeni, da jih lahko uporabimo v zanki `for`.

```python
seznam_terk = [("Matej", True), ("Lan", True), ("Luka", False)]

for element in seznam_terk:
    print(element)

# ('Matej', True) <- izpiše terko
# ('Lan', True)
# ('Luka', False)
```

Elemente lahko `razpakiramo` v več spremenljivk kar v zanki `for`.

```python
for ime, student in seznam_terk:
    print(ime, student)

# Matej True <- prvi element je niz, drugi pa bool
# Lan True
# Luka False
```

Tako lahko hitro iteriramo tudi čez slovarje.

```python
slovar = {
    "ime": "Matej",
    "priimek": "Urbas",
    "starost": 23
}

# klic funkcije items() vrne seznam terk ključ-vrednost
for kljuc, vrednost in slovar.items():
    print(kljuc, vrednost)

# ime Matej
# priimek Urbas
# starost 23
```

Iteracija čez slovar pa nam podaja ključe.

```python
for kljuc in slovar:
    print(kljuc)
    print(slovar[kljuc])

# ime
# Matej
# priimek
# Urbas
# starost
# 23
```

## Comprehension

Python ima zelo uporabno sintakso za ustvarjanje seznamov, ki se imenuje `list comprehension`. Z njim lahko ustvarimo seznam na zelo enostaven način. Podrobnosti je veliko, tukaj pa bomo predstavili le osnovno uporabo.

```python
seznam = [i for i in range(5)]
kvadrati = [i ** 2 for i in range(5)]

print(seznam) # [0, 1, 2, 3, 4]
print(kvadrati) # [0, 1, 4, 9, 16]
```

List comprehension lahko uporabimo tudi za ustvarjanje slovarjev.

```python
slovar = {i: i ** 2 for i in range(5)}

print(slovar) # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

V list comprehension lahko dodamo še `if` stavek, s katerim lahko filtriramo elemente.

```python
seznam = [i for i in range(10) if i % 2 == 0]

print(seznam) # [0, 2, 4, 6, 8]
```

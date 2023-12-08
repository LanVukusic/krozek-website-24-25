---
title: "Funkcije"
description: "Funkcije"
pubDate: "dec 9 2023"
heroImage: "/blog-placeholder-2.jpg"
---

Predstavljajte si, da na večih mestih v programu izvajate enako zaporedje ukazov, nato pa ugotovite, da ste se pri enem ukazu zmotili in ga morate popraviti. Popraviti pa ga morate na vseh mestih, kjer se je pojavil. To je lahko zelo zamudno in naporno. Prav tako je možnost napak velika. V takem primeru je smiselno to zaporedje ukazov `zapisati` le enkrat in ga nato `klicati` na vsakem mestu, kjer ga potrebujemo. To lahko naredimo z uporabo `funkcij`.

Funkcijo v pythonu definiramo z uporabo ključne besede `def`. Sledi `ime` funkcije, nato `oklepaji` in `dvopičje`. Kodo v `telesu` funkcije moramo zamakniti za 4 presledke (1 `tab`). Pametnejši urejevalniki kode to naredijo sami.

```py
def pozdravi():
    print("Živijo!")
```

Definirali smo funkcijo `pozdravi`, ki izpiše `Živijo!`. Če poženemo program, se ne zgodi nič, saj smo funkcijo le `definirali`, moramo jo pa še `poklicati`. To naredimo tako, da napišemo ime funkcije in dodamo oklepaje.

```py
pozdravi() # Živijo!
```

Funkcijo lahko kličemo večkrat:

```py
pozdravi() # Živijo!
pozdravi() # Živijo!
...
pozdravi() # Živijo!
pozdravi() # Živijo!
```

Če bi sedaj želeli spremeniti besedilo, ki ga funkcija izpiše, bi to morali storiti le na enem mestu. To je velika prednost funkcij. Spremenimo besedilo:

```py
def pozdravi():
    print("Spremenjeno besedilo")

pozdravi() # Spremenjeno besedilo
pozdravi() # Spremenjeno besedilo
pozdravi() # Spremenjeno besedilo
```

Seveda lahko v telesu funkcije napišemo tudi več ukazov.

## Argumenti

Funkciji lahko podamo tudi `argumente`. To so podatki, ki jih funkcija potrebuje za svoje delovanje. Argumente podamo v oklepajih, ločene z vejico. V telesu funkcije jih lahko uporabimo kot spremenljivke.

```py
def pozdravi(ime):
    print(f"Živijo {ime}!")

pozdravi("Matej") # Živijo Matej!
pozdravi("Lan") # Živijo Lan!
pozdravi("svet") # Živijo svet!
```

Vendar pazi, sedaj moraš funkciji vedno podati argument, sicer bo prišlo do napake.

```py
pozdravi()
```

```
Traceback (most recent call last):
  File "<pot/do/datoteke>", line 1, in <module>
TypeError: pozdravi() missing 1 required positional argument: 'ime'
```

Temu se lahko izognemo z uporabo `privzetih vrednosti` argumentov. To pomeni, da lahko argumentu določimo vrednost, ki se uporabi, če argumenta ne podamo. Za uporabo privzetih vrednosti je še nekaj tehnikalij, zato jih sedaj še ne bomo obravnavali.

Funkcija lahko sprejme tudi več argumentov.

```py
def opisi(ime, priimek, starost):
    print(f"Sem {ime} {priimek}. Star sem {starost} let.")

opisi("Matej", "Urbas", 23) # Sem Matej Urbas. Star sem 23 let.
```

> Vas to kaj spominja na `print`?

## Vrnitev vrednosti

Samo z argumenti pa ne moremo narediti veliko. Velikokrat želimo dati funkciji neke podatke, ki jih funkcija obdela, nato pa želimo dobljen rezultat uporabiti nekje drugje v programu. To storimo s ključno besedo `return`.

```py
def zmnozi(a, b):
    return a * b

zmnozi(2, 3) # ne izpiše ničesar
a = zmnozi(2, 3) # to NI isti a kot v funkciji
b = zmnozi(4, 2) # to NI isti b kot v funkciji
print(zmnozi(b, a)) # 48
```

`return` nemudoma prekine izvajanje funkcije.

```py
def primerjaj(a, b):
    if a > b:
        print("a je večje od b")
        return a + b

    print("a je manjše od b")
    return a**2

primerjaj(2, 3) # a je manjše od b
x = primerjaj(3, 2) # a je večje od b
print(x) # 5
```

V primeru, da velja `a > b` se funkcija zaključi, preden pride do drugega `print` ukaza, kljub temu, da nismo uporabili `else`.

## Rekurzija (dodatno)

Nič nam ne preprečuje, da v telesu funkcije kličemo funkcijo, v kateri smo. Temu pravimo `rekurzija`. Eden izmed enostavnejših primerov rekurzije je izračun `fakultete`. Fakulteta je produkt vseh naravnih števil od 1 do n. Zapišemo jo kot `n!`. Na primer `5! = 1 * 2 * 3 * 4 * 5 = 120`.

```py
def fakulteta(n):
    return fakulteta(n - 1) * n

fakulteta(5) # OJOJ, program crashne
```

> Pomislite, kaj se je tukaj v resnici zgodilo.

Rekurzivni programi potrebujejo `ustavitveni pogoj`. Poskusimo še enkrat.

```py
def fakulteta(n):
    if n == 1:
        return 1
    return n * fakulteta(n - 1)

print(fakulteta(5)) # 120
```

Kaj se dejansko zgodi?

-   pokličemo `fakulteta(5)`
-   ker `5 != 1` se izvede `return 5 * fakulteta(4)`
-   ker `4 != 1` se izvede `return 4 * fakulteta(3)`
-   ker `3 != 1` se izvede `return 3 * fakulteta(2)`
-   ker `2 != 1` se izvede `return 2 * fakulteta(1)`
-   ker `1 == 1` se izvede `return 1`
-   `fakulteta(1)` vrne `1`
-   `fakulteta(2)` vrne `2 * 1 = 2`
-   `fakulteta(3)` vrne `3 * 2 = 6`
-   `fakulteta(4)` vrne `4 * 6 = 24`
-   `fakulteta(5)` vrne `5 * 24 = 120`

Več o rekurziji ne bomo govorili, saj je to že precej napredna tema.

## Naloge

1. Napiši funkcijo `soda`, ki sprejme število in vrne `True`, če je število sodo, in `False`, če je liho.

2. Napiši funkcijo `povprecje`, ki sprejme 3 števila in vrne njihovo povprečje.

3. Napiši funkcijo `najvecji`, ki sprejme 3 števila in vrne največje izmed njih.

4. Napiši funkcijo `povrsina`, ki sprejme `oblika` (niz) in `stevilo` ter vrne ploščino dane oblike. Na voljo naj bodo naslednje oblike: `krog`, `trikotnik`, `kvadrat`. Primer uporabe: `povrsina("krog", 3)` vrne ploščino kroga s polmerom 3.

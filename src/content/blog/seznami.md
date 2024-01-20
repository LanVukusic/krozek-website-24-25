---
title: "Seznami"
description: "Seznami"
pubDate: "dec 16 2023"
heroImage: "/seznami.jpg"
---
`Avtor slike: Teja Rutar`

Seznam je vrsta spremenljivke (podatkovna struktura), ki vsebuje več podatkov. Seznam definiramo z uporabo oglatih oklepajev `[]`. Elemente seznama ločimo z vejico `,`. Seznam lahko vsebuje različne podatkovne tipe, vendar je to slaba praksa.

```py
seznam_nizov = ["Jabolko", "Hruška", "Mandarina"]
seznam_stevil = [-5, 0, 5, 10]
prazen_seznam = []

# ne delat tega
mesan_seznam = ["Jabolko", 5, 10.5, True]
```

## Dostop do elementov

Elemente seznama lahko dostopamo preko indeksa. Indeks elementa je njegova številka v seznamu. Prvi element ima indeks **0**, drugi 1, tretji 2, itd. Indeks elementa podamo v oglatih oklepajih `[]` za seznamom.

```py
drzave = ["Slovenija", "Hrvaška", "Avstrija", "Italija"]

print(drzave[0]) # Slovenija
print(drzave[1]) # Hrvaška
print(drzave[2]) # Avstrija
print(drzave[3]) # Italija
```

Če poskušamo dostopati do elementa, ki ne obstaja, dobimo napako.

```py
print(drzave[4]) # IndexError: list index out of range
```

V Pythonu je možna tudi uporaba `negativnih` indeksov. V tem primeru se šteje od konca seznama. Zadnji element ima indeks **-1**, predzadnji **-2**, itd.

```py
print(drzave[-1]) # Italija
print(drzave[-4]) # Slovenija
```

## Rezinjanje (slicing)

Včasih želimo dostopati do več elementov hkrati. To naredimo s `rezinjanjem` (ang. slicing). Rezinjanje omogoča, da iz seznama izberemo podseznam. Podseznam izberemo tako, da podamo začetni in končni indeks, ločena z dvopičjem `:`. Začetni indeks je vključen, končni pa izključen. Če izpustimo začetni indeks, se začne rezinjanje na začetku seznama. Če izpustimo končni indeks, se rezinjanje konča na koncu seznama.

```py
print(drzave[0:2]) # ["Slovenija", "Hrvaška"]
print(drzave[1:4]) # ["Hrvaška", "Avstrija", "Italija"]
```

Dodamo pa lahko tudi tretji argument, ki določa korak. Če je korak pozitiven, se rezinjanje izvaja od začetnega do končnega indeksa. Če je korak negativen, se rezinjanje izvaja od končnega do začetnega indeksa.

```py
print(drzave[0:4:2]) # ["Slovenija", "Avstrija"]
print(drzave[3:0:-1]) # ["Italija", "Avstrija", "Hrvaška"]
print(drzave[::-1]) # ["Italija", "Avstrija", "Hrvaška", "Slovenija"]
```

## Spreminjanje elementov

Elemente seznama lahko spreminjamo. Z indeksom določimo element, ki ga želimo spremeniti, nato pa mu priredimo novo vrednost.

```py
drzave[1] = "Francija"
drzave[-1] = "Nemčija"
print(drzave) # ["Slovenija", "Francija", "Avstrija", "Nemčija"]
```

## Dodajanje elementov

Elemente seznama lahko dodajamo na konec seznama. To naredimo z metodo `append`.

```py
stevilke = [1, 2, 3]
stevilke.append(4)
print(stevilke) # [1, 2, 3, 4]
```

Z uporabo metode `insert` lahko dodamo element na poljubno mesto v seznamu. Metoda `insert` sprejme dva argumenta: indeks, na katerega želimo dodati element, in element, ki ga želimo dodati. Vsi elementi za tem mestom se premaknejo za eno mesto naprej.

```py
stevilke.insert(1, 5)
print(stevilke) # [1, 5, 2, 3, 4]
```

Če poskušamo seznamu dodati seznam, se bo seznam dodal kot element. Če želimo dodati elemente seznama, moramo uporabiti metodo `extend`.

```py
stevilke.append([6, 7])
print(stevilke) # [1, 5, 2, 3, 4, [6, 7]]

stevilke = stevilke[:-1] # odstranimo zadnji element
stevilke.extend([6, 7])
print(stevilke) # [1, 5, 2, 3, 4, 6, 7]
```

## Odstranjevanje elementov

Z uporabo metode `pop` lahko odstranimo element na določenem indeksu. Metoda `pop` vrne odstranjeni element. Z metodo `remove` pa odstranimo prvi element, ki se ujema z vrednostjo, ki jo podamo kot argument.

```py
stevilke = [1, 2, 3, 4, 5, 6, 7, 8, 8]
stevilke.pop(0) # odstrani 1
stevilke.pop(5) # odstrani 7
stevilke.remove(8) # odstrani prvo 8
print(stevilke) # [2, 3, 4, 5, 6, 8]
```

## Operacije s seznami

Sezname lahko seštevamo, množimo in preverjamo ali vsebujejo elemente.

```py
stevilke = [1, 2, 3]
stevilke = stevilke + [4, 5, 6]
print(stevilke) # [1, 2, 3, 4, 5, 6]

stevilke = stevilke * 2
print(stevilke) # [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]

print(1 in stevilke) # True
print(10 in stevilke) # False
```

## Še nekaj uporabnih metod

-   `clear()` - odstrani vse elemente iz seznama
-   `count(arg)` - vrne število pojavitev elementa `arg` v seznamu
-   `index(arg)` - vrne indeks prvega elementa, ki se ujema z `arg`
-   `reverse()` - obrne vrstni red elementov v seznamu
-   `sort()` - uredi elemente seznama
-   `len(seznam)` - vrne število elementov v seznamu

## Napredno

### Posebnosti pri delu s seznami

Seznami so samo naslovi na podatke v pomnilniku, tako da imamo lahko več spremenljivk, ki kažejo na isti seznam. Če spremenimo eno spremenljivko, se spremeni tudi druga.

```py
seznam1 = [1, 2, 3]
seznam2 = seznam1

seznam1[0] = 5
print(seznam1) # [5, 2, 3]
```

Prav tako moramo biti pozorni, ko sezname podajamo kot argumente funkcijam. Če funkcija spremeni seznam, se bo spremenil tudi izven funkcije.

```py
def dodaj_element(seznam):
    seznam.append(5)

seznam = [1, 2, 3, 5]
dodaj_element(seznam)
print(seznam) # [1, 2, 3, 5]
```

### Večdimenzionalni seznami

Seznam lahko vsebuje tudi druge sezname. Tako dobimo večdimenzionalni seznam. V tem primeru je indeksiranje malo bolj zapleteno.

```py
tic_tac_toe = [
    ["X", "O", "X"],
    ["O", "X", "O"],
    ["X", "O", "X"]
]

print(tic_tac_toe[0]) # ["X", "O", "X"]
print(tic_tac_toe[0][0]) # "X"
```

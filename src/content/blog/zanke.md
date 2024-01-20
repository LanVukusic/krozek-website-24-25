---
title: "Zanke"
description: "Zanke"
pubDate: "dec 16 2023"
heroImage: "/zanke.jpg"
---
`Avtor slike: Teja Rutar`

Če bi želeli v terminal 5x izpisati določeno spremenljivko, bi to sedaj to naredili takole:

```py
niz = "Živijo"

print(niz)
print(niz)
print(niz)
print(niz)
print(niz)
```

To sicer deluje, vendar pa je to zelo nepraktično, saj moramo vsakič napisati `print(niz)`. Če bi želeli izpisati 100x, bi morali to napisati 100x. Če želimo, da se nekaj izvede večkrat, uporabimo zanko. Zanka je del kode, ki se izvaja večkrat. V Pythonu poznamo dve vrsti zank: `while` in `for`.

## For zanka

For zanka se uporablja, ko želimo, da se nekaj izvede točno določeno število krat. Na primer, če želimo izpisati nekaj 5x, uporabimo for zanko.

```py
niz = "Živijo"

for i in range(5):
    print(niz)
```

Kaj se je tukaj zgodilo?

-   zanko začnemo s ključno besedo `for`
-   sledi opcijska spremenljivka, ki jo bomo zaenkrat preskočili
-   nato sledi ključna beseda `in`
-   nato sledi `range(5)`, kar pomeni, da se bo zanka izvedla 5x
-   nato sledi dvopičje, telo zanke pa je zamaknjeno

Zanka se torej izvede 5x, vsakič pa se izpiše vrednost spremenljivke `niz`.

Sedaj pa podrobneje pogledamo spremenljivko med `for` in `in`. Spremenljivka (v zgornjem primeru `i`) dobi vsako `iteracijo` zanke novo vrednost. Ta vrednost pa je odvisna od tega, kaj je napisano med `in` in `:`.
V zgornjem primeru smo uporabili `range(5)`. Funkcija `range(n)` za nas naredi seznam števil od 0 do n-1. (Bolj podrobneje naredi `generator`, vendar je to out-of-scope krožka) V našem primeru je to torej `[0, 1, 2, 3, 4]`. Sedaj bo spremenljivka `i` "hodila" po seznamu in dobila vrednost 0, 1, 2, 3 in 4. Vsakič, ko se bo zanka izvedla, bo spremenljivka `i` dobila novo vrednost.

```py
for i in range(5):
    print(i)

# izpiše:
# 0
# 1
# 2
# 3
# 4
```

Funkcija `range` lahko podobno kot pri rezanju seznamov in nizov sprejme več argumentov:

-   če je argument en sam predstavlja zgornjo mejo (spodnja meja je 0)
-   če sta argumenta dva, predstavljata spodnjo in zgornjo mejo
-   če so argumenta trije, predstavljata spodnjo in zgornjo mejo ter korak

Spodnja meja je `inclusive`, zgornja meja pa `exclusive`. To pomeni, da je spodnja meja vključena v seznam, zgornja pa ne.

Poskušajmo izpisati vsa soda števila med 10 in vključno 20

```py
for i in range(10, 21, 2):
    print(i)
```

Pri opisu funkcije `range` smo omenili, da ta funkcija za nas naredi seznam. Seveda pa lahko v `for` zanko podamo tudi svoj seznam.

```py
drzave = ["Slovenija", "Hrvaška", "Avstrija", "Italija"]

for drzava in drzave:
    print(drzava)
```

## While zanka

While zanka se izvaja toliko časa dokler je pogoj resničen.

```py
i = 0

while i < 5:
    print(i)
    i += 1
```

## Continue in break

Včasih pa želimo zanko prekiniti predčasno. To lahko naredimo z `break` ali pa preskočimo trenutno iteracijo z `continue`.

```py
for i in range(10):
    if i == 5:
        break
    print(i)

# izpiše:
# 0
# 1
# 2
# 3
# 4
```

```py
for i in range(10):
    if i == 5:
        continue
    print(i)

# izpiše:
# 0
# 1
# 2
# 3
# 4
# 6
# 7
# 8
# 9
```

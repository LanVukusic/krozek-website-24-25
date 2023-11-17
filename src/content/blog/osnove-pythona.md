---
title: 'Osnove pythona'
description: 'Osnovni koncepti programeskega jezika python3'
pubDate: 'nov 11 2023'
heroImage: '/blog-2.png'
---

Python je `interpretirani` programski jezik, kar pomeni da moramo za zagon programa imeti nameščen Pythonov `interpreter`. Interpreter nato bere našo kodo in jo izvaja vrstico za vrstico. Najbolje, da kar začnemo z najenostavnejšim programom v Pythonu, ki izpiše besedilo `Hello World!`.

## Izpisovanje v konzolo

Ustvarimo datoteko `hello.py` in v njo vpišemo:

```python
print("Hello World!")
```

Vsebino datoteke nato shranimo (`Ctrl + S`) in zaženemo v terminalu z ukazom `python`:

```shell
krozek@DESKTOP:~$ python hello.py
Hello World!
krozek@DESKTOP:~$
```

> Od tu naprej ne bom več pisal ukazov v terminalu, saj se bodo lahko vaše poti razlikovale. Prav tako nas zares zanima samo izpis Python programa.

Pa poglejmo ta program malo bolj podrobno:

- `print` je `funkcija`, ki izpiše vsebino znotraj oklepajev
- `"Hello World!"` je `argument` funkcije `print`
- `"` označuje začetek in konec `niza` (ang. `string`)

V nizu lahko napišemo poljubno besedilo, ki ga želimo izpisati.

```python
print("Pozdravljen svet!")
```

izpiše

```shell
Pozdravljen svet!
```

## Komentarji

Komentarji so del kode, ki se ne izvaja. Uporabljamo jih za opisovanje kode, da jo lažje razumemo. V Pythonu komentarje označimo z znakom `#`.

```python
# To je komentar
print("Pozdravljen svet!")
```

izpiše
```shell
Pozdravljen svet!
```
Interpreter bo vse kar sledi za znakom `#`, do konca vrstice, ignoriral.

## Spremenljivke

Želeli bi petkrat zapored izpisati `Pozdravljen svet`. Lahko bi napisali:
```python
print("Pozdravljen svet!")
print("Pozdravljen svet!")
print("Pozdravljen svet!")
print("Pozdravljen svet!")
print("Pozdravljen svet!")
```
Če poženemo program, dobimo želeni izpis:
```shell
Pozdravljen svet!
Pozdravljen svet!
Pozdravljen svet!
Pozdravljen svet!
Pozdravljen svet!
```

> Kasneje se bomo naučili, da za takšen izpis obstaja še boljši način.

Kaj pa če bi sedaj želeli namesto `Pozdravljen svet` izpisati `Danes je lep dan`? Morali bi spremeniti vsako vrstico, kar je zelo naporno. V ta namen bomo ustvarili novo `spremenljivko`, ter jo nato izpisali petkrat.

```python
besedilo = "Pozdravljen svet"
print(besedilo)
print(besedilo)
print(besedilo)
print(besedilo)
print(besedilo)
```

izpiše

```txt
Pozdravljen svet!
Pozdravljen svet!
Pozdravljen svet!
Pozdravljen svet!
Pozdravljen svet!
```

Sedaj lahko samo spremenimo `vrednost` spremenljivke in ne več vsakega izpisa posebej.

```python
besedilo = "Danes je lep dan"
print(besedilo)
print(besedilo)
print(besedilo)
print(besedilo)
print(besedilo)
```

izpiše

```txt
Danes je lep dan!
Danes je lep dan!
Danes je lep dan!
Danes je lep dan!
Danes je lep dan!
```

Kot nam že ime spremenljivka pove, jo lahko `spreminjamo` med izvajanjem programa

```python
besedilo = "Danes je lep dan"
print(besedilo)
print(besedilo)
besedilo = "Jutri bo lepši dan"
print(besedilo)
print(besedilo)
print(besedilo)
```

izpiše

```txt
Danes je lep dan!
Danes je lep dan!
Jutri bo lepši dan!
Jutri bo lepši dan!
Jutri bo lepši dan!
```

### Tipi spremenljivk

Python ima več različnih privzetih tipou spremenljivk:

- celo število (ang. `integer`) `x = 5`
- decimalno število (ang. `float`) `x = 4.2`
- niz (ang. `string`) `x = "Pozdravljen svet"` 
- logična vrednost (ang. `boolean`) `x = True` ali `x = False`

Kasneje bomo spoznali še druge tipe:

- seznam (ang. `list`)
- slovar (ang. `dictionary`)
- množica (ang. `set`)
- terka (ang. `tuple`)
- ...

Pythona sicer ne moti, da med izvajanjem programa spremenimo tip spremenljivke, vendar pa je to **zelo slaba praksa**.
```python
x = 5
print(x)
x = "Pozdravljen svet"
print(x)
```
izpiše
```shell
5
Pozdravljen svet
```

### Osnovne operacije nad spremenljivkami

#### Števila

S števili lahko izvajamo vse osnovne operacije:
- seštevanje `+`
- odštevanje `-`
- množenje `*`
- deljenje `/`
- celoštevilsko deljenje `//`
- potenciranje `**`
- ostanek pri deljenju `%`

```python
x = 5
y = 3
print(x + y) # 8
print(x - y) # 2
print(x * y) # 15
print(x / y) # 1.6666666666666667
print(x // y) # 1
print(x ** y) # 125
print(x % y) # 2
```

Rezultat operacije lahko `priredimo` spremenljivki.
```python
z = x + y
print(z) # 8
```

Ker je v programiranju znak `=` uporabljen za **prirejanje** in ne za **enakost** lahko z njim priredimo tudi spremenljivko sama sebi.
```python
x = x + 5
print(x) # 10
```

Velikokrat se zgodi, da želimo spremenljivko nekako spremeniti za določeno vrednost. V ta namen lahko uporabimo krajše zapise:
```python
x += 5 # x = x + 5
print(x) # 15
x *= 3 # x = x * 3
print(x) # 45
```
Krajši zapisi obstajajo za vse osnovne operacije:
- `x += y` je enako kot `x = x + y`
- `x -= y` je enako kot `x = x - y`
- `x *= y` je enako kot `x = x * y`
- `x /= y` je enako kot `x = x / y`
- `x //= y` je enako kot `x = x // y`
- `x **= y` je enako kot `x = x ** y`
- `x %= y` je enako kot `x = x % y`

Vendar, največkrat uporablajmo samo prve 4 (`+=`, `-=`, `*=`, `/=`).

#### Nizi

Nize lahko:
- seštevamo `+`
- množimo `*`
- indeksiramo `[]`
- rezinamo `[:]` (ang. **slicing**)
- formatiramo `{}`

```python
x = "Pozdravljen"
y = "svet"
print(x + " " + y) # Pozdravljen svet
print(x * 3) # PozdravljenPozdravljenPozdravljen
print(f"{x} {y}") # Pozdravljen svet

print(x[0]) # P
print(x[1]) # o
print(x[5:10]) # avlje
print(x[5:]) # avljen
print(x[:5]) # Pozdr
print(x[-1]) # n
print(x[5:-3]) # avl
print(x[::-1]) # nejlvardzoP
```
> O indeksiranju bomo bolj podrobno govorili pri seznamih.

#### Logične vrednosti

Logične vrednosti so `True` in `False`. Z njimi lahko izvajamo osnovne logične operacije:
- `and` (in)
- `or` (ali)
- `not` (ne)

```python
x = True
y = False
print(x and y) # False
print(x or y) # True
print(not x) # False
print(not y) # True
```
Osnovne logične operacije so definirane v sledeči tabeli:

| `x` | `y` | `x and y` | `x or y` | `not x` | `not y` |
| --- | --- | --------- | -------- | ------- | ------- |
| `True` | `True` | `True` | `True` | `False` | `False` |
| `True` | `False` | `False` | `True` | `False` | `True` |
| `False` | `True` | `False` | `True` | `True` | `False` |
| `False` | `False` | `False` | `False` | `True` | `True` |

#### Primerjava

Spremenljivke lahko primerjamo med seboj. Rezultat primerjave je logična vrednost (`True` ali `False`):
- `x == y` (enako)
- `x != y` (različno)
- `x > y` (večje)
- `x < y` (manjše)
- `x >= y` (večje ali enako)
- `x <= y` (manjše ali enako)

```python
x = 5
y = 3
print(x == y) # False
print(x != y) # True
print(x > y) # True
print(x < y) # False
print(x >= y) # True
print(x <= y) # False
```

## Vaje

Za reševanje vaj si pomagjate z **GOOGLOM!!**  
Koda ne bo delovla takoj... to je pričakovano. Kodo poskusite zagnati in spreminjati dokler ne začne delovati.  
Srečno.

### Pretvorba enot

Napištie program, ki spremenljivko `vhod` v katero zapišemo kot v stopinjah, pretvori v radijane in rezultat _lepo_ izpiše.  

Dopolnite spodnji program do delujočega.

```py
vhod = 90 # stopinj
#-------------------

# vaša koda tukaj

print("rezultat") # popravite, da bo izpis v formatu "Rezultat: {X} rad", kjer je {X} pretvorjena cifra.

```

### Linearna funkcija

Napištie program, ki za vhono spremenljivko X izračuna in izpiše vrednost Y.  
Program naj ima spremenljivki za faktor `k` ter prosti člen `n`  

```py
x = 2.5 # vhod v funkcijo
#-------------------

# vaša koda tukaj

print("rezultat") # popravite, da bo izpis v formatu "f(x)= {Y}", kjer je {Y} izračunana vrednost funkcije.
```

Če vam uspe, poskusite implementirati program, ki na podoben način računa poljuben polinom pete stopnje. `(a * x ** 5 + ... )`  
Koeficienti naj bodo nastavljive spremenljivke.

### Krog

Napištie program, ki sprejme polmer kroga `r` izpiše pa osnovne podtke o tem krogu:  

- premer
- obseg
- ploščina

```py
r = 2.5 # polmer
#-------------------

# vaša koda tukaj

print("rezultat") # popravite, da bo izpis v formatu "premer = {X}", kjer je {X} premer krogra.
print("rezultat") # popravite, ... obseg
print("rezultat") # popravite, ... ploščina
```

Za konstanto `PI` uporabite **3.14** ali pa približek **22/7**. Poskusite izračunati oboje in primerjajte rezultate.  

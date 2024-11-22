---
title: "GDScript"
description: "Osnove programiranja v Godotu"
pubDate: "Nov 22 2024"
heroImage: "/gdscript.png"
---

V tem poglavju bomo spoznali osnove programskega jezika GDScript.
Če si že kdaj programiral v Pythonu, ti bo ta jezik zelo znan, saj mu je GDScript zelo podoben.
Če pa še nisi programiral, pa ne skrbi, saj bomo začeli z osnovami.
To poglavje je prirejeno po [https://gdscript.com/](https://gdscript.com/) ter uradni dokumentaciji jezika [GDScript](https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/gdscript_basics.html).

## Sprermenljivke

Vsak programski jezik ima spremenljivke. Spremenljivke so kot škatle, v katere lahko shranimo podatke in do njih dostopamo kasneje.
V GDScriptu spremenljivke definiramo z ključno besedo `var`, kateri sledi ime spremenljivke in nato enačaj `=` ter vrednost, ki jo želimo shraniti v spremenljivko.

```gdscript
var score = 0
var remaining_fuel = 99.9
var paused = false
var player_name = "matej"
var selected_weapon
var starting_grid_position
```

Tukaj lahko vidimo 6 spremenljivk. Prve 4 so že `initializirane`, kar pomeni, da smo jim določili vrednost. Ostali dve pa sta `neinitializirani`, kar pomeni, da še nista dobili vrednosti in sta tako `null`.

## Tipi spremenljivk

Spremenljivke so lahko različnih `tipov`. V zgornjem primeru smo uporabili 4 različne tipe spremenljivk:
- `int` (celo število, 64bit)
- `float` (decimalno število)
- `bool` (logična vrednost, samo `true` ali `false`)
- `string` (tekst)

Poleg teh tipov obstaja še mnogo drugih, ki jih bomo spoznali kasneje.

V zgornjem primeru smo pustili, da Godot sam ugotovi tip spremenljivke. Takšnim spremenljivkam rečemo, da so `dinamične` in jim lahko tip poljubno spreminjamo.

```gdscript
var score = 0
score = "to je zdaj string"
```

V tem primeru je spremenljivka `score` najprej tipa `int`, nato pa smo ji dodelili vrednost tipa `string`.

Za hitro prototipiranje je to super, vendar pa je v večjih programih boljša praksa, da spremenljivkam sami določimo tip.
Tako se lahko izognemo napakam, ki bi se lahko pojavile zaradi napačnega tipa spremenljivke.
Spremenljivki lahko določimo tip na dva načina:

```gdscript
# Prvi način
var score: int = 0
var remaining_fuel: float = 99.9
var paused: bool = false
var player_name: string = "matej"

# Drugi način
var score := 0
var remaining_fuel := 99.9
var paused := false
var player_name := "matej"
```

Pri prvem načinu moramo sami določiti tip spremenljivke, pri drugem pa to naredi Godot sam.
Razlika se pojavi, če bi želeli spremenljivki dodeliti vrednost drugega tipa.

```gdscript
var score: int = 0
score = "to je zdaj string" # napaka

Parse Error: Cannot assign a value of type "String" as "int".
Parse Error: Value of type "String" cannot be assigned to a variable of type "int".
```

Godot nam bo vrnil napako s prijaznim sporočilom, s katerim si lahko pomagamo pri odpravljanju napake.
Priporočam, da poskušate vsaki spremenljivki določiti tip, saj se boste tako izognili marsikateri napaki.

## Operacije

Nad spremenljivkami lahko izvajamo različne operacije, kot naprimer matematično seštevanje, odštevanje, množenje in deljenje.

```gdscript
var a: int = 5
var b: int = 3

print(a + b) # 8
print(a - b) # 2
print(a * b) # 15
print(a / b) # 1 hmm, to je pa malce čudno
```

Pri nekaterih operacijah je tip spremenljivke pomemben. Če delimo dve celo števili, bo rezultat tudi celo število. Če želimo decimalni rezultat, moramo eno od števil spremeniti v decimalno.

```gdscript
var a: int = 5
var b: int = 3

print(a / b) # 1
print(a / float(b)) # 1.6666666666666667
```

Zelo pomembna operacija je tudi `modulo`, ki vrne ostanek pri deljenju dveh števil.

```gdscript
var a: int = 5
var b: int = 3

print(a % b) # 2
```

To operacijo si zapomnite, saj jo bomo kar redno uporabljali.

Pri programiranju so pomembne tudi `primerjalne operacije`, ki vrnejo logično vrednost `true` ali `false`.

```gdscript
var a: int = 5
var b: int = 3

print(a > b) # true
print(a < b) # false
print(a == b) # false
print(a != b) # true
```

Med spremenljivkami tipa `boolean` pa poznamo tri zelo pomembne logične operacije: `and`, `or` in `not`.

```gdscript
var a: bool = true
var b: bool = false

print(a and b) # false
print(a or b) # true
print(not a) # false
```

Te opracije sledijo sledečim praivilom:
- `and` vrne `true`, samo če sta oba izraza `true`
- `or` vrne `true`, če je vsaj en izraz `true`
- `not` vrne `true`, če je izraz `false`

## Pogojno izvajanje kode

V programiranju je zelo pomembno, da lahko izvajamo določen del kode samo, če je določen pogoj izpolnjen.
To naredimo s pomočjo `if` stavka.

```gdscript
var a: int = 5

if a > 3:
    print("a je večji od 3")
```

> Vedno ko v Godotu vidimo `:` na koncu vrstice, pomeni, da moramo naslednji blok kode zamakniti za en `tab`.

V tem primeru bo izpisano `a je večji od 3`, saj je pogoj `a > 3` resničen.
If stavek lahko tudi razširimo z `else` in `elif`.

```gdscript
var a: int = 5

if a > 3:
    print("a je večji od 3")
elif a == 3:
    print("a je enak 3")
else:
    print("a je manjši od 3")
```

V pogoju lahko uporabljmo tudi logične operacije.

```gdscript
var a: int = 5
var b: int = 3

if a > 3 and b < 5:
    print("a je večji od 3 in b je manjši od 5")
```

## Funkcije

Funkcije so zelo pomemben del programiranja, saj nam omogočajo, da določen del kode zapakiramo v funkcijo in jo kasneje uporabimo večkrat.
Funkcijo si lahko nekako predstavljamo kot sceno, narejeno iz nodov, ki jo lahko večkrat uporabimo v različnih scenah.
Fukcija <=> scena in vrstica kode <=> node.

Funkcijo definiramo z ključno besedo `func`, ki ji sledi ime funkcije in nato oklepaji in dvopičje `():`.
V naslednjih vrsticah sledi galvno telo funkcije, ki mora biti zamaknjeno!

```gdscript
func pozdravi():
    print("Hello, World!")

pozdravi() # Hello, World!
```

Funkcijam lahko podamo tudi argumente, ki jih uporabimo znotraj funkcije.

```gdscript
func pozdravi(ime: string):
    print("Hello, " + ime + "!")

pozdravi("matej") # Hello, matej!
```

Funkcije lahko tudi `vračajo` vrednosti.

```gdscript
func sestej(a: int, b: int) -> int:
    return a + b

var rezultat = sestej(5, 3)
print(rezultat) # 8
```

Vidimo, da lahko argumentom funkcije in njeni vrednosti določimo tip. To je zelo uporabno, saj se tako izognemo marsikateri napaki.
Kot primer si poglejmo naslednjo funkcijo.

```gdscript
func sestej(a, b):
    return a + b

sestej("5", 3) # napaka
```

Dobimo napako, ampak šele, ko program dejansko izvedemo. Če bi imeli določen tip argumentov, bi napako videli že med pisanjem kode.

```gdscript
func sestej(a: int, b: int) -> int:
    return a + b

sestej("5", 3)

Cannot pass a value of type "String" as "int".
Invalid argument for "sestej()" function: argument 1 should be "int" but is "String".
```

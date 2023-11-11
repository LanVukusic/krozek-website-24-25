---
title: 'Operacijski sistemi'
description: 'Osnovna razlaga operacijskih sistemov, ter uporaba terminala'
pubDate: 'nov 10 2023'
heroImage: '/blog-placeholder-1.jpg'
---

## Windows

Predvidevam, da vas večina uporablja operacijski sistem Windows, najverjetneje Windows 10 ali 11. Če želite, lahko tudi za potrebe krožka uporabljate Windows. Vse kar potrebujete je nameščen [Python](https://www.python.org/) in urejevalnik besedil:

- [IDLE](https://docs.python.org/3/library/idle.html) - urejevalnik besedil, ki je del Pythona
- [Notepad++](https://notepad-plus-plus.org/) - boljši kot privzet Windows Notepad
- [Visual Studio Code](https://code.visualstudio.com/) - najbolj pogosto uporabljen urejevalnik, uporabljali ga bomo na krožku
- [SublimeText](https://www.sublimetext.com/)
- in še mnogo drugih

## Linux

Med programerji pa je bolj priljubljena družina operacijskih sistemov Linux. Za potrebe krožka sva naredila 20 `bootable USB` ključkov z operacijskim sistemtom [Fedora Linux](https://fedoraproject.org/). Ti ključki imajo naloženo že vso potrebno programsko opremo, ki jo bomo potrebovali, in so tako rečeno `plug and play`.

### Kako zagnati Linux iz USB ključka?

Prvi program, ki se zažene, ko prižgemo računalnik je [UEFI](https://en.wikipedia.org/wiki/UEFI) (naslednjik [BIOS-a](https://en.wikipedia.org/wiki/BIOS)). UEFI je odgovoren za pripravo in zagon operacijskega sistema. Če imamo na disku samo en operacijski sistem, je to zelo enostavno.

Na disku pa imamo lahko tudi več različnih operacijskih sistemov. V tem primeru moramo UEFI-u povedati, kateri operacijski sistem naj zažene. V našem primeru imamo Windows na notranjem disku v računalniku, Fedora Linux pa na USB ključku. Zagona se lotimo tako:

1. Vstavimo USB ključek v računalnik (če je možno v USB 3.0 port)
2. Računalnik prižgemo in med zagonom pritisnemo eno izmed `F` tipk (običajno `F2`, `F8`, `F10`, `F12` ali `Del`, odvisno od proizvajalca računalnika - Google is your friend), da pridemo v `boot menu`
3. V `boot menu`-ju izberemo USB ključek in pritisnemo `Enter`
4. Računalnik bo zagnal Linux iz USB ključka
5. Prijavimo se v uporabnika `Krozek` z geslom `krozek123`

> USB ključka ne smemo odstraniti, dokler računalnika ne ugasnemo. V nasprotnem primeru lahko pride do poškodb datotek na ključku.

# Terminal

Terminal je program, ki nam omogoča, da z računalnikom komuniciramo preko ukazov. Na Windowsih imamo `Command Prompt` in `PowerShell`, na Linuxu pa `Terminal`. Vsi trije so si med seboj zelo podobni, vendar se vseeno razlikujejo. Tukaj bom opisal Linuxov `Terminal`.

Na Fedori lahko terminal odpremo na več načinov:

- z uporabo `Windows` tipke in iskanjem `Terminal`
- z uporabo bližnjice `Ctrl + Alt + T`
- z desnim klikom v določeni mapi in izbiro `Open in Terminal`

Odpre se nam črna koznola, ki je videti nekako takole:

```shell
krozek@DESKTOP:~$
```

Ta vrstica je sestavljena iz treh delov:

- `krozek` je ime uporabnika
- `DESKTOP` je ime računalnika
- `~` je trenutna mapa (`~` pomeni domača mapa uporabnika `/home/krozek`)

Na koncu vrstice je prostor za vnos ukazov.

## Podatkovni sistem v Linuxu

Vse datoteke v Linuxu se nahajajo v drevesni strukturi. Drevo je sestavljeno iz map in datotek. Vsaka mapa ima lahko v sebi datoteke in podmape. Vse datoteke in mape imajo svojo `absolutno pot` (ang. `aboslute path`), ki je sestavljena iz imen vseh map, ki se nahajajo nad njo, ločenih z `/`. Na primer, če imamo mapo `Desktop`, ki se nahaja v mapi `krozek`, ki se nahaja v mapi `home`, ki se nahaja v mapi `/`, je pot do mape `Desktop` enaka `/home/krozek/Desktop`, kjer je `/home/krozek` velikokrat zapisano kot `~`.

## Osnovni ukazi

Tukaj bom opisal nekaj osnovnih ukazov, ki jih bomo potrebovali tekom krožka. Vseh ukazov je seveda veliko več.

Kadar za ukaz vpisujemo pot do datoteke, lahko uporabimo `tabulator` (tipka `TAB`) za avtomatsko dopolnjevanje. Ob pritisku `TAB` nam konzola prikaže vse možne poti, ko je ta pot ena sama, pa jo kar avtomatsko dopolni v celoti.

### pwd

Ukaz `pwd` izpiše absolutno pot do trenutne mape

```shell
krozek@DESKTOP:~$ pwd
/home/krozek
krozek@DESKTOP:~$
```

### ls

Ukaz `ls` izpiše vse datoteke v trenutni mapi

```shell
krozek@DESKTOP:~$ ls
Desktop Documents Downloads Music Pictures Public Templates Videos
krozek@DESKTOP:~$
```

### cd

Ukaz `cd` se uporablja za premikanje med mapami. Če želimo priti v mapo `Desktop`, v terminal vpišemo:

```shell
krozek@DESKTOP:~$ cd Desktop
krozek@DESKTOP:~/Desktop$
```

> Tukaj smo uporabili `relativno` pot.

Vidimo, da se je naša trenutna mapa spremenila iz `~` v `~/Desktop`. Če želimo priti nazaj v domačo mapo, v terminal vpišemo:

```shell
krozek@DESKTOP:~/Desktop$ cd ..
krozek@DESKTOP:~$
```

`.` predstavlja trenutno mapo, `..` pa mapo, v kateri je trenutna mapa.

Če se želimo premakniti v mapo, ki ne obstaja, dobimo napako

```shell
krozek@DESKTOP:~$ cd test
bash: cd: test: No such file or directory
krozek@DESKTOP:~$
```

Ukaz `cd` deluje tudi na `absolutnih` poteh.

```shell
krozek@DESKTOP:~/test1/test2$ cd /home/krozek/Desktop
krozek@DESKTOP:~/Desktop$
```

Brez dodatnih parametrov nas `cd` vedno prestavi v domačo mapo

```shell
krozek@DESKTOP:~/test1/test2$ cd
krozek@DESKTOP:~$
```

### mkdir

Ukaz `mkdir` se uporablja za ustvarjanje map. Če želimo ustvariti mapo `test`, v terminal vpišemo:

```shell
krozek@DESKTOP:~$ mkdir test
krozek@DESKTOP:~$ mkdir test/test2
krozek@DESKTOP:~$
```

Sedaj nam ukaz `ls` izpiše tudi mapo `test`

```shell
krozek@DESKTOP:~$ ls
Desktop Documents Downloads Music Pictures Public Templates Videos test
krozek@DESKTOP:~$
```

Z `cd` pa se lahko premaknemo v novo mapo

```shell
krozek@DESKTOP:~$ cd test
krozek@DESKTOP:~/test$
```

### touch

Ukaz `touch` se uporablja za ustvarjanje datotek. Če želimo ustvariti datoteko `test.txt`, v terminal vpišemo:

```shell
krozek@DESKTOP:~/test$ touch test.txt
krozek@DESKTOP:~/test$
```

Sedaj nam ukaz `ls` izpiše tudi datoteko `test.txt`

```shell
krozek@DESKTOP:~/test$ ls
test.txt
krozek@DESKTOP:~/test$
```

### cp

Ukaz `cp` se uporablja za kopiranje datotek. Če želimo kopirati datoteko `test.txt` v datoteko `test2.txt`, v terminal vpišemo:

```shell
krozek@DESKTOP:~/test$ cp test.txt test2.txt
krozek@DESKTOP:~/test$
```

Sedaj nam ukaz `ls` izpiše tudi datoteko `test2.txt`

```shell
krozek@DESKTOP:~/test$ ls
test.txt test2.txt
krozek@DESKTOP:~/test$
```

### mv

Ukaz `mv` se uporablja za premikanje (preimenovanje) datotek. Če želimo premakniti in preimenovati datoteko `test2.txt` v `test2/test.txt`, v terminal vpišemo:

```shell
krozek@DESKTOP:~/test$ mv test2.txt test2/test.txt
krozek@DESKTOP:~/test$
```

Tukaj smo datoteko `test2.txt` **premaknili** v mapo `test2` in **preimenovali** v `test.txt`.

### rm

Ukaz `rm` se uporablja za brisanje datotek. Če želimo izbrisati datoteko `test.txt`, v terminal vpišemo:

```shell
krozek@DESKTOP:~/test$ rm test.txt
krozek@DESKTOP:~/test$
```

Sedaj nam ukaz `ls` ne izpiše več datoteke `test.txt`

```shell
krozek@DESKTOP:~/test$ ls
krozek@DESKTOP:~/test$
```

Če želimo izbrisati mapo, moramo ukazu `rm` dodati parameter `-r`

```shell
krozek@DESKTOP:~$ rm -r test
krozek@DESKTOP:~$
```

### python

Ukaz `python` se uporablja za zagon Python [REPL-a](https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop), ki nam omogoča interaktivno izvajanje Python kode. Na večini Linux distribucijah je Python že nameščen.

````shell

```shell
krozek@DESKTOP:~$ python
Python 3.12.0 (main, Oct 2 2023, 00:00:00) [GCC 13.2.1 20230918 (Red Hat 13.2.1-3)] on linux
Type "help", "copyright", "credits" or "license" for more information
>>>
````

> Za izhod iz REPL-a uporabimo `Ctrl + D` ali napišemo `exit()`

Če želimo pognati Python datoteko `test.py`, v terminal vpišemo:

```shell
krozek@DESKTOP:~$ python test.py
// Izpis programa
krozek@DESKTOP:~$
```

### code

Ukaz `code` se uporablja za odpiranje urejevalnika `Visual Studio Code`. Privzeto `Visual Studio Code` **ni** nameščen. Namestiti ga moramo sami. Na USB ključkih sva vam ga že namestila. Če želimo odpreti mapo `krozek`, v terminal vpišemo:

```shell
krozek@DESKTOP:~$ code krozek
krozek@DESKTOP:~$
```

Odpre se urejevalnik `Visual Studio Code` z vsebino mape krozek.

# Naloga

Ustvarite vse potrebne mape in datoteke, da ukaz `tree` izpiše naslednjo strukturo:

```shell
krozek@DESKTOP:~$ tree drevo
drevo
├── veja1
│   ├── jabolko
│   ├── list
│   └── vejica
│       └── listek
├── veja2
│   ├── list
│   └── list2
└── veja3
    ├── vejica1
    │   └── jabolko
    └── vejica2
        └── listek

7 directories, 7 files
```

#Podstawy

##Polecenia 05
-mkdir
- cd <nazwa>
- cd ...

##Instalacja Pythona

https;//www.python.org/

## Ogólnie o językach programowania

###Język Maszynowy 

### Assemblery 

mnemoniki - ADD 

### Języki wyższego poziomu

- komplilowane - kod źródłowy jest komplilowany

- interpretowane

- JIT - just in Time 

###przydatne funkcje na początku 
- help 
- dir

help () - interaktywna pomoc
help(1) 
help (print) -dokumentacja obiektu

dir() - wyświetlenie nazw  z bieżącej przestrzeni, zasięgu (scope)

dir("napis")  - zwraca listę atrybutów i metod danego obiektu

### podstawowe typy

int - intiger, liczny całkowite 

operacje +, -, /, *, 
// (zwraca część całkowitą dzielenia), 
% (modulo)
**  - potęgowanie
 pow - 

0b11- liczba przedstawiona binarnie 
np. ob11010100 --> 212
0o - system ósemkowy np. 0o11 --> 9
0x- system szesnastkowy np. 0x11 --> 17
 
int zamienia nam liczby przecinkowe, napisy na liczby 

### bool 
False 
True
 wartośći logiczne

and, or, not operatory logiczne

or - wystarczy ze jedna wartość jest prawdziwa 
not - odwrócenie not true = false 
and - tylko jak true and true jest true 

1+ True 
2

bool () - zamienia nam na typ bool każda liczba jest True, 0 jest zawsze False
 napisy tez są True, pusty napis False, listy puste też False, wszystko co jest puste jest zamieniane na False

operatory porównania  
<
>
<=
>=
==
!=

###float

liczba zniennoprzecinkowa

separatorem dziesiętnym jest kropka 

### complex - liczby zezpolone 

### str - string - napis 

>>> f'{"ogórek":30}{1.5:4.3f}'
'ogórek                        1.500'

sposób na formatowanie 

###zmienne (i STAŁE)

nazwy składają się z liter, cyfr i znaku podkreślenia
Mozemy używac polskie znaki - ale lepiej tego nie robić
najlepiej pisać kod po ang

źle - niezgodnie z konwencją:

somevariable
someVariable
SomeVariable

dobrze:
some_variable

PEP8
https:// peps.python.org/pep-008/














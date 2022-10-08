#napisz program, kóry pobierze od użytkownika
# rok urodzenia i wypisze czy użytkownik jest
# pełnoletni czy nie

bieżący_rok = 2022
x = int(input('Podaj rok urodzenia: '))

if bieżący_rok - x >= 18:
    print ("pełnoletni")
else:
    print ("niepełnoletni")
    
    
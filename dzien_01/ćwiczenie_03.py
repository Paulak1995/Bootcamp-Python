#Napisz program, któy obliczy koszty przejazdu z A do B

'''
Miasta A: Warszawa
M3iasto B: Gdańsk
Dystans Warszawa - Gdańsk: 420
Cena paliwa: 7.25
Spalanie na 100 km : 10
'''


#Koszt przejazdu Warszawa- Gdańsk to 404.50 PLN

Miasto_A = input("Wpisz nazwę miasta z którego ruszasz: ")
Miasto_B = input("Wpisz nazwę miasta do którego jedziesz: ")
Dystans = float(input("jaka jest odległość między {Miasto_A}-{Miasto_B}"))
cena_paliwa = float(input("podaj cenę paliwa: "))
spalanie = float(input("podaj spalanie na 100 km: "))

koszt= Dystans*cena_paliwa/spalanie

# (f:"Koszt przejazdu z Miasto_A do Miasto_B wynosi:"  (spalanie * Dystans)/100*cena_paliwa)

print (f'koszt podróży z {Miasto_A} do {Miasto_B} wynosi {koszt:.2f}')
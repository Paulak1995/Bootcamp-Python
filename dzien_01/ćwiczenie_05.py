# zadanie kalkulator
'''
Podaj pierwszą liczbę: 10
POdaj drugą liczbę: 20
Podaj rodzaj operacji: +

Wynik: 30
'''
x = int(input('Podaj pierwszą liczbę: '))
y = int(input ('Podaj drugą liczbę: '))
z = input('podaj rodzaj operacji: ')


if z == "+":
    result = x + y
elif z == "-":
    result = x - y
elif z == "*":
    result = x * y
elif z == "/":
    if y== 0:
        result = ("Pamiętaj nie dziel przez zero")
    else:
        result = (x/y)
    if z == "**":
        result = x ** y
else:
    result = ('błąd')
    
print (f'wynik to: {result}')
   
    

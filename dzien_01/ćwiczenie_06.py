x = int (input('Podaj pierwszą liczbę'))
y = int (input ('Podaj drugą liczbę'))

if 0< x < 10 and 0< y < 10:
    result = "lewy dolny róg"
elif 10 < x < 90 and 10 < y < 90:
    result = "lewy krawędź"
elif 90<= x >= 100 and 90<= y >= 100:
    result = "lewy górny kraniec"
elif 10 < x <90 and 0 < y < 90:
    result = "dolny krawędź"
elif 90 <= x <= 100 and 0 < y < 90:
    result = "dolny lewy róg"
elif 10 < x < 90 and 10 < y < 90:
    result = "centrum"
elif 90 < x < 100 and 10 < y < 90:
       result = "prawy krawędź"
elif 90 < x < 100 and 90<= y <= 100:
    result = "górny prawy róg"
elif 10 < x <90 and 90 < y <100:
    result = "górna krawędź"
elif x>100 or x< 0 or y >100 or y < 0:
    result = "jesteś poza planszą"
    
print(f'wynik to: {result}')
###Program do obliczania 
#współczynnika BMI

wzrost = int(input ("Podaj wzrost w cm:"))/100
waga = int(input("Podaj wagę w kg: "))

BMI = waga/ wzrost **2

print ("Twój współczynnik BMI wynosi, {BMI:.2f}")


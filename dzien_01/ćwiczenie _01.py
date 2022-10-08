produkt_1= "pomidory"
waga_1 = 3.4 
cena_01 = 5.55 

produkt_2= "ogórki"
waga_2 = 1.2
cena_02= 3.56 

produkt_3="marchewka"
waga_3 = 2.45
cena_03 = 4.5


suma = cena_01 +cena_02 + cena_03

raport = f"""
{produkt_1:30}{waga_1:5.2f} kg {cena_01:5.2f} PLN
{produkt_2:30}{waga_2:5.2f} kg {cena_02:5.2f} PLN
{produkt_3:30}{waga_3:5.2f} kg {cena_03:5.2f} PLN
{"-"*50}
{"suma":30}:{"":8} {suma:5.2f} PLN


"""
print(raport)
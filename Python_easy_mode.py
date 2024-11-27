from statistics import mean
from math import pi
from random import randint as rd
from ipaddress import summarize_address_range
from math import * #pi laabimoot
 # ümbernimetus
print("Hello world") #Конечное действие для задачи 
#intput("Hello world") #Сохраняет введеные данные 
nimi = input("Sisestage nimi ").capitalize #lover()-aaa, upper()-AAA, capitalize()-Aaa
print("Tere tulemast",nimi)
print("tere tulemast "+nimi)
vanus=int(input("Kui vana sa oled? "))
print("Tere tulemast! Tervitan sind " +nimi+ "sa oled",vanus,"aastat vana")
print(f"Tere tulemast! Tervitan sind {nimi} Sa olde {vanus} aastat vana")

# Ülesanne 2
vanus = 18
eesnimi = "Jaak"
pikkus = 16.5
kas_käib_koolis = True
print(type(vanus))
print(type(pikkus))
print(type(kas_käib_koolis))
if kas_käib_koolis is True:
    print("Käib kooli")

# Ülesanne 3
kokku = rd(1, 1000)
print (f"Kokku on {kokku} kommi")
kommi = int(input("Mitu kommi sa tahad? "))
kokku=kokku-kommi
print(f"Teil on jäänud {kokku} kommid")

# Ülesanne4
print("Läbimõõdu leidmide ")
l - ümbermõõt
l = float(input("Ümbermõõt "))
d = l/pi
print(f"Teie läbimõõdu suurus {round(d,2)} sm")
# If u are reading what think, that means that I still puck upt

# Ülesanne5 
print("Diagonaali otsimine")
N = float(input("Sissestage suurus N meetrites "))
M = float(input("Sisestage suurus M meetrites "))
d = sqrt(M**2+N**2)
print(f"Teie diagonaali pikkus on {round(d,3)}m")

# Ülesanne6
time = float(input("Сколько часов вам потребовалось, чтобы ехать? ")) 
distance = float(input("Сколько километров вы проехали? ")) 
speed = distance / time 

print("Ваша скорость была " + str (speed) + "«км/ч»")

# Ülesanne7
nun = input("Sisestage 5 tühikuga eraldatxud numbrit ").split()
oige = list(map(int, nun))
print(f"Keskmine arifmeetiline on {sum(oige)/5}")

# Ülesanne8
text = '''    @..@
   (----)
  ( \__/ )
  ^^ "" ^^  '''
print(text)
print("  @..@")
print(" (----)")
print("( \__/ )")
lalala = str("^^ "" ^^")
print(f"^^ {lalala} ^^")

# Ülesanne9
print("Kolmnurga ümbermõõdu otsimine")
a = float(input("sisestage number a "))
b = float(input("sisestage number b "))
c = float(input("sisestage number c "))
raschet = a + b + c
print(f"P võrdub {raschet}")

# Ülesanne10
summa = 12.9
jootraha = float(summa / 100 * 10)
ty = float(summa / 2)
print(f"Teie sõber maksate {summa/2} € ja Te maksate {sum(ty+jootraha)}€")

# print("Pitsa maksmine arvutamine")
# algus = int(input("Sisestage, kui palju teid oli? "))
# suma = float(input("Sisestage, kui palju te maksite pitsa kohta? "))
# vastus = input("Kas Te soovite jääta jootraha? (Jah/Ei) ")
# print(f"Teie sõber jäätab {suma/2}€ ja te jäätate {sum(suma/100 * 10)}")
# if vastus.upper() == 'Jah':
#     pol = int(input("Kui palju protsentid te soovite jääda? "))
#     joot = suma / 100 * pol
#     print(f"Teised inimesed jäätavad {suma/algus}€ ja te jääte {joot}") # Я 5 минут убил, чтобы понять что проблема была в отсутствие табуляции
# if vastus.upper() == 'Ei':
#     print("AAAA")
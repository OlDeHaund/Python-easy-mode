from datetime import *
from calendar import *
from random import *
from math import *
# # Ülesanne1
# täna = date.today()
# tänaf = date.today().strftime("%B, %d, %Y")
# # print(f"Täna on {tänaf}")

# d=täna.day             #nimetus - omadus
# a=täna.month
# y=täna.year
# print (d)
# print (a)
# print (y)
# monthend = int(30-d)
# yearend = int(12-y)
# print(f"Enne kuu lõppuni on jaanud {monthend} päevad" )

#Ülesanne2
a = 3+8/(4-2)*2
b = 3+8/4-2*2
c = (3+8)/(4-2)*2
print( a,"\n",b,"\n",c)

#Ülesanne3
try:
    R=float(input("Sissesta R: "))
    Sk = pi * R**2
    Pk = 2 * (pi*R)
    Skv = (2*R)**2
    Dkv = 2*R*4
    print(f"Ruudu pindala on {Sk}\nRingi ümbermõõt on {Pk}sm\nRuudu pindala S on {Skv}sm\nRingi Ruudu ümbermõõt {Dkv}sm")
except:

#Через рандом
r = round(Random()*100) #0.0 - 1.0
Sk = pi * r**2
Pk = 2 * (pi*r)
Skv = (2*r)**2
Dkv = 2*r*4
print(f"Ruudu pindala on {Sk}\nRingi ümbermõõt on {Pk}sm\nRuudu pindala S on {Skv}sm\nRingi Ruudu ümbermõõt {Dkv}sm")

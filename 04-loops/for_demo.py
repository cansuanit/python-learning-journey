
"""
sayilar = [1,3,5,7,9,12,19,21]

1- Sayılar listesindeki hangi sayılar 3'ün katıdır?
2- Sayılar listesindeki sayıların toplamı kaçtır?
3- Sayılar listesindeki tek sayıların karesini alınız.
"""

sayilar = [1,3,5,7,9,12,19,21]

print(sayilar)

print("sayılar listesindeki 3'ün katı olan sayılar:")
for sayi in sayilar:
    if (sayi%3==0):
        print (sayi)
#toplam değişkeni for döngüsüne girmeden tanımlanır
toplam = 0
print("sayılar listesindeki sayıların toplamı = ")
for num in sayilar:
    toplam = num +toplam

print(toplam)

print("sayılar listesindeki tek sayıların karesi ")

for tek in sayilar:
    if (tek%2 != 0):
        karesi = tek**2
        print(karesi)

"""
sehirler = ["Kocaeli","İstanbul","Ankara","İzmir","Rize"]

4- Şehirlerden hangileri en fazla 5 krakterlidir?

"""
sehirler = ["Kocaeli","İstanbul","Ankara","İzmir","Rize"]
print(f"ŞEHİRLER: {sehirler}")
print("Yukarıdaki şehirlerden hangileri en fazla 5 karakterlidir?")
for city in sehirler:
    if (len(city)<=5):
     print(city)

"""
urunler = [
    {"name": "samsung s6", "price": "3000"}
    {"name": "samsung s7", "price": "4000"}
    {"name": "samsung s8", "price": "5000"}
    {"name": "samsung s9", "price": "6000"}
    {"name": "samsung s10", "price": "7000"}
]
5- Ürünlerin fiyatları toplamı nedir?
6- Ürünlerin fiyatları en fazla 5000 olan ürünleri gösteriniz.
"""
urunler = [
    {"name": "samsung s6", "price": "3000"},
    {"name": "samsung s7", "price": "4000"},
    {"name": "samsung s8", "price": "5000"},
    {"name": "samsung s9", "price": "6000"},
    {"name": "samsung s10", "price": "7000"}
]
toplamfiyat= 0
for urun in urunler:
  toplamfiyat += int(urun["price"])
print(f"Ürünlerin toplam fiyatı : {toplamfiyat}")
print("Ürünlerden fiyatı en fazla 5000 olan ürünlerin listesi: ")
for urun in urunler:
   if (int(urun["price"])<= 5000):
    print(urun)
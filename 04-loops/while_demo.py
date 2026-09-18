"""
while örnekleri
"""
# sayilar = [1,3,5,7,9,12,19,21]
# 1- sayilar listesini while ile ekrana yazdırın.

sayilar = [1,3,5,7,9,12,19,21]

i = 0

while (i < len(sayilar)):
    print(sayilar[i], end = " ")
    i +=1
# end = " " ile tüm listeyi örnekteki gibi yan yana yazdırabiliyoruz.
# 2- Başlangıç ve bitiş değerlerini kullanıcıdan alıp 
# aradaki tüm tek sayıları ekrana yazdırın.

print("")
baslangic = int(input("bir başlangıç değeri girin : "))
bitis = int(input("Bir bitiş değeri girin : "))

n= baslangic
while (n < bitis):
    n+=1
    if (n%2 == 1):
     print(n, end = " ")
#if bloğu yazdığımızda else yazmak zorunda değiliz

# 3- (1-100) arasındaki sayıları azalan şekilde yazdırın.
print("\n 1-100 arasındaki sayılar azalan şekilde:")
num = 100
while (num>0):
   print(num, end = " ")
   num -=1

# 4-Kullanıcıdan alacağını 5 sayıyı ekranda sıralı bir şekilde yazdırın

numbers = []

x = 0
while(x<5):
   sayi = int(input("sayi :"))
   numbers.append(sayi)
   x +=1
numbers.sort()
print(numbers)

# 5- kullanıcıdan alacağınız sınırsız ürün bilgisini 
# urunler listesi içinde sakla
# ** ürün sayısını kullanıcıya sorun
# ** dictionary listesi yapısı (name, price) şeklinde olsun
# ** ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin

urunler = []

urun = input("urun : ")
urunsayisi = int(input("urun sayisi : "))
c= 0 
while(c<urunsayisi):
   name= input("ürün ismi :")
   fiyat = float (input("ürün fiyatı : "))
   urunler.append({
      "name" : name,
      "fiyat" : fiyat
   }
      
   )
   c +=1

   for urun in urunler:
      print(f"ürün adı : {urun['name']}  ürün fiyatı : {urun['fiyat']}")

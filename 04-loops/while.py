# 1-100 e kadar olan çift  sayıları ekrana yazdır
#while de belli bir koşul belirtiyoruz ne zaman koşul false düşerse o zaman çıkar whiledan
x= 0

while (x<=100):
    if(x%2 == 0):
     print(f"sayı çift : {x}")
    else:
       print(f"sayı tek : {x}")
    x += 1
# x += 1 while döngüsüne ait bir arttırma olacak 
print("bitti")

# Kullanıcıdan name bilgisi iste 

name= "" # false
#not name false olan durumların hepsini işlet demek burada name içine bir değer girmezsek
#enter karakterine basarsa isminizi girin yazısı ekranda çıkmaya devam eder
while not name.strip() :
   name = input("isminizi giriniz :  ")
print ("merhaba")
# ancak kullanıcı boşluk karakterine basıp daha sonra enter tuşuna basarsa o zaman boşluk bir string gibi algılanır
#ve tekrar merhaba der burada bu durumu engellemek için strip methodunu kullanamız lazım 
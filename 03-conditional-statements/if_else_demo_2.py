"""
1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.
sayi = float(input("sayı: "))
print(f"sayı 0-100 arasında mı ? : {result}")
"""
sayi = float (input("Bir sayı girin : "))
print("Girilen sayı 0-100 arasında bir değer mi ?")
if (0<= sayi <= 100):
    print("Evet")
else:
    print("Hayır")

"""
2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.

"""

sayi2= float(input("Bir sayı girin :"))

if (sayi2 > 0):
    if(sayi2%2 == 0):
        print("Girdiğiniz sayı pozitif bir çift sayıdır.")
    else:
        print("Girdiğiniz sayı pozitif bir tek sayıdır")
else:
    if(sayi2%2 == 0):
        print("Girdiğiniz sayı negatif bir çift sayıdır.")
    else:
        print("Girdiğiniz sayı negatif bir tek sayıdır.")

"""
3- Email ve parola bilgileri ile giriş kontrolü yapınız.
email = "can@look.com"
password = "abc123"

user_email = input("email : ")
user_password = input ("password : ")

"""

email = "can@look.com"
password = "abc123"

user_email = input("email : ")
user_password =  input("password : ")

if (email == user_email):
    if(password == user_password):
        print("Giriş başarılı.")
    else:
        print("Password hatalı.")
else:
    print("email hatalı")

"""
4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.

"""

a= int(input("a: "))
b= int(input("b: "))
c= int(input("c: "))

if (a> b and a>c):
    if (b>c):
        print ("a>b>c")
    elif (b<c):
        print("a>c>b")
    else:
        print("a> b=c")

elif (b>a and b>c):
    if (a>c):
        print ("b>a>c")
    elif (c>a):
        print("b>c>a")
    else:
        print("b>c=a")
elif (c>a and c>b):
    if(a>b):
        print("c>a>b")
    elif (b>a):
        print("c>b>a ")
    else:
        print("c>a=b")
elif (a==b):
    if(a>c):
        print("a=b>c")
    elif(c>a):
        print("c>a =b")
    else:
        print("a=b=c")
elif (a==c):
    if(a>b):
        print("a=b>c")
    elif(b>a):
        print("b>a =c")
    else:
        print("a=b=c")
elif (c==b):
    if(c>a):
        print("c=b>a")
    elif(a>c):
        print("a>c =b")
    else:
        print("a=b=c")
else:
    print("hatalı bir şey girdiniz")

"""
5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
Eğer ortalama 50 ve üzerindeyse geçti değilse kaldı yazdırın
"""
vize1 = float(input("Birinci vize notunu girin : "))
vize2 = float(input("İkinci vize notunu girin : "))
final = float(input("Final notunu girin : "))

ortalama = (((vize1+vize2)/2)*0.6)+(final*0.4)

if ortalama >= 50 :
    print(f"Ortalamanız {ortalama} geçtiniz.")
else:
    print(f"Ortalamanız {ortalama} kaldınız.")

#a) Ortalama 50 olsa bile final notu en azz 50 olmalıdır


if (final >= 50 and ortalama>= 50):
    print("Fİnal notunuz va ortalamanız 50 barajını geçti. GEÇTİNİZ.")
else:
    print("Final notunuz veya ortalamanız 50 barajının altında. KALDINIZ.")

#b)Finalden 70 alındığında ortalamanın önemi olmasın

if (final >= 70):
    print("Final notunuz en az 70 üzeri olduğu için GEÇTİNİZ.")
else:
    if (ortalama >= 50):
        print(f"Ortalamanız: {ortalama} GEÇTİNİZ.")
    else:
        print("KALDINIZ.")
"""
6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
formül: (Kilo/ boy uzunluğunun karesi)
Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
0-18.4 >= zayıf
18.5-24.9 >= normal
25- 29.9 >= fazla kilolu
30- 34.9>= obez
"""

name = input("Adınız : ")
kilo = float (input("Kilonuz kg cinsinden girin : "))
boy = float (input("Boyunuzu cm cinsinden girin: "))

indeks = kilo / ((boy/100)**2)

if (0<= indeks <= 18.4):
    print(f"Beden kitle indeksiniz : {indeks} : ZAYIF")
elif (18.5<= indeks<= 24.9):
    print(f"Beden kitle indeksiniz : {indeks} : NORMAL")
elif (25 <= indeks <= 29.9):
    print(f"Beden kitle indeksiniz : {indeks} : FAZLA KİLOLU")
elif (30 <= indeks <= 34.9):
    print(f"Beden kitle indeksiniz : {indeks} : OBEZ")
else:
    print("hatalı bir değer girdiniz")
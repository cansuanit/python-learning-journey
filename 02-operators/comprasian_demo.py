#1- girilen iki sayıdan hangisi büyüktür?
x= int(input("sayı 1:"))
y= int(input("sayı 2: "))
result = (x>y)
print(f"x:{x} y:{y} den büyüktür eğer sonuç true çıkarsa false çıkarsa küçüktür : {result}")

#2- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayın

a = float(input("1. vize notu : "))
b = float(input("2. vize notu : "))
c = float(input("final notu : "))

ortalama = (((a+b)/2)*0.60) + (c*0.40)

print(ortalama>=50, "Geçti")


#3-Girilen bir sayının tek mi çift mi olduğunu yazdırın

z = int(input("Bir sayı girin: "))
tekcift = (z %2 == 0)
print(tekcift)

#4- Girilen bir sayının negatif pozitif durumunu yazınız

num = int(input("Bir sayı girin: "))
print("Girdiğiniz sayı sıfırsan büyükse true sonucu", num > 0)

#5- Parola ve email bilgisi isteyip doğruluğunu kontrol ediniz.
#email : cansuanit@out.com parola : 123456

username = input("e mail : ")
password = input("password : ")

email = "cansuanit@out.com"
passw = "123456"

isEmail = (username == email.lower().strip())
#strip() metodu ile boşluk karakterleri temizleniyor

isPassword = (password == passw.lower())

print(f"Email bilgisi doğru mu ? :{isEmail}")
print(f"Parola doğru mu?: {isPassword}" )
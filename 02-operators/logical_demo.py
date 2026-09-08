# 1- Girilemn bir sayının 0-100 arasında olup olmadığını kontrol ediniz.
x = int(input("Bir tam sayı giriniz: "))
result1 = (x>0) and (x<100)
print(f"Girilen sayı 0 ve 100 arasında mı ?{result1}")

#2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.

y= int(input("Bir tam sayı giriniz: "))
result2 = (y>0) and (y%2 ==0)
print(f"Girilen sayı pozitif bir çift sayı mı ? {result2}")

#3- Email ve parola bilgileri ile giriş kontrolü yapınız.
email = "cansu@cloud.com"
password= "123456"

useremail = input("Email girin : ")
userpassword = input("Password girin : ")

result3 = (email == useremail) and (password == userpassword)
print(f"Uygulamaya giriş başarılı mı ? {result3}")

#4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.

sayi1= int(input("1. sayıyı girin: "))
sayi2= int(input("2. sayıyı girin: "))
sayi3= int(input("3. sayıyı girin: "))
result4a = (sayi1 > sayi2) and (sayi1> sayi3)
result4b = (sayi2>sayi3) and (sayi2> sayi1)
result4c = (sayi3>sayi1) and (sayi3> sayi2)

print(f"1. sayı en büyük sayı mı? {result4a}")
print(f"2. sayı en büyük sayı mı? {result4b}")
print(f"3. sayı en büyük sayı mı? {result4c}")

#5- Kullanıcıdam 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
vize1 = float(input("1. vize notunu giriniz : "))
vize2 = float(input("2. vize notunu giriniz : "))
final = float(input("Final notunu giriniz: ")) 

ort = (((vize1+vize2)/2)*0.6)+ (final*0.4)
print(f"Yıl sonu ortalaması : {ort}")

#   Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırınız.
result5 = (ort >= 50)
print("Geçti") == (result5 == True)
print("Kaldı") == (result5 == False)
#   a-) Ortalama 50 olsa bile final notu en az 50 olmalıdır
result5a = (ort >= 50) and (final >= 50)
print(f"Öğrencinin ortalaması : {ort} Dersten geçti mi ? {result5a}")
#   b-) Finalde 70 alındığında ortalamanın önemi olmasın
result5b= (final>=70) or (ort>=50)
print(f"Dersten geçti mi ? {result5b}")

#6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerin hesaplayınız.
#formül = (kilo/ boy uzunluğunun karesi)
# 0-18.4 => zayıf
# 18.5-24.9 => normal
# 25- 29.9 => fazla kilolu
# 30-34,9 => şişman (obez)

ad = input("Adinizi giriniz: ")
kilo = float(input("Kilonuzu giriniz : "))
boy = float(input("Boyunuzu metre cinsinden giriniz : "))

result6 = (kilo)/(boy**2)
zayif = (result6>=0) and (result6<= 18.4)
normal = (result6>=18.5) and (result6<= 24.9)
kilolu = (result6>=25) and (result6<= 29.9)
obez = (result6>=30) and (result6<= 34.9)


print(f"{ad} Beden kitle indeksiniz : {result6}. zayıf mı ? {zayif}")
print(f"{ad} Beden kitle indeksiniz : {result6}. normal mi ? {normal}")
print(f"{ad} Beden kitle indeksiniz : {result6}.  kilolu mu ? {kilolu}")
print(f"{ad} Beden kitle indeksiniz : {result6}. obez mi ? {obez}")





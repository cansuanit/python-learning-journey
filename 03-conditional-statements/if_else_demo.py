# 1- Kullanıcıdam isim, yaş ve eğitim bilgilerini isteyip alabilme
#durumunu kontrol ediniz. Ehliyet alma koşulu en az 18 ve eğitim durumu lise ya da üniversite olmalıdır.
username = input("Adınızı girin : ")
userage = int(input("Yaşınızı girin : "))
usereducation = input("Eğitim durumunuzu girin: ")

if (userage >= 18) :
 if (usereducation == "lise" or usereducation == "üniversite" ):
  print(f"{username} Ehliyet alabilirsiniz.")
 else:
  print(f"{username} Ehliyet alamazsınız eğitim durumunuz yetersiz.")
else:
  print(f"{username} Ehliyet alamazsınız yaşınız tutmuyor.")


#2- Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplayan ortalamaya göre
#not aralıına karşılık gelen not bilgisini yazınız.
# 0-24 => 0
# 25-44=> 1
# 45-54=>2
# 55-69=>3
# 70-84=>4
# 85-100=>5

yazili1= float(input("Birinci yazılı notunu girin :"))
yazili2= float(input("İkinci yazılı notunuzu girin:"))

ort = float((yazili1+yazili2)/2)

if(0<= ort) and (ort <= 24):
 print(f"ortalamanız {ort} notunuz 0.")
elif (24 <= ort) and (ort <= 44):
 print(f"ortalamanız {ort}  1.")
elif (45 <= ort) and (ort <= 54):
 print(f"ortalamanız {ort} notunuz 2.")
elif (55<= ort) and (ort <= 69):
 print(f"ortalamanız {ort} notunuz 3. ")
elif (70 <= ort) and (ort <=84):
 print(f"ortalamanız {ort} notunuz 4.")
elif (85 <= ort) and (ort <=100):
 print(f"ortalamanız {ort} notunuz 5.") 
else:
 print("Yanlış bir bilgi girdiniz.")

#3- Trafiğe çıkış tarihi alınan bir aracın servis zamanını
# aşağıdaki bilgilere göre hesaplayınız
# 1. bakım : 1.yıl
# 2. bakım : 2. yıl
# 3. bakım : 3.yıl
#  ** Süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı hesaplayınız:
#  ** datetime modülünü kullanmanız gerekiyor

from datetime import datetime

userdate =  input("Arcanızın trafiğe ilk çıkış tarifini girin (GG/AA/YYYY): ")
userdate = datetime.strptime(userdate, "%d/%m/%Y")
#print(userdate[0])
#print(userdate[1])
#print(userdate[2])

now_date = datetime.now()
print(now_date)

days = now_date- userdate
control = int(days.days / 365)
# aradaki günü bulmak için kullanıcıdan aldığımız veriyi datetime objesine çevirmemiz lazım
if control == 1:
  print(f"Aracınız {days.days} gündür trafikte 1. bakım ")
elif control == 2:
 print(f"Aracınız {days.days} gündür trafikte 2. bakım ")
elif control == 3:
 print(f"Aracınız {days.days} gündür trafikte 3. bakım ")
else:
 print("hatalı bir değer girdiniz")


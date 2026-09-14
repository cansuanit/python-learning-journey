from datetime import datetime
#datetime modülünden (fromdan sonra yazan), datetime sınıfını (importtan sonra gelen) getir
#import datetime
#datetime modülünü kullanmak için modülün adını dosyaya import ettik

#datetime. datetime
#ikinci datetime modülün adı ile aynı olsa da sınıfın adı
#now() -> şuanki tarihi ve saati veren metot

now = datetime.now()
#yukarıdaki kodu çalıştırdığımızda datetime modülüne git datetime sınıfını bul, now() metodunu çalıştır 
#ve sonucu now değişkenine koy demek

print(now)

#bu nesnenin parçalarına ulaşabiliriz.
print (now.year)
print (now.month)
print(now.day)
print(now.hour)
print(now.minute)

#elimizde iki tarih var
#başlangıç : 15 ağustos 2026
#bitiş : 11 eylül 2026
#bu iki tarih arasında kaç gün var?


start_date = datetime(2026,8,15)
#start_date değişkenine datetime nesnesi aktarıldı
end_date = datetime(2026,9,11)
#end_date değişkenine datetime nesnesi aktarıldı
difference = end_date - start_date
#difference timedelta nesnesi yani bir zaman aralığını/süreyi temsil eden sınıf
print(type(start_date))
print(type(end_date))
print(difference)
print(difference.days)


#2- Kullanıcıdan aldığımız doum tarihi ile şuan kullanıcının kaç yaşında olduğunu
#hesaplayalım.
user_birthday = input("Enter your birthday : ")
print(type(user_birthday))
#burada user_birthday string dolayısıyla bunu datetime nesnesine dönüştürmemiz lazım
#bunun için strptime() kullanılır. 
user_birthday = datetime.strptime(user_birthday, "%d/%m/%Y")
print(user_birthday)

nowtime = datetime.now()
print(nowtime)

yashesabi = nowtime - user_birthday
yashesabi = int(yashesabi.days/365)
print(f"{yashesabi}  yaşındasınız")
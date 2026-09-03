names= ["Ali","Yağmur","Hakan","Deniz"]
years= [1998,2000,1998,1987]
# 1- "Cenk" ismini listenin sonuna ekleyiniz.

names.append("Cenk")
print(names)

#2-"Sena" değerini listenin başına ekleyiniz
names.insert(0,"Sena")
print(names)

#3-"Deniz" ismini listeden siliniz.
names.remove("Deniz")
print(names)

#4-"Cenk" isminin indeksi kaçtır?

print(names.index("Cenk"))

#5-"Ali" ismi bir eleman mıdır?
find = "Ali" in names
print(find)

#6-Liste elemanlarını ters çevirin
names.reverse()
print(names)

#7- Liste elemanlarını alfabetik olarak sıralayınız
names.sort()
print(names)

#8- years listesindeki rakamsal büyüklüğe göre sıralayınız
years.sort()
print(years)

#9- str ="Chevrolet, Dacia" karakter dizisini listeye çeviriniz

str ="Chevrolet, Dacia"
#str_list= [str] 
#print(str_list)

result= str.split(",")
print(result)

#10- years dizisinin en büyük ve en küçük elemanı nedir?
#method1
years.sort()
print(years)
print(years[0], years[-1])
#method2
min = min(years)
max= max(years)
print(min,max)

#11- years dizisinde kaç tane 1998 değeri vardır?
print(years.count(1998))

#12-years dizisinin  tüm elemanlarını silin
years.clear()
print(years)

#13- kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.

markalar= []
marka= input("marka: ")
markalar.append(marka)
marka= input("marka: ")
markalar.append(marka)
marka= input("marka: ")
markalar.append(marka)
print(markalar)
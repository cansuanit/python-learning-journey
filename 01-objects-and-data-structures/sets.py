fruits = {"orange", "apple","banana"}
print(fruits)

# print(fruits[0]) indekslenemez. Tüm listeyi yazdırabiliriz ama indeks yazıp içindeki elemanlara ulaşamayız
# elemanlarına ulaşmak için döngü kullanmamız gerekir.
for x in fruits:
    print (x)

fruits.add("cherry")

print(fruits)

#birden fazla eleman eklemek istediğimizde update metodunu kullanabiliriz. köşeli parantez içinde yazmamız gerekir

fruits.update(["mango","grape"])
#zaten liste içinde var olan bir elemanı listeye eklediğimizde bize ekstra bir şey göstermez.liste üzerine eklenmez
fruits.add("apple") 
print(fruits)

myList = [1,2,3,2,1,6,5,6]
print (myList)
#set haline getirirsek tekrarlayan elemanlar silinir
print(set(myList))

#silme işlemi 
fruits.remove("mango")
print(fruits)
fruits.discard("apple")
print(fruits)
#pop ile herhangi bir eleman silinebilir
fruits.pop()
print(fruits)
# clear tüm elemanları siler
fruits.clear()

print(fruits)
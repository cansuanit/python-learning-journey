numbers = [1,10,5,16,4,9,10]
letters=["a","g","s","b","y","a","s"]

val = min(numbers)
print(val)

val =  max(numbers)
print(val)

val= max(letters)
print(val)

val= min(letters)
print(val)

val= numbers[3:6]
print(val)

val = numbers[:3]
print(val)

val = numbers[4:]
print(val)

numbers[4]= 40
print(numbers)

#append ile ekleme yapabiliriz. string pşaak eklediğimizde "49" 
#şeklinde yazıyoruz eğer number olarak eklemek istersek direk 49 yazmamız 
#yeterli direk listenin sonuna ekleyecek
numbers.append("49")
numbers.append(49)
print(numbers)

#insert metodu ile istediğimiz konuma eleman ekleyebiliriz
numbers.insert(3,78)
numbers.insert(-1,52)
print(numbers)

numbers.pop()
print(numbers)

numbers.pop(1)
print(numbers)

numbers.pop(-1)
print(numbers)

#aradığımız değeri siler
numbers.remove("49")
print(numbers)

numbers.sort()
letters.sort()
letters.reverse()
print(letters)

numbers.reverse()
print(numbers)

print(len(numbers))
print(len(letters))

print(numbers.count(10))
print(letters.count("a"))

numbers.clear()
print(numbers)
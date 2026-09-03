# value types => string, number
x= 5
y= 25

x=y
y=10
print(x,y)

# reference types => list

# tanımladığımız listede bir eşitleme yaptıktan sonra her hangi bir listede değişiklik yaparsak bu diğer listeyi de etkiler
#reference typler da biz bir address bilgisi taşıyoruz.

a= ["apple","banana"]
b= ["apple","banana"]

a=b
# a ve b listesinin adresi aynı . ben a listesinde değişiklik yaparsam adresin içinde değişiklik yapıyoruz o yüzden adres aynı
#olduğu için  her iki listede değişiyor
b[0] = "grape"

print(a,b)
x,y,z = 2, 5, 10

numbers= 1,5,7,10,6

#1- Kullanıcıdam aldığınız 2 sayısının çarpımı ile x,y,z toplamının farkı nedir
number1= int(input("number 1: "))
number2 = int(input("number2: "))
mult= number1 * number2
sum = x + y+ z
total= mult-sum
print(total)
#2- y'nin x'e kalansız bölümünü hesaplayın
print(y//x)

#3-(x,y,z) toplamının mod 3 ü nedir?
mod = sum % 3
print(mod)

#4- y'nin x. kuvvetini hesaplayın
y= y**x
print(y)

#5- x,*y, z = numbers işlemimine göre z'nin küpü kaçtır?
#216
x,*y, z = numbers 
print(z**3)

#6- x,*y,z = numbers işlemine göre y'nin değerleri toplamı kaçtır?

sumy = y[0]+y[1]+y[2]
print(sumy)
# identidy operator : is
# x= y = [1,2,3]
# z = [1,2,3]
# print(x==y)
# print(x==z)
# # x ve y aynı adres içinde tanımlanmış bir liste
# print(x is y)
# # x ve z farklı adres içinde tanımlanmış bir liste
# print(x is z)

x = [1,2,3]
y= [2,4]
z= [1,2,3]
t =[4,2]
print(x is y)
print(x==z)
print(x is z)
print(y==t)
print(y is t)
print(x is not z)
# membership operator : in

fruit = ["apple","banana"]
print("banana" in fruit)

name = "Cansu"
print("a"in name)
#lists are and tuples aren't mutable.
list = [1,2,3]
tuple = (1, "iki", 3)

# print(type(list))
# print(type(tuple))

# print(len(tuple))
# print(len(list))

list = ["ali","veli"]
tuple=("damla","ayşe","ayşe")
names=("damla","ayşe","ayşe")+ tuple
list[0]= "ahmet"
#tuple de indexlere eleman atadıktan sonra değişiklik yapamıyoruz.
#tuple[0]="deniz"
print(list)
print(tuple)

result=tuple.count("ayşe")
print(tuple.index("ayşe"))
print(result)

print(names)
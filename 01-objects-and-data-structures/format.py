name = "Alice"
surname = "Smith"
age = 30
print("My name is {} {}".format(name, surname))
print("My name is {0} {1}".format(name, surname))
print("My name is {1} {0}".format(name, surname))
print("My name is {s} {n}".format(n=name, s=surname))
print("My name is {} {} and I am {} years old.".format(name, surname, age))

result = 200/ 500
print ("the ressult is {r: 1.3}" .fotmat(r = result))

#f string 

print(f"the result is {r: 1.3}" .format(r = result))
"""
Area of a circle : π * r^2
Circumference of a circle : 2 * π * r

Calculate the area and circumference of a circle given its radius.
(π : 3.14)

"""
pi = 3.14
radius = float(input("Enter the radius of the circle: "))
area = pi * (radius ** 2)
circumference = 2 * pi  * radius
print("Area of the circle:", area)  
print("Circumference of the circle:", circumference)

#print("Area: " + str(area) + ", Circumference: " + str(circumference))
#TypeError: can only concatenate str (not "float") to str

print("Area: " + str(area) + ", Circumference: " + str(circumference))
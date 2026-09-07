x=5
y=10
z=20
print(x,y,z)

#x,y,z=5,10,20
#x,y =y,x

x= x+5 #x+=5
print(x,y,z)

x -= 5 #x=x-5
print(x)

x *= 5 #x=x*5
print(x)

x /= 5 # x = x/5
print(x)

x%=5 # x= x %5
print(x)
t= 16
print(t)
t //= 5 # x= x//5
print(t)

t **= 5 #t= t**5
print(t)

values = 1,2,3,4,5
#values list is tuple.

print(type(values))

print(x,y,z)
x,y,*z= values
#z is list

print(x,y,z)

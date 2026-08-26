website = "https://github.com/cansuanit"
course  = "Python Programming for Beginners"

# 1- 'How many caracters are in the course variable?'
print(len(course))
# 2- 'How many caracters are in the website variable?'
print(len(website))

# 3- 'Pull out www from the website variable'
print(website[8:11])

# 4- 'Pull out the com from the website variable'
print(website[12:15])

# 5- 'Pull out the first 15 characters and last 15 characters from the course variable'
print(course[:15])
print(course[-15:]) 
# 6- 'Print the following expression to the screen using the variables above:

#  "My name is Alice Smith, I am 30 years old and I work as an Engineer."'
name = "Alice"
surname = "Smith"   
age = 30
print(f"My name is {name} {surname}, I am {age} years old and I work as an Engineer.")
# 7 - 'Change the "W" letter "w" in the "Hello World" string to "w" and print it to the screen'
print("Hello World".replace("W", "w"))
# 8 - 'Print "abc" to the screen 3 times' 
print("abc" * 3)
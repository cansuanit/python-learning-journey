website = "http://www.cansuanit.com"
course = "PYTHON COURSE FOR BEGINNERS (40 hours)"

print("1- Remove the whitespace characters from the beginning and end of the string ' Hello World '.")
result = " Hello World ".strip()
print(result)

print ("2-Remove the whitespace character from the beginning of the string ' Hello World '. ")
resultleft = " Hello World ".lstrip()
print(resultleft)

print ("3 -Remove the whitespace character from the end of the string ' Hello World '. ")
resultright = " Hello World ".rstrip()
print(resultright)

print ("4- Remove all characters from 'http://www.cansuanit.com' except for the 'cansuanit' information.")
result =website.lstrip('.w/:pth' ).rstrip('.com')
print(result)
resut = website.strip('htp:/w.com')
print(result)

print ("5 - Convert all characters in the string 'course' to lowercase.")
print(course.lower())

print ("6 - How many 'a' characters are there in 'website'?")
message = "website"
print(message.count('E') or message.count('e'))


print ("7 - Does the 'website' start with 'www' and end with 'com'? ")
result = website.startswith('www')
print(result)
result= website.endswith('com')
print(result)

print ("8 - Does the website string contain the 'com' ?")
result = website.find('com')
print(result)
result = website.find('com',0,10)
print(result)

print ("9 - Does the course string contain the 'python' ?")
result = course.find('PYTHON')
print(result)

print ("10 - Are all the characters in 'course' alphabetical?")
result= course.isalpha()
print(result)

print(" 11-  Are all the characters in 'newword= 'NewWord.'' is alphabetical? ")
newword = "NewWord"
result = newword.isalpha()
print(result)

print("12 - Place the word 'contents' within 50 characters of the line and add a * to both the left and right of it. ")
result = "contents".center(50, '*')
print(result)
result = "contents".ljust(50, '*')
print(result)
result = "contents".rjust(50, '*')
print(result)

print ("13 - Replace all spaces in the string 'course' with '-'.")
result = course.replace(' ','-')
print(result)

print(" 14 - In the character string 'Hello World,' change 'World' to 'There.'")
result = "Hello World".replace('World', 'There')
print(result)


print(" 15 - Separate the string 'course' from the space character.")
result = course.split()
print(result)
salaryAli=5000
salaryAhmet =4000
tax_rate = 0.27

print("Salary after tax deduction for Ali:", salaryAli - (salaryAli * tax_rate))
print("Salary after tax deduction for Ahmet:", salaryAhmet - (salaryAhmet * tax_rate))

#Variables Defination Rules:
#1. Variables names must start with a letter or underscore.
#2. Variables names cannot start with a number.
number1=10
print("number1:", number1)

number1=20
print("number1:", number1)

number1 += 30 
#The variable adds its previously held value to the last assigned value and prints the result.
print("number1:", number1)
#3. Variables names can only contain alphanumeric characters and underscores (A-z, 0-9, and _).
#4. Variables names are case-sensitive. 

age = 20
Age=30
print("age:", age)
print("Age:", Age)

# x, y , name, isStudent = (1, 2, "Cansu", True) #This line will cause a syntax error because variable names cannot contain spaces.

x =1    #integer variable
y=2     #integer variable
z=3.5   #float variable
name="Cansu"    #string variable
isStudent=True  #boolean variable 

a= "10"
b= "20"
print("a+b:", a+b) #The result will be 1020 because the variables
# are strings and the + operator concatenates them instead of adding them numerically.

firstName = "Cansu"  # This line will cause a syntax error because variable names cannot contain spaces.
lastName = "Anıt"  # This line will cause a syntax error because variable names cannot contain spaces.

print (firstName + " " + lastName)  # This line will cause a syntax error because variable names cannot contain spaces.
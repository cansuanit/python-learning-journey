# 1- Create a list containing the following elements: "BMW", "Mercedes", "Opel", and "Mazda".
brand_list = ["BMW","MERCEDES","OPEL", "MAZDA"]
print("List         :   " + str(brand_list))
# 2- How many elements are there in the list?
count_brand_list = len(brand_list)
print("How many elements are there in the list:"+ str(count_brand_list))
# 3- What are the first and last elements of the list?
firs_element = brand_list[0]
last_element = brand_list[-1]
print("What are the first and last elements of the list?    :   "+firs_element + " "+ last_element)
# 4- Replace "Mazda" with "Toyota".
brand_list[3]= "TOYOTA"
print(brand_list)
# 5- Is "Mercedes" an element of the list?
result = "MERCEDES" in brand_list
print(result)
# 6- What is the value at index -2?
print(brand_list[-2])
# 7- Get the first three elements of the list.
print(brand_list[:2])
# 8- Replace the last two elements of the list with "Toyota" and "Renault".
brand_list[-2:] = ["TOYOTA", "RENAULT"]

print(brand_list)

# 9- Add "Audi" and "Nissan" to the list.
result = brand_list + ["Audi","Nissan"]
print(result)
# 10- Delete the last element of the list.
del brand_list [-1]
print(brand_list)
# 11- Print the list elements in reverse order.
result = brand_list[::-1]
print("Reverse List" + str(result))
# 12- Store the following data in a list.

# Student A: Yiğit Bilgi, 2010, (70, 60, 70)
# Student B: Sena Turan, 1999, (80, 80, 70)
# Student C: Ahmet Turan, 1998, (80, 70, 90)
studentA = ["Yiğit","Bilgi",2010, [70,60,70]]
studentB = ["Sena","Turan",1999, [80,80,70]]
studentC= ["Ahmet","Turan", 1998, [80,70,90]]

# 13- Print the list elements to the screen.
result= studentA[0]
print(result)
result=studentB[1]
print(result)

result=studentC[3]
print(result)

result =studentC[3][1]
print(result)

result= f"{studentA[0]} {studentA[1]} {2026-studentA[2]} yaşında ve not ortalaması {(studentA[3][0]+studentA[3][1]+studentA[3][2])/3}"
print(result)
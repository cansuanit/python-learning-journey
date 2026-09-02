
#STUDENTS 

#1-Bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgileere dictionary içinde saklayin.
#2- Öğrenci numarası kullanıcıdan alıp ilgili öğrenci bilgisini gösterin
# ad, soyad, telefon, öğrenci numarası

students={}

student_number= input("student number: ")
student_name = input("student name: ")
student_surname = input ("student surname: ")
student_phone= input("student phone number: ")

# students[student_number] = {
#     "student_name" : student_name,
#     "student_surname": student_surname,
#     "student_phone": student_phone
# }
# print(students)

students.update({
    student_number:{
        "student_name" : student_name,
        "student_surname": student_surname,
        "student_phone": student_phone
    }
})
print("*"*50)
print(students)

std_no=input ("student number")
print(f"Aradığınız öğrencinin adı: {student_name} soyadı : {student_surname} ve telefonu :{student_phone}")
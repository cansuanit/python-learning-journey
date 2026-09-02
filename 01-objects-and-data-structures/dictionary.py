#key -value pairs

#41 => kocaeli 34 => istanbul

# sehirler = ["kocaeli","istanbul"]
# plakalar = [41,34]

# print(plakalar [sehirler.index("istanbul")])

#print(plakalar ["kocaeli"=> 41])

#dictionary ={"key" : "value"}

# plaka_dictionary = {"kocaeli":"41", "istanbul":"34"}


# plaka_dictionary["ankara"]= "06"


# print  (plaka_dictionary)

user = {
    "cansuanit" : {
        "age" : "39",
        "roles": ["admin","user"],
        "email": "cansuanit@outlook.com",
        "adress": "sakarya",
        "phone" :"123456"
    },
    "miraanit"  :{
    "age": "9", 
    "roles" : ["user"],
    "email" : "mira@gmail.com",
    "adress" : "serdivan",
    "phone" :  "456123"}

}
print(user["cansuanit"]["roles"])
print(user["cansuanit"]["roles"][0])
print(user["cansuanit"]["roles"][1])

print(user["cansuanit"]["age"])
print(user["cansuanit"]["email"])
print(user["cansuanit"]["adress"])
print(user["cansuanit"]["email"])
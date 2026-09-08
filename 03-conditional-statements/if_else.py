
# isLoggedin = False
# if isLoggedin == True:
#  print("Hoş geldiniz.")

username = "cansuanit"
password= "1234"

isLoggedin = (username == "cansuanit") 


if isLoggedin:
    print("Bilgiler doğru")
    if (password == "1234"):
        print("hoşgeldiniz")
    else:
        print("parola yanlış")
else:
    print("username yanlış ")
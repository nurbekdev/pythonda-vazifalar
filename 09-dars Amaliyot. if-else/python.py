"""
Created on Fri Oct 15 14:56:54 2021

@author: Nurbek Po'latov

"""
#1-vazifa

cars = ["toyota" , "mazda" , "hyundai" , "gm" , 'kia']
for car in cars:
    if car ==  "gm":
        print(car.upper())
    else:
        print(car.title())

#2-vazifa

cars = ["toyota" , "mazda" , "hyundai" , "gm" , 'kia']
for car in cars:
    if car !=  "gm":
        print(car.title())
    else:
        print(car.upper())
        
#3-vazifa

ism = input("Foydalanuvchi iltimos ismingizni kiriting: ")
f_ism = ism.lower()
if f_ism == 'admin':
    print("Xush kelibsiz,Admin.Foydalanuvchilar ro'yhatini ko'rasizmi")
else:
    print(f"Xush kelibsiz,{f_ism.title()}")

#4-vazifa

b_son = input("1-Sonni kiritng: ")
i_son = input ("2-sonni kiring: ")
if b_son ==i_son:
    print(f"Sonlar teng {b_son == i_son}")
else:
    print("Sonlar teng emas")
    
#5-vazifa

son = input("Istalgan sonni kiring: ")
if son < 0 :
    print("Manfiy son")
else:
    print("Musbat son")

#6-vazifa

son = int(input("Istalgan son kiriting: "))
if son > 0 :
    print(f"Siz kiritgan sonning ildizi {son**0.5}")
else:
    print("Iltimos musbat son kiriting")

#7-vazifa

son = int(input("Istalgan son kiritng: "))
if son%2==0:
    print("Siz kiritgan son Juft")
else:
    print("Siz kiritgan son Toq")



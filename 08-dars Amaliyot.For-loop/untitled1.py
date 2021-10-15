"""
Created on Wed Oct 13 12:30:14 2021

@author: Nurbek Po'latov


"""
#1-vazifa

dostlar  = ["davron", "nurbek" , "asadbek" , "otabek", "shohjahon"]
for dost in dostlar:
    print(f"Salom {dost.title()} ishlaring yaxshimi")
    
#2-vazifa

print(f"Kod {len(dostlar)} marta takrorlandi")

#3-vazifa

sonlar = list(range(11,100,2))
for son in sonlar:
    print(f"{son} ning kubi {son**3}\n")

#4-vazifa

kinolar = []
print("Sevimli kinolarizni kriting")
for kino in range(5):
    kinolar.append(input(f"{kino+1}-kinoni nomini kiritng: "))
print(kinolar)

#5-vazifa

odamlar = int(input("Bugun necha kishi bn suhbat qildingiz?"))
ismlar = []
for n in range(odamlar):
    ismlar.append(input(f"{n+1}-suhbat qilgan odamingizni kiritng: "))
print(ismlar)
    

    

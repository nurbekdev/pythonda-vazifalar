"""
Created on Tue Oct 12 11:59:14 2021

@author: Nurbek Po'latov

"""
#1-vazifa

ismlar =  ['davron','nurbek','otabek','asadbek']

#2-vazifa

print("Salom " + ismlar[0].title() + " ishlaring yaxshimi?")
print(f"{ismlar[2].title()} va {ismlar[3].title()} egizaklar")
print(ismlar[-1].title() + " g'ildirakni g'izillatib g'ildratti")

#3-vazifa

sonlar = [-6 , 10 , 23 , 78 , -9 , 5]

#4-vazifa

sonlar[0] = sonlar[2]-sonlar[-1]
sonlar[1] = 80
sonlar[4] = sonlar[1] + 87
del sonlar[3]
print(sonlar)




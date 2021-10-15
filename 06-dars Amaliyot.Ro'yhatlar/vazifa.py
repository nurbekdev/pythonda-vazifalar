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

#5-vazifa

t_shaxslar = ["mirzo ulug'bek" , "alisher navoiy" , "amir temur" ]
z_shaxslar = ["anvar narzullayev" , "bill gets" , "elon musk"]

#6-vazifa

print(f"\nMen tarixiy shaxslardan {t_shaxslar.pop(1).title()} bilan,\n\
zamonaviy shaxslardan esa {z_shaxslar.pop(0).title()} bilan\n\
suhbat qilishni istar edim\n")

#7-vazifa

friends = []
friends.append('Nurbek')
friends.append('Asadbek')
friends.append('Otabek')
friends.append('Davron')
friends.append('Ali')
print(friends)

#8-vazifa

friends.remove('Davron')
friends.remove('Ali')
print(friends)

#9-vazifa

friends.append('Mansurxon')
friends.insert(0, 'Alisher')
friends.insert(2, 'Xusan')
print(friends)


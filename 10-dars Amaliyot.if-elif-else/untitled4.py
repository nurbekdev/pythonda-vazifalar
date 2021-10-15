"""

Created on Fri Oct 15 16:18:49 2021

@author: Nurbek Po'latov

"""
mahsulotlar = ['un', "yog'", "shakar", 'guruch', 'piyoz',
               'non', 'olma', 'banan', 'kartoshka', 'sovun']

savat = []
for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

if savat:
    for mahsulot in savat:
        if mahsulot in mahsulotlar:
            print(f"Do'konimizda {mahsulot} bor")
        else:
            print(f"Do'konimizda {mahsulot} yo'q")
else: 
    print("Savatingiz bo'sh")      


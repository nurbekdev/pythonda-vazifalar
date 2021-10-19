"""

Created on Tue Oct 19 15:34:00 2021

@author:Nurbek Po'latov

"""
menu = {
        'manti':3000,
        "shashlik":20000,
        'osh':17000,
        'choy':5000,
        'pilmin':12000,
        'somsa':6000,
        'tabaka':15000
        }

print('3 ta taom buyurtma bering.')
buyurtmalar = []
for n in range(3):
    buyurtmalar.append(input(f"{n+1}-taom:").lower())

for buyurtma in buyurtmalar:
    if buyurtma in menu:
        print(f"{buyurtma.title()} {menu[buyurtma]} so'm")
    else:
        print(f"Kechirasiz, bizda {buyurtma} yo'q.")


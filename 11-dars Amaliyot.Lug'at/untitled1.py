"""

Created on Sat Oct 16 11:26:33 2021

@author: Nurbek Po'latov

"""
otam = {'ismi':'xayrullo', 'tyil':1976,'viloyat':'qashqadaryo'}
tyil = otam['tyil']
vil = otam['viloyat']
print(f"Otamning ismi {otam['ismi'].title()}, {tyil}-yilda, {vil.title()} viloyatida tug'ilgan")

taomlar = {
    'nurbek':'manti',
    'nurullo':'somsa',
    'zarifa':"lavash",
    'nodir':"shashlik",
    'alisher':"tandir"
    }

taom = taomlar['nurbek']
print(f"Alining sevimli taomi {taom}")

python_izohli_lugati = {
    'integer':"Butun son",
    'float':"O'nlik son",
    'string':"Matn",
    'list':"Ro'yxat",
    'tuple':"O'zgarmas ro'yxat"}


kalit = input("Kalit so'z kiriting:").lower()
print(python_izohli_lugati.get(kalit,"Bunday so'z mavjud emas"))

kalit = input("Kalit so'z kiriting:").lower()
tarjima = python_izohli_lugati.get(kalit)
if tarjima==None:
    print("Bunday so'z mavjud emas")
else:
    print(f"{kalit.title()} so'zi {tarjima} deb tarjima qilinadi")
    


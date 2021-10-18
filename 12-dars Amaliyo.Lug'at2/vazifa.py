"""
Created on Mon Oct 18 15:54:09 2021

@author: Nurbek Po'latov

"""
python_lugat = {
    'string':'Matn',
    'float': "O'nlik son",
    'integer':'Butun son',
    'boolean':"Mantiqiy qiymat",
    'for':"Biror amalni qayta-qayta bajarish tsikli",
    'if':'Shartlarni tekshirish operatori'}

for key, value in sorted(python_lugat.items()):
    print(f"{key.title()} - {value}")


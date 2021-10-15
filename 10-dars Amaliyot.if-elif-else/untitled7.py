"""

Created on Fri Oct 15 16:24:25 2021

@author:Nurbek Po'latov

"""

son = int(input("Istalgan butun son kiriting: "))

for n in range(2,11):
    if not (son%n):
        print(f"{son} soni {n} ga qoldiqsiz bo'linadi")
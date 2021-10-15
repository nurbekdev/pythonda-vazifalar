# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 15:52:45 2021

@author: Nurbek Po'latov

"""
yosh = int(input("Yoshingiz nechida?"))

if yosh<=4 or yosh>=60:
    narh = 0;
elif yosh < 18:
    narh = 10000
else:
    narh = 20000
print(f"Chipta {narh} so'm")


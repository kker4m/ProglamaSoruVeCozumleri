# -*- coding: utf-8 -*-
"""
Find whether the entered number is Pronic (equal to the product of two consecutive numbers)?

Girilen sayının Pronic olup olmadığını bulun (ardışık iki sayının çarpımına eşit)?
"""
nmb=int(input("Please enter a number..:"))
elist=[]
for i in range(1,nmb+1):
    b=nmb/i
    elist=elist+[b]
if len(elist)>2 or nmb==0 or nmb==2:
    print("\nThis number is a Pronic number")
else:
    print("\nThis number is not a pronic number")
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 16:08:22 2021

@author: mrtke
"""

"""
The program that sorts the elements?

Öğeleri sıralayan program?
"""

hmr=int(input("How many element u want to add and sort ?.. :  "))
elist=[]
for i in range(hmr):
    i=int(input("Please enter a number..: "))
    elist=elist+[i]
elist=sorted(elist,reverse=False)
print("From biggest to smallest, ur sorted list is :\n------------ ")
for i in elist:
    print(i,end=" ")
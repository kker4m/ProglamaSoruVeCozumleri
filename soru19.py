# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 16:05:05 2021

@author: mrtke
"""

"""32.Find LMC ( EKOK )  """
"""school"""
nmb=int(input("Please enter a number..: "))
[x,b]=[2,1]
elist=[]
while not nmb==1:
    if nmb%x==0:
        nmb=int(nmb/x)
        elist=elist+[x]
    else:
        x+=1
for i in elist:
    b=b*i
print('\nThe LMC ( EKOK ) of your number is..: ',b)
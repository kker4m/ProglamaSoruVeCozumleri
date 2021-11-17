# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 16:06:24 2021

@author: mrtke
"""

"""
Program to calculate the biggest common divisor of two numbers

İki sayının en büyük ortak bölenini hesaplayan program ( EBOB )
"""
 
 
nmb1=int(input("Please enter number one.. : "))
nmb2=int(input("Please enter number two.. : "))
[x,result]=[2,1]
elist=[]
while not [nmb1,nmb2]==[1,1]:
    if nmb1%x==0 and nmb2%x==0:
        nmb1=nmb1/x
        nmb2=nmb2/x
        elist=elist+[x]
    elif nmb1%x==0 and (nmb2%x) != 0:
        nmb1=nmb1/x
    elif nmb2%x==0 and (nmb1%x) != 0:
        nmb2=nmb2/x
    else:
        x+=1
for i in elist:
    result=i*result
print("\nResult is..: ",result)
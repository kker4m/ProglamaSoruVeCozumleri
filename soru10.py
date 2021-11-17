# -*- coding: utf-8 -*-
"""
Convert the entered decimal number to binary number?

Girilen ondalık sayı ikili sayıya dönüştürülsün mü?
"""
dn=int(input("Please enter a decimal number to convert binary number..: "))
elist=[]
while 1==1:
    if dn !=0:
        a=dn%2
        elist=elist+[a]
        dn=int(dn/2)
    else:
         break
elist=elist[::-1]
print("Binary equivalent of the number you entered is :")
for i in range(len(elist)):
    print(elist[i],end=" ")


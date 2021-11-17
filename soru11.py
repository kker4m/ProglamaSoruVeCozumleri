# -*- coding: utf-8 -*-
"""
Convert the entered decimal number to hexadecimal number?

Girilen ondalık sayı onaltılık sayıya dönüştüren program?
"""
dn=int(input("Please enter a decimal number to convert hexadecimal number..: "))
elist=[]
while 1==1:
   if dn !=0:
       a=dn%16
       elist=elist+[a]
       dn=int(dn/16)
   else:
       break
elist=elist[::-1]
elist=['A' if i==10 else 'B' if i==11 else 'C' if i==12 else 'D' if i==13 else 'E' if i==14 else 'F' if i==15 else i for i in elist]
print("Hexadecimal equivalent of the number you entered is :")
for i in range(len(elist)):
   print(elist[i],end="")

# -*- coding: utf-8 -*-
"""
Program that prints the number of digits of the entered number to the screen?

Girilen sayının basamak sayısını ekrana yazdıran program?
"""
a=0
nmb=int(input("Please enter a number..: "))
nmb=list(str(nmb))
for i in range(len(nmb)):
    a+=1
print("Number of digits of the number you entered is..: ",a)
# -*- coding: utf-8 -*-
"""
k of the text entered. with the character r. Write a program that copies between characters?

Girilen metnin k ile r karakterleri arasında kopyalama yapan bir program yazınız
"""
txt=input("Enter a text..: ")
k=int(input("Please select the starting point you want to copy.. : "))
r=int(input("Select the endpoint you want to copy.. : "))
newtxt=txt[k:r]
print("Your copied text is : ",newtxt)
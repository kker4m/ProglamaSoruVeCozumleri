# -*- coding: utf-8 -*-
"""
37.Program to find the number of space characters in the text entered? 
Girilen metindeki boşluk karakterlerinin sayısını bulan program?
"""
txt=input("Please enter a text to know how many space characters in it.. : ")
a=0
for i in txt:
    if i==" ":
        a+=1
    else:
        pass
print("\nThere are {} space characters in your sentence.".format(a))
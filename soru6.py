# -*- coding: utf-8 -*-
"""
Program to reverse an entered 3-digit number? (573 ==> 375)

Girilen 3 basamaklı bir sayıyı tersine çevirmek için program? (573 ==> 375)
"""
n=int(input('Enter your number to reverse: '))
a=int(n/100)
b=int((n-(a*100))/10)
c=int(n-((a*100)+(b*10)))
print('\nReverse style is :',str(c)+str(b)+str(a))

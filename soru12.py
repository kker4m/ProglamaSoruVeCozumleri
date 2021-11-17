# -*- coding: utf-8 -*-
"""
Convert the entered binary number to decimal number?

Girilen ikili sayı ondalık sayıya dönüştürülsün mü?
"""
bn=input("Please enter a binary number to convert decimal number..: ")
bn=bn[::-1]
end=[]
a,c=[0,0]
for i in bn:
    b=int(i)*(2**a)
    a +=1
    c=b+c
print('\nThe decimal equivalent of the number you entered is.. :',c) 

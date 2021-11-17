# -*- coding: utf-8 -*-
"""
Girilen 5 sayının standart sapmasını bulan program?

Program to find standard deviation of 5 entered numbers?
"""
b=[]
for x in range(5):
    a=int(input('Please enter a number: '))
    b=b+[a]
d=0
for c in b:
    d=c+d
arithmetic_mean=d/(len(b))
g=0
for x in b:
    n=x-arithmetic_mean
    n=n**2
    g=n+g
    
sd=g/(len(b)-1)
if sd<0:
    sd=sd*-1
    sd=sd**(1/2)
else:
    sd=sd**(1/2)
    
print('Our standart deviation is: ',sd)

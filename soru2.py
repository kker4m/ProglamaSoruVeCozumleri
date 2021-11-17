# -*- coding: utf-8 -*-

"""
Girilen 5 sayının ortalamasını bulan program?

Program to find the average of 5 entered numbers?
"""

b=[]
for x in range(5):
    a=int(input('Please enter a number: '))
    b=b+[a]
d=0
for c in b:
    d=c+d
print('average of 5 numbers is: ',d/5)

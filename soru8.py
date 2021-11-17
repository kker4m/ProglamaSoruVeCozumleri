# -*- coding: utf-8 -*-
"""
Program to find prime factors of a given number?

Verilen bir sayının asal çarpanlarını bulan program?
"""
bolen=2
numb=int(input("\nPlease enter a  number: "))
for i in range(0,numb):
    if(numb%bolen==0):
        print(bolen)
        numb/=bolen
    else:
        bolen=bolen+1
        
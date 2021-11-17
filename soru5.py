# -*- coding: utf-8 -*-
"""
Girilen n ve k değerlerine göre k + 2k + 3k + ...+nk hesaplayan program?

Program that calculates k + 2k + 3k + ...+nk according to the entered n and k values? 
"""
k=int(input('k value= '))
n=int(input('n value= '))
h,a=0,0
for x in range(n+1):
    j=k*x
    h=j+h
print('\nYour result is: ',h)
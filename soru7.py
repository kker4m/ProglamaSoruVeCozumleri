# -*- coding: utf-8 -*-
"""
Print after receiving information from the user how many Fibonacci numbers to generate

Kullanıcıdan kaç Fibonacci sayısının üretileceği bilgisini aldıktan sonra yazdırın
"""
n=int(input('How many fibonacci numer u want : '))
a=0
b=1
print(a)
print(b)
for x in range(n-1):
    f=a+b
    print(f)
    a=b
    b=f
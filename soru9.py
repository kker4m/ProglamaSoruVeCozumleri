# -*- coding: utf-8 -*-
"""
Keep multiplying until the product of the place values ​​of the entered number drops to a single digit, and the program that writes the resulting products?

Girilen sayının basamak değerlerinin çarpımı tek haneye düşene kadar çarpmaya devam edin ve ortaya çıkan sonucu yazdıran program?
"""
numb=input("Please enter a number: ")
carpim=1
sonuc=1
for rakam in str(numb):
  if int(rakam) != 0:
    carpim *= int(rakam)
carpim=str(carpim)
for rakam in str(carpim):
  if int(rakam) != 0:
    sonuc *= int(rakam)
if len(carpim)>1:
    print("Multiplication of digits of a number: ",sonuc)
else:
    print("Multiplication of digits of a number:",carpim)

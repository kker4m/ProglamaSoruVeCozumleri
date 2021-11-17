# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 16:07:48 2021

@author: mrtke
"""

"""34.Number guessing game 
Sayı tahmin oyunu
"""

import random
a=random.randint(1,100)
for i in range(1,11):
  sayi=int(input(str(i)+'. hak >> Sayıyı Girin :'))
  if(sayi>a):
    if(i>=10):
      print("Hakkınız kalmadı :(" )
      print("Tutulan Sayı",a)
      break
    print("Daha küçük bir sayı giriniz.")
  elif(sayi<a):
    if(i>=10):
      print("Hakkınız kalmadı :( ")
      print("Tutulan Sayı : ",a)
      break
    print("Daha büyük bir sayı giriniz.")
  else:
    print("Tebrikler :)",i,". Hakkınızda bildiniz.")
    break
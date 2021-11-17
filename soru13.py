# -*- coding: utf-8 -*-
"""
Program that lists the place values ​​of numbers up to n that do not have k digits?

K basamağı olmayan n'ye kadar olan sayıların basamak değerlerini listeleyen program?
"""
nd=int(input("Please enter the n digit..: "))
k=int(input("Please enter the k digit..: "))
for i in range(0,nd+2):
    while 1==1:
        if i==k:
            break
        else:
            if i%10==3 or i%100==3:
                i=list(str(i))
                print(i[0])
                break
            else:
                print(i)
                break


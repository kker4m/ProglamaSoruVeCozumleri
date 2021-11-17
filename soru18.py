# -*- coding: utf-8 -*-
"""
List how many Harshads (if the number itself is divided by the sum of its digits)?

Verilen değer kadar harshad sayııs listeleyiniz (Harshard = eğer sayının kendisi rakamları toplamına bölünürse)?
"""
nmb=int(input("Please enter a number..: "))
elist=[]
[a,b,c]=[0,0,0]
for i in range(1,nmb+1):
    a=int(i/100)
    b=int((i-(a*100))/10)
    c=int(i-((a*100)+(b*10)))
    if i%(a+b+c)==0:
        elist=elist+[i]
    else:
        pass
print("Harshad numbers up to the number you give :",elist,end="")

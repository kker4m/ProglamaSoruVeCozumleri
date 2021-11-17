# -*- coding: utf-8 -*-
"""
36.Program to find the number of repetitions of each element? 
Her elemanın tekrar sayısını bulan program?
"""

hmr=int(input("How many element u want to add and sort ?.. :  "))
elist=[]
elistwoe=[]
a=0
for i in range(hmr):
    i=int(input("Please enter a number..: "))
    elist=elist+[i]
    elistwoe=elistwoe+[i]
elistwoe=list(set(elistwoe))
for i in elistwoe:
    for k in elist:
        if i==k:
            a+=1
    print("\n{} element is {} times typing in the list u wrote.".format(i,a))
    a=0

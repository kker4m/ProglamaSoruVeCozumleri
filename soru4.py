# -*- coding: utf-8 -*-
"""
Girilen numaranın listede olup olmadığını bulan program?

Program to find if the entered number is in the list?
"""
exlist=[15,23,1,2,3,5,123,6,568,4]
sj=int(input('Which number do you want to know exists?: '))
if exlist.count(sj)>=1:
    print('\nThe number you are looking for is in {} lists'.format(sj))
else:
    print('\nThe number you are looking for is not in the list.')

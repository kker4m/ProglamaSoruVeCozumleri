# -*- coding: utf-8 -*-

"""
İşçi maaşı ve çocuk sayısı verilmektedir. Çocuk sayısı bir ise %5, iki ise %10, üç veya daha fazla ise %15 zam yaparak yeni maaşı hesaplayınız?

Employee salary and number of children are given. Calculate the new salary by increasing 5% if the number of children is one, 10% if two, and 15% if there are three or more? 
"""
while 1==1:
    try:
        client_salary=int(input('Please enter your salary: '))
        client_child=int(input('Please enter the number of children u have: '))
        break
    except(ValueError):
        print('\nPlease type a number !')
if client_child==1:
    client_salary=client_salary*0.05+client_salary
    print('\nYour new salary is {}'.format(client_salary))
elif client_child==2:
    client_salary=client_salary*0.1+client_salary
    print('\nYour new salary is {}'.format(client_salary))
elif client_child>=3:  
    client_salary=client_salary*0.15+client_salary
    print('\nYour new salary is {}'.format(client_salary))
else:
    print('\nProgram haved a error, please try again.')
    
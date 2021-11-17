# -*- coding: utf-8 -*-
"""
3 side lengths are entered from the keyboard. Program that calculates whether a triangle can be drawn considering the entered side lengths, and if it can be drawn, its type (isosceles, scalene, equilateral), area and perimeter?

Klavyeden 3 kenar uzunluğu girilir. Girilen kenar uzunluklarına göre üçgen çizilip çizilemeyeceğini, çizilebiliyorsa türünü (ikizkenar, eşkenar), alanını ve çevresini hesaplayan program?
"""
a=int(input("Please enter the first side of the triangle..: "))
b=int(input("Please enter the second side of the triangle..: "))
c=int(input("Please enter the last side of the triangle..: "))
if abs(a+b)>c>abs(a-b):
    if a==b or a==c or b==c:
        if a==b==c:
            print("\nThis triangle is equilateral triangle (Bu üçgen eşkenar üçgendir)")
        else:
            print("\nThis triangle is isosceles triangle(Bu üçgen ikizkenar üçgendir)")
    else:
        print("\nThis triangle is a scalene triangle(Bu üçgen çeşitkenar bir üçgendir)")
else:
    print("\nThis triangle cannot be drawn.(Bu üçgen çizilemez) ")


"""
31.Write a program that gives the following output? 

0!=1 , 1!=1 , 2!=2 , 3!=6 , 4!=24 , 5!=120 , 6!=720 , 7!=5040 , 8!=40320 , 9!=362880

Yukarıda ki çıktıyı veren programı yazınız.
"""
def exercise31pre1(sayi):
    f=1
    for i in range(1,sayi+1):
        f = i*f
    return f
for i in range(1,10):
    a=str(exercise31pre1(i))
    print(str(i)+"! = "+a)

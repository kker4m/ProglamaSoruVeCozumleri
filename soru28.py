"""
41.The program that adds the LINK symbol before and after the searched word in the entered text?

Girilen metinde aranan kelimenin önüne ve arkasına tırnak sembolünü ekleyen program?
"""
txt=input("Please enter the text.. : ")
sword=input("Please enter the searched word.. : ")
a=0
newcumle=""
elist=txt.split()
for i in elist:
    if i==sword:
        elist[a]="'"+elist[a]+"'"
    a+=1
for i in elist:
    newcumle=newcumle+i+" "
print(newcumle)

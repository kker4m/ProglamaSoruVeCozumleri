"""
Program that finds whether the entered text is capitalized or not?

Girilen metnin büyük harf olup olmadığını bulan program?
"""
[a,b]=[0,0]
txt=input("Please enter a text.: ")
alfabe={"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","R","S","T","Y","U","V","Y","Z"," "}
for i in txt:
    b+=1
    for k in alfabe:
        if i==k:
            a+=1
        else:
            pass
if b==a:
    print("Ur text is all capitalized")
else:
    print("Your text has lowercase letters")
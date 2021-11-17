"""
Delete punctuation marks in entered text

Girilen metindeki noktalama işaretlerini sil
"""
txt=input("Please enter the text.. : ")
for i in txt:
    if i.isalpha():
        pass
    elif i.isnumeric():
        pass
    else:
        txt=txt.replace(i, "")
"""
Word or letter extraction program from the given sentence

Verilen cümleden kelime veya harf çıkarma programı
"""
txt=input("Please enter the text.. : ")
dc=input("What chard u want to delete from text : ")
if txt.__contains__(dc)==1:
    txt=txt.replace(dc, "")
    print(txt)
else:
    print("There is no chard in text like u wrote")
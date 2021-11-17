"""
Program that finds the number of words, numbers and characters in the text entered?

Girilen metindeki kelime, sayı ve karakter sayısını bulan program?
"""
txt=input("Please enter a text.. : ")
numbers=["0","1","2","3","4","5","6","7","8","9"]
[letters,characters,other,digit,x]=[0,0,0,0,txt]
for i in x:
    if i.isalpha():
        letters+=1
    elif i.isnumeric():
        digit+=1
    else:
        other+=1
print("Your text have {} number in it.".format(digit))
print("Your text have {} letter in it.".format(letters))
print("Your text have {} other in it.".format(other))

#Modül kullanmamak yerine alfabenin ve numerik sayıların bulunduğu ayrı bir liste oluşturabilir. Çözümün kısa gözükmesi için bu yolu izledim.

#Instead of using a module, it can create a separate list of alphabets and numeric numbers. I followed this path to make the solution look short and nice.

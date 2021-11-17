"""
33.Find whether the entered date is appropriate or not?

Girilen tarihin uygun olup olmadığını bulun.
"""
date=input("Please enter a date.(Ex: 13.07.1997)..: ")
date=date.split(".")
a=(date[2].__len__())
date = [int(x) for x in date]
if type(date)==list:
    if 0<date[0]<=30 and 0<date[1]<=12:
        if a==4:
            print("Your date is avaible")
        else:
            print("Your date is not avaible")
    else:
        print("Please enter a valid date.")
else:
    print("y")
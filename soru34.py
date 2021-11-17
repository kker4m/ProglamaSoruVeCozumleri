"""
The program that deletes the most repeating element in the list?

Listedeki en çok tekrar eden öğeyi silen program?
"""
counter=0
elist=[]
les=int(input("How many elements u want to add to the list : "))
for i in range(les):
    a=int(input("Please write a number to add tot the list: "))
    elist=elist+[a]
for i in elist:
    rn=0
    for k in elist:
        if i==k:
            rn+=1
    if (rn>counter):
        counter=rn
        num=i
print("\nMost repeated element is : ",num)
for i in range(counter):
    elist.remove(num)
print("Your new list is :",elist)
"""
32.Program to list first N prime number? 

İlk N asal sayıyı listeleyen program?
"""
n=int(input("How many prime number u wanna list.. : "))
a=1
elist=[]
while not n==0:
    elist=elist+[a]
    a+=2
    n-=1
for i in elist:
    print(i,end=" ")
    
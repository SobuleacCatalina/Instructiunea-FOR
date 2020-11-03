#Utilizînd ciclul FOR elaboraţi un program care afişează toate numerele impare, pentru intervalul de la a la b (a și b se citesc de la tastatură).
a=int(input("Introdu a:"))
b=int(input("Introdu b:"))
if a%2==0:
    for i in range(a+1,b,2):
        print(i,end=" ")
else:
    for i in range(a,b,2):
        print(i,end=" ")
"""
Să se calculeze sumele: 	s1=1+2+3+…+n
s2=1*2+2*3+3*4+…+(n-1)*n
s3=1+1*2+1*2*3+…+1*2*3*…*n
s4=12+22+32+…+n2
s5=1/2+2/3+3/4+…+n/(n+1)
s6=1+2+22+23+24+…+2n
Notă: Pentru fiecare sumă n – se va citi de la tastatură.
"""
n1=int(input("Introdu n1 :"))
n2=int(input("Introdu n2 :"))
n3=int(input("Introdu n3 :"))
n4=int(input("Introdu n4 :"))
n5=int(input("Introdu n5 :"))
n6=int(input("Introdu n6 :"))
s1=0
s2=0
s3=0
s4=0
s5=0
s6=3
for i in range(1,n1+1):
    s1+=i
for i in range(2,n2+1):
    s2+=(i-1)*i
for i in range(1,n3+1):
    p=1
    for n in range(1,i+1):
        p*=n
    s3+=p
for i in range(1,n4+1):
    s4+=i*10+2
for i in range(1,n5+1):
    s5+=i/(i+1)
for i in range(2,n6+1):
    if i<10:
        s6+=20+i
    else:
        s6+=2*(i//10)+i
print("s1=",s1,sep="")
print("s2=",s2,sep="")
print("s3=",s3,sep="")
print("s4=",s4,sep="")
print("s5=",s5,sep="")
print("s6=",s6,sep="")
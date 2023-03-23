n=int (input("enter \"5\" "))
c=[]
b=[]
a=0
for i in range (n):
    if (i==((n+1)/2-1)):
        print("-"*2*i,"WELCOME","-"*2*i)
    elif(i<2):
        print(("-"*((n+1+i)-4*i)),".|."*(2*i+1),"-"*((n+1+i)-4*i))
        c.append((n+1+i)-4*i)
        b.append(2*i+1)
    else :
        print("-"*c[a+1],".|."*b[a+1],"-"*c[a+1])
        a=a-1
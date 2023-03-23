n=int(input())
a=0
b=1
print(a,end=" ")
print(b,end=" ")
for item in range(3,n+1):
   c=a+b
   print(c,end=' ')
   a=b
   b=c


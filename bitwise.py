a,b =(input()).split()
k= int(input())
a =int(a)
b =int(b)
c= a&b
d= a|b
e= a^b
if(c>d and c>e):
    if(c<k):
        print(c)
    else:
        print("0")
elif(d>c and d>e):
    if(d<k):
        print(d)
    else:
        print('0')
elif(e>c and e>d):
    if(e<k):
        print(e)
    else:
        print('0')
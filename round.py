num = float (input("Enter any no.:"))
if((num +0.5)<int(num +1)):
    print(int(num))
elif((num +0.5)==int(num +1)):
    if(int(num)%2==0):
        print(int(num))
    else:
        print(int(num)+1)
else:
    print(int(num)+1)
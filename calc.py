a=float(input("Enter first digit:"))
opr=input("Enter the operator:")
c=float(input("Enter second digit:"))
if(opr=='+'):
    print(a+c)
elif(opr=='-'):
    print(a-c)
elif(opr=='*'):
    print(a*c)
elif(opr=='/'):
    print(a/c)
elif(opr=='**'):
    print(a**c)
elif(opr=='%'):
    print(a%c)
elif(opr=='//'):
    print(a//c)

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1=name1.upper()
name2=name2.upper()
name3=name1+name2

n=0
T= name3.count("T")
R= name3.count("R")
U= name3.count("U")
E= name3.count("E")
true= T+R+U+E
l= name3.count("L")
o= name3.count("O")
v= name3.count("V")
e= name3.count("E")
love=l+o+v+e
score=int(str(true)+str(love))
if(score<10 or score>90):
    print(f"Your score is **{score}**, you go together like coke and mentos.")
elif( score>40 and score<50):
    print(f"Your score is **{score}**, you are alright together.")
else:
    print(f"Your score is **{score}**.")
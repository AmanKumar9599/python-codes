import random
your=int(input('Enter "0" for Rock, "1" for paper and "2" for Scissor:\n'))
print("Your choice")
if(your==0):
    print("""
    Rock-
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
elif(your==1):
    print("""
    Paper-
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
elif(your==3):
    print("""
    Scissor-
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
computer=random.randint(0,2)
print("computer choice")
if(computer==0):
    print("""
    Rock-
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
elif(computer==1):
    print("""
    Paper-
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
elif(computer==3):
    print("""
    Scissor-
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
if(your==0 and computer==2 or your==1 and computer==0 or your==2 and computer==1 ):
    print("you win")
elif(your==2 and computer==0 or your==0 and computer==1 or your==1 and computer==2 ):
    print("computer win")
else:
    print("draw")
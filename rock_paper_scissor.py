import random

user_input=input("Type 1 for rock, 2 for paper and 3 for scissor: ")
if int(user_input)==1:
    print("User choice is: Rock")
elif int(user_input)==2:
    print("User choice is: Paper")
else:
    print("User choice is: Scissor")

random_integer= random.randint(1,3)
if int(random_integer)==1:
    print("Computer choice is: Rock")
elif int(random_integer)==2:
    print("Computer choice is: Paper")
else:
    print("Computer choice is: Scissor")

if int(random_integer)==int(user_input):
    print("Tie")
elif int(random_integer)==1 and int(user_input)==2:
    print("User Wins")
elif int(random_integer)==1 and int(user_input)==3:
    print("User wins")
elif int(random_integer)==2 and int(user_input)==1:
    print("Computer wins")
elif int(random_integer)==2 and int(user_input)==3:
    print("Computer wins")
elif int(random_integer)==3 and int(user_input)==1:
    print("User wins")
else:
    print("Computer wins")
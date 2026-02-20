import random
from game_data import data

score=0
def format(option):
    option_name=option["name"]
    return f"{option_name}"

def checkans(guess, follower_1, follower_2):
    if follower_1>follower_2:
        return guess=="a"
    else:
        return guess=="b"
        
option2=random.choice(data)
should_continue=True

while should_continue:
    option1=option2
    option2=random.choice(data)
    if option1==option2:
        option2==random.choice(data)

    print(f"Compare A:{format(option1)}")
    print(f"Compare B:{format(option2)}")

    guess=input("Who has more followers A or B: ").lower()

    print("\n"*20)

    follower_1 =option1["follower_count"]
    follower_2 =option2["follower_count"]

    is_correct= checkans(guess, follower_1, follower_2)
    if is_correct:
        score+=1
        print(f"Correct guess. Current score = {score}")
    else:
        print(f"Wrong guess. Final score = {score}")
        should_continue=False
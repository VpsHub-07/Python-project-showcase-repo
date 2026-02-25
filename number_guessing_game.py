import random

def random_number():
    guess=1
    number=random.randint(1,100)
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100 ")
    choice=input("Choose a difficulty. Type 'easy' or 'hard': ")
    if choice == 'easy':
        print("You have 10 guesses to guess the number")
        guess=10
    else:
        print("You have 5 guesses to guess the number")
        guess=5
    
    while guess>0:
        user_guess=int(input("Guess the number "))
        if user_guess==number:
            print("You have guessed the correct number\nYou win!")
            break
        elif user_guess>number:
            print("You have guessed too high")
            guess-=1
            print(f"You have {guess} attempts remaining")
        elif user_guess<number:
            print("You have guessed too low")
            guess-=1
            print(f"You have {guess} attempts remaining")
    if guess==0:
        print("You exhausted your choices.\nYou lose!")
random_number()
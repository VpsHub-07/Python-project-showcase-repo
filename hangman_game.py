import random

word_list=["aardvark","baboon","camel"]
word=random.choice(word_list)
length=len(word)
print(word)

placeholder =""

while length>0:
    placeholder+="_"
    length-=1

print(placeholder)

correct_letter=[]
game_over=False
lives=6

while not game_over:
    print(f"Lives left:{lives}")
    guess=input("Guess a letter: ").lower()
    if guess in correct_letter:
        print("Letter already guessed")
    guess_word=""
    correct_guess=False 
    
    for letter in word:
        if guess==letter:
            guess_word+=guess
            correct_letter.append(guess)
        elif letter in correct_letter:
            guess_word+=letter
        else:
            guess_word+= "_"
    print(guess_word)

    if guess not in word:
        print("Wrong guess: "+guess)
        lives-=1

    if lives==0:
        print("You lose\nGame Over")
        game_over=True
    elif "_" not in guess_word:
        print("You win\nGame Over")
        game_over=True 
   
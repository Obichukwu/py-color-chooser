import random 

from hangman_guessing import guess_list
from hangman_life import lives
from hangman_life import game_name

def get_user_guess():
    unique_guess = False
    while not unique_guess:
        user_guess = input("Enter a Character: ")

        if user_guess == "":
            print("You did not enter guess.")
        elif user_guess[0].upper() in user_guesses:
            print("You have already guess that word")
        else:
            unique_guess = True

    return user_guess[0]

def print_status():
    print(lives[user_lives])

    for ch in word_to_guess:
        if ch.upper() in user_guesses:
            print(ch, end="")
        else:
            print("_", end= "")
    print("")


print(game_name)

#rand_num = random.randint(0, len(guess_list)-1)
#word_to_guess = guess_list[rand_num]
word_to_guess = random.choice(guess_list)
user_guesses = []
user_lives = 6

while user_lives > 0:
    print_status()

    user_guess = get_user_guess()

    user_guesses.append(user_guess.upper())

    if not (user_guess.upper() in word_to_guess or user_guess.lower() in word_to_guess):
        user_lives -= 1

if user_lives > 0:
    print("Yay, you won")
else:
    print_status()
    print("The word was {}".format(word_to_guess))
import random 

def print_instructions():
    print("Instruction")
    print("=======================================================")
    print("The computer would choose a colour")
    print("You are to guess the choosen colour")
    print("If your guess is correct, you win, otherwise, you lose")
    print("=======================================================")
    print("\n")

def start_game():
    global chosen_colour
    random_index = random.randint(0, len(colours)-1)
    chosen_colour = colours[random_index]

scores = {"machine": 0, "user": 0}
colours = ("Red", "Green", "Blue", "Orange", "Purple", "Yellow")
colours_str = ', '.join(colours)
chosen_colour = ""




print_instructions()

game_on = True

while game_on:
    start_game()

    for guess in range(3):
        user_guess = ""
        is_guess_valid = False
        while not is_guess_valid:
            user_guess = input("Enter your guess:")
            user_guess = user_guess.title()
            
            if (user_guess in colours):
                is_guess_valid = True
            else:
                print("You guessed an invalid colour. The acceptable colours are {}, Kindly try again.".format(colours_str))

        if (chosen_colour == user_guess):
            print("Yay, your guess was correct. You won!\n")
            break
        else:
            print("Wrong guess, try again.\n")

    if chosen_colour == user_guess:
        scores['user'] += 10
    else:
        print("The chosen colour was {}".format(chosen_colour))
        scores['machine'] += 10

    play_again = input("Do you want to play again? (Default = Yes): ")    
    if play_again.title() == "No":
        game_on = False

print("\nFinal Score")
for k, v in scores.items():
    print("{} : {}".format(k,v))

print("\nThank you for playing!")
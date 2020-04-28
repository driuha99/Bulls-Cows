# Bulls & Cows game
# Created by: Andrei Rotari
# Version: 1.0

import random
import string

# Global variables
bull = 0
cow = 0
user_win = False

# Start the game and ask the user the flow of the game
def start_game():
    # Ask user if they want play with numbers or letters
    play_method = input("Do you want to play with numbers? Y/N ")

    if play_method.lower() == "yes" or play_method.lower() == "y":
        # User wants to play with numbers tha game will generate 4 numbers next
        print("Great! Let's play with numbers: ")
        play_with_numbers()

    elif play_method.lower() == "no" or play_method.lower() == "n":
        # User wants to play with letters
        print("Great! Let's play with letters (The game is not case sensitive): ")
        play_with_letters()

    else:
        # If user introduce incorrect letters
        print("Please type: Yes or No")

        # start the game aganin for the right answer
        start_game()

    # The user choose to play with numbers


# Generate numbers and check for cows and bulls in a number range
def play_with_numbers():
    global bull, user_win, cow
    number_sequence = generate_numbers()

    while not user_win:
        user_input = input("Make a guess: ")
        # reset the count for every try
        bull = 0
        cow = 0

        if user_input == number_sequence:
            # Hooray! user won
            bull = 4
            user_win = True
        else:
            # Assign bulls and cows
            position = 0

            for number in user_input[:4]:
                if number == number_sequence[position]:
                    bull += 1
                elif number in number_sequence:
                    cow += 1

                position += 1

        # Let the user if their score if they won
        if user_win:
            print("Congrats you win!")
        else:
            print("Cows: ", cow)
            print("Bulls: ", bull)


# User choose to play with letters
# Generate letters and check for cows and bulls for letters
def play_with_letters():
    global bull, user_win, cow
    letter_sequence = generate_letters()
    
    # reset the count for every try
    bull = 0
    cow = 0

    while not user_win:
        user_input = input("Make a guess: ").lower()
        # reset the count for every try
        bull = 0
        cow = 0

        if user_input == letter_sequence:
            # Hooray! user won
            bull = 4
            user_win = True
        else:
            # Assign bulls and cows
            position = 0

            for number in user_input[:4]:
                if number == letter_sequence[position]:
                    bull += 1
                elif number in letter_sequence:
                    cow += 1

                position += 1

        # Let the user if their score if they won
        if user_win:
            print("Congrats you win!")
        else:
            print("Cows: ", cow)
            print("Bulls: ", bull)


# Generate 4 unique random numbers
def generate_numbers():
    random_number = str(random.randint(0,9))

    for i in range(3):
        unique = False
        while not unique:
            next_number = str(random.randint(0,9))
            if next_number not in random_number:
                random_number = random_number + next_number
                unique = True

    return random_number


# Generate 4 unique random letters
def generate_letters():
    random_letters = string.ascii_lowercase
    print("Generate letters")

    result = ""

    for i in range(4):
        result += random.choice(random_letters)

    return result.lower()

start_game()

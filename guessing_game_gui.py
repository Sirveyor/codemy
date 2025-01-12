# Import Tkinter
from tkinter import Button, Entry, Label, Tk

# import the os module/library
#import os
# import the random library
import random


# Create a function to ask the user Play Again?
def play_again():
    answer_yes: str = ("y", "Y", "yes", "Yes", "YES")
    again: str = input("Play Again? (Y/N): ")
    if again in answer_yes:
        game()
    else:
        print("Thank you for playing!")
    return None

# Create the main game function
def game():

    # create a variable to store the number of guesses
    number_of_guesses: int = 0
    correct: bool = False

    # Generate a random number
    number_to_guess: int = random.randint(1, 10)

    # Get user number
    print("Guess a Number from 1 to 10")

    # Creat the guessing loop
    while not correct:
        # Try/except block
        try:
            guess: str = int(input("Enter your guess: "))
        except Exception as e:
            print(f'{e} \nInput must be an integer from 1 to 10. Game Over!')

        # Create some logic to check the guess
        if guess < number_to_guess:
            results_label.config(text="Too Lo! -Try Again!")
            #increment the number of guesses
            number_of_guesses += 1
        elif guess > number_to_guess:
            results_label.config(text='Too High! - Try Again!')
            #increment the number of guesses
            number_of_guesses += 1
        else:
            #increment the number of guesses
            number_of_guesses += 1
            results_label.config(text=f"Correct! you guess it in {number_of_guesses} tries!")
            # Set correct to True
            correct = True
            # Run play_again function to see if the user wants to play again
            play_again()


def setup_gui():
    # Create a window
    root = Tk()
    # Set the title
    root.title("Guessing Game")
    # Set the size of the app
    root.geometry("500x350")

    # Create a Label
    instruction_label = Label(root, text="Guess a number from 1 to 10", font=("Helvetica", 18))
    instruction_label.pack(pady=20)

    # Create an entry box
    guess_entry = Entry(root, font=("Helvetica", 18))
    guess_entry.pack(pady=10)

    # Create another Label
    results_label = Label(root, text="")
    results_label.pack(pady=10)

    # Create some buttons
    ok_button = Button(root, text="Submit Guess")
    ok_button.pack(pady=20)

    play_button = Button(root, text="Play Again")
    play_button.pack(pady=20)
    play_button.enabled=True









    # Start the app
    root.mainloop()


# Call our main function
setup_gui()

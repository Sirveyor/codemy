# import the os module/library
import os
# import the random library
import random

# Create a function to ask the user Play Again?
def play_again():
	answer_yes = ("y", "Y", "yes", "Yes", "YES")
	again = input("Play Again? (Y/N): ")
	if again in answer_yes:
		game()
	else:
		print("Thank you for playing!")
		return


# Create the main game function
def game():

	# create a variable to store the number of guesses
	number_of_guesses = 0
	correct = False

	#Clear The Screen
	os.system("clear")

	# Generate a random number
	number_to_guess = random.randint(1, 10)

	# Get user number
	print("Guess a Number from 1 to 10")

	# Creat the guessing loop
	while not correct:
		# Try/except block
		try:
			guess = int(input("Enter your guess: "))
		except Exception as e:
			print(f'{e} \nInput must be an integer from 1 to 10. Game Over!')
			return 

		# Create some logic to check the guess
		if guess < number_to_guess:
			print("Too Lo! -Try Again!")
			#increment the number of guesses
			number_of_guesses += 1
		elif guess > number_to_guess:
			print(f'Too High! - Try Again!')
			#increment the number of guesses
			number_of_guesses += 1
		else:
			number_of_guesses += 1
			print(f"Correct! you guess it in {number_of_guesses} tries!")			# Aks user Play Again
			correct = True
			play_again()



# Call the game function
game()


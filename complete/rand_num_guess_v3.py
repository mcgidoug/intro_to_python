import random


def guess_number():
  # Generate a random number between 1 and 100
  number = random.randint(1, 100)

  # Start a loop for the guessing game
  while True:
    # Prompt the user to guess the number
    guess = int(input("Guess a number between 1 and 100: "))

    # Check if the guess is correct
    if guess == number:
      print("Congratulations! You guessed the correct number!")
      break
    # Check if the guess is too high
    elif guess > number:
      print("Too high! Try again.")
    # Check if the guess is too low
    else:
      print("Too low! Try again.")


# Start the game
guess_number()

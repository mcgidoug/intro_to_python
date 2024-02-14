import random


def guess_number():
  number = random.randint(1, 100)
  while True:
    guess = input(
        "Guess a number between 1 and 100 (type 'exit' to close program): ")
    if guess.lower() == "exit":
      print("Goodbye!")
      break
    try:
      guess = int(guess)  # Convert input to integer
      if guess == number:
        print("You got it!")
        break
      elif guess < number:
        print("Too low!")
      elif guess > number:
        print("Too high!")
    except ValueError:
      print("Invalid input. Please enter a valid number or type 'exit'.")


# Start the game
guess_number()

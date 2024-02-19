#spider word guess game

import random


def start_game():
  word_list = ["aardvark", "baboon", "camel", "dog"]
  cpu_choice = random.choice(word_list)
  guesses = 6

  for letter in cpu_choice:
    print("_", end=" ")

  while guesses > 0:
    guess = input("\nGuess a letter: ")
    if guess in cpu_choice:
      print("Correct!")
    elif guess not in cpu_choice:
      print("Incorrect!")
      guesses -= 1
      print(f"You have {guesses} guesses left.")

    if guesses == 0:
      print("Game Over.")


start_game()

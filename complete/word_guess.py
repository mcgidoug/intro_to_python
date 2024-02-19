#spider word guess game

import random


def start_game():
  word_list = ["aardvark", "baboon", "camel", "dog"]
  cpu_choice = random.choice(word_list)
  guesses = 6
  guessed_letters = []

  guessed_letters.extend("_" * len(cpu_choice))

  while guesses > 0:
    print(" ".join(guessed_letters))

    guess = input("\nGuess a letter: ")
    if guess in cpu_choice:
      print("Correct!")
      for index, letter in enumerate(cpu_choice):
        if letter == guess:
          guessed_letters[index] = guess
    elif guess not in cpu_choice:
      print("Incorrect!")
      guesses -= 1
      print(f"You have {guesses} guesses left.")

    if "_" not in guessed_letters:
      print("You win!")
      break

    if guesses == 0:
      print(f"Game Over. The word was: {cpu_choice}")


start_game()

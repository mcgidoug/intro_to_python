import random


def guess_number():
  number = random.randint(1, 100)
  guess = 0
  while True:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess == number:
      print("You got it!")
      break
    elif guess < number:
      print("Too low!")
    elif guess > number:
      print("Too high!")


guess_number()

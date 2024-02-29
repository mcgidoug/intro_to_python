import random


def scramble_word(word):
  # Convert the word to a list of characters
  chars = list(word)
  # Shuffle the characters randomly
  random.shuffle(chars)
  # Join the characters back into a string
  scrambled_word = ''.join(chars)
  return scrambled_word


# Test the function
word = input("Enter a word to scramble: ")
scrambled = scramble_word(word)
print("Scrambled word:", scrambled)

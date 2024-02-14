words = ["apple", "banana", "cherry", "orange", "grape"]
search_word = "apple"


def linear_search(words, search_word):
  try:
    index = words.index(search_word)
    print(f"The index of '{search_word}' in the list is: {index}")
  except ValueError:
    print(f"'{search_word}' is not in the list.")


linear_search(words, "dog")

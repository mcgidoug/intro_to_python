arr = [
    "the dog ran across the street", "the boy went to the store",
    "the girl went to the park"
]


def sentence_search(arr, search):
  for index, element in enumerate(arr):
    if search in element:
      print(f"Your search term was found at index: {index}")


sentence_search(arr, "the")

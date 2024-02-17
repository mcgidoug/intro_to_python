# how to use enumerate to search a user

users = ['cooper', 'shelly', 'bob', 'mike']


def find_user(users, search):
  for index, user in enumerate(users):
    if user == search:
      print(f"User: {user} is located at index: {index}")


find_user(users, "bob")

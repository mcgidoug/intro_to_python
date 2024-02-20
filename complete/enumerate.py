l1 = ["eat", "sleep", "repeat"]

# creating enumerate objects
obj1 = enumerate(l1)

print(list(enumerate(l1)))

# will print:
# [(0, 'eat'), (1, 'sleep'), (2, 'repeat')]

# ---

l1 = ["eat", "sleep", "repeat"]

# creating enumerate objects
obj1 = enumerate(l1)

for item in obj1:
  print(item)

# will print:
# (0, 'eat')
# (1, 'sleep')
# (2, 'repeat')

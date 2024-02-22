# create a new user object


class Person:

  def __init__(self, name, age, height):
    self.name = name
    self.age = age
    self.height = height


# Creating an instance of the class
person1 = Person("Doug", "34", "6")

# Convert object attributes to dictionary
person_dict = vars(person1)

# Print the dictionary
print(person_dict)

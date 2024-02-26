def generate_readme(title, description, installation, usage, license):
  readme_content = f"""# {title}

## Description
{description}

## Installation
{installation}

## Usage
{usage}

## License
{license}
"""
  with open("README.md", "w") as f:
    f.write(readme_content)


if __name__ == "__main__":
  title = input("Enter project title: ")
  description = input("Enter project description: ")
  installation = input("Enter installation instructions: ")
  usage = input("Enter usage instructions: ")
  license = input("Enter license information: ")

  generate_readme(title, description, installation, usage, license)

# ---

# import random

# def scramble_word(word):
#     # Convert the word to a list of characters
#     chars = list(word)
#     # Shuffle the characters randomly
#     random.shuffle(chars)
#     # Join the characters back into a string
#     scrambled_word = ''.join(chars)
#     return scrambled_word

# # Test the function
# word = input("Enter a word to scramble: ")
# scrambled = scramble_word(word)
# print("Scrambled word:", scrambled)

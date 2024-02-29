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

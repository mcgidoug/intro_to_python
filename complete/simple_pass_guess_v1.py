def pass_guess():
  password = ""
  while password != "1234":
    password = input("Enter the password: ")
    if password == "1234":
      print("Welcome!")


pass_guess()

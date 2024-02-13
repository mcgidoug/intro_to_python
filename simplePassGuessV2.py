def pass_guess():
  password = "1234"

  while True:
    guess = input("Enter your password or type 'stop': ").lower()
    if guess == "stop":
      print("Goodbye.")
      break
    elif guess == password:
      print("You guessed the password!")
      break
    else:
      print("Wrong password. Try again.")


pass_guess()

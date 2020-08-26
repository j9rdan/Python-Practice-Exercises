
attempt = 1
success = False

user_list = {
  "user1":"password1",
  "user2":"password2",
  "user3":"password3"
}

# checks attempt <=3 and login isn't successful
while attempt <= 3 and success == False:

  username = input("Enter your username: ")
  password = input("Enter Your Password: ")

  # password is password stored in the dictionary for that user
  if password == user_list.get(username):
    print("Sending 2FA...")
    print("265")
    number = input("Enter the code you received: ")
    #verify 2FA
    if number == "265":
      print("Welcome user")
      success = True
    else:
      print("Wrong 2FA")
  else:
    print("Incorrect login")
  # Add 1 to attempts
attempt = attempt + 1
name = input("Hello, type your name: ")
# print("Hello", name, "welcome to my game!")
print("Hello " + name + " welcome to my game!")

should_we_play = input("Do you want to play? ").lower()
# play = should_we_play == "yes"

if should_we_play == "y" or should_we_play == "yes": 
  print("We are going to play!")
  weapon = input("Choose a weapon (sword/axe): ").lower()

  direction = input("Do you want to go left or right? (left/right) ").lower()
  if direction == "left" :
    print("You went left and fell off a cliff, try again.")
  elif direction == "right":
    choice = input("Okay, you now see a bridge, do you want to swim under it or cross it? (swim/cross) ")
    if choice == "swim" and weapon == "axe":
      print("You got eaten by a shark! Game over.")
    elif choice == "swim" and weapon == "sword":
       print("You killed the shark! You win!")
    if choice == "Cross":
      print("Congrats! You won the game!")  
  else:
    print("Sorry not a valid reply, you lose!")

  
else:
  print("We are NOT playing...")
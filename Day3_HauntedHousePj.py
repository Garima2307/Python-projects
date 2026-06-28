# Build your own mini game.

# For example:

# Welcome to the AI Lab!

# Choose a door:
# 1. Red
# 2. Blue
# 3. Green

# ↓

# Different choices lead to different outcomes.

print("Welcome to the AI lab")
door = input("You reached a haunted house . "
             "Choose a door from which you want to enter into the hause -"
              " red , blue or green door\n").lower()

if door == "red":
    decision1 = input("You came across a giant box ."
          "It could be something which will help you navigate the mystery of the house."
          "Do you want to open it? - 'yes' or 'no'\n").lower()
    if decision1 == "yes":
        print('''The box suddenly opens..
              a terrifying ghost escapes!
              It screams..
              YOU DIED!''')
    else:
        print("You are saved . Congratualtions , you won!"
              "The box was having a ghost in it . Now , run to save your life!")
elif door == "blue":
    print("The ghost knocked you off . You are dead . GAME OVER!!")
elif door == "green":
    print("You bumped into the big fat ass door which was filled with nails . "
          "You died and lost the game !")
else :
    print("You lose ! You entered an invalid door and bumped yourself into it")






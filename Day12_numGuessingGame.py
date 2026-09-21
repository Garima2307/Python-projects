logo = '''
                                                    )                                 
 (                            *   )    )         ( /(                   )             
 )\ )      (     (          ` )  /( ( /(    (    )\())   (      )    ( /(    (   (    
(()/(     ))\   ))\ (   (    ( )(_)))\())  ))\  ((_)\   ))\    (     )\())  ))\  )(   
 /(_))_  /((_) /((_))\  )\  (_(_())((_)\  /((_)  _((_) /((_)   )\  '((_)\  /((_)(()\  
(_)) __|(_))( (_)) ((_)((_) |_   _|| |(_)(_))   | \| |(_))(  _((_)) | |(_)(_))   ((_) 
  | (_ || || |/ -_)(_-<(_-<   | |  | ' \ / -_)  | .` || || || '  \()| '_ \/ -_) | '_| 
   \___| \_,_|\___|/__//__/   |_|  |_||_|\___|  |_|\_| \_,_||_|_|_| |_.__/\___| |_|   

'''

import random
print(logo)
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")
level_of_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

computer_guess = random.randint(1,100)

def guessing_game(lives):
    while lives > 0:
        print(f"You have {lives} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        if guess == computer_guess:
            print(f"Yayy!! You got it right. The answer was {computer_guess}.👏🏻")
            return
        elif guess > computer_guess:
            print("Too High!")
            print("Guess again.")
        else:
            print("Too Low!")
            print("Guess again.")

        lives -= 1

    print("You have run out of guesses. You lost!😭")
    return


if level_of_difficulty == "hard":
    guessing_game(5)
else:
    guessing_game(10)


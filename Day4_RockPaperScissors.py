import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

num_chosen = int(input("What do you choose ?"
                   "Type 0 for rock , 1 for paper or 2 for scissors .\n"))
possibilities = [rock,paper,scissors]
if num_chosen >=0 and num_chosen<=2 :
    print(possibilities[num_chosen])


computer_num = random.randint(0,2)
print(f"Computer chose :\n{possibilities[computer_num]}")

if num_chosen >= 3 or num_chosen <= 0 :
    print("You typed an invalid number . You lost!")
elif num_chosen == 0 and computer_num == 2:
    print("You won!")
elif computer_num == 0 and num_chosen == 2:
    print("You lost!")
elif num_chosen == computer_num:
    print("It's a draw!")
elif num_chosen > computer_num:
    print("You won!")
elif computer_num > num_chosen:
    print("You lost!")

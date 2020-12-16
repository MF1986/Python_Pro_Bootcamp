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

#list the possibilities within a list
list_img = [rock, paper, scissors]

#get input as an integer
menu = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))

#let the computer chose a random number between 0, 1 or 2
computer = random.randint(0, 2)

#make a condition that if equal or above 3 or less than 0 then you lose.
if menu >= 3 or menu < 0:
  print("you type a wrong number, you lose!")

#else make a statement for each rules between rock, paper, scissors.
else:
  print(list_img[menu])
  print(f"You chose {menu}\n")
  print(f"computer chose {computer}")
  print(list_img[computer])

  if menu == 0 and computer == 2:
    print("you Win!")
  elif computer == 0 and menu == 2:
    print("you lose!")
  elif computer > menu:
    print("You lose!")
  elif menu > computer:
    print("You win!")
  elif computer == menu:
    print("Draw.")  

import random
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
while True:
    game_img = [rock,paper,scissors]
    user_choice=int(input("Enter your Choice: Type \n0 for Rock, \n1 for Paper, \n2 for Scissors.\n9 for Exit"))
    if user_choice==9:
       print("Thank you.....................")
       break
    elif user_choice >= 3 or user_choice < 0:
        print("Invalid Input , You Lose")
    else:
        print(game_img[user_choice])
        computer_choice=random.randint(0,2)
        print("computer Choose:")
        print(game_img[computer_choice])
        print(computer_choice)
        if computer_choice == user_choice:
            print("it's a draw")
        elif computer_choice == 0 and user_choice == 2:
            print("You lose")
        elif user_choice == 0 and computer_choice == 2:
            print("You Win")
        elif computer_choice > user_choice:
            print("You Lose")
        elif user_choice > Computer_choice:
            print("You Win")


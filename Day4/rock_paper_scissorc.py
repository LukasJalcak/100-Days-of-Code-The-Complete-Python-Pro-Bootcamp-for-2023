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
# Computer choice
list = [rock, paper, scissors]
len_list = len(list)
random_choice = random.randint(0, len_list - 1)
computer_choice = list[random_choice]

# Player choice
choise = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
player_move = list[choise]
print(player_move)



print(f"Computer choose: \n {computer_choice}")

if random_choice == player_move:
    print("draw")
else:
    print("lksajdf")
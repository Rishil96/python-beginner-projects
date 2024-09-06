# Rock Paper Scissors Game

import random
import art

user_choice = int(input("What do you want to choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0, 2)

print("You chose:\n", art.hand_signs[user_choice])
print("Computer chose:\n", art.hand_signs[computer_choice])

# Draw condition
if user_choice == computer_choice:
    print("It was a tie.")
elif ((user_choice == 1 and computer_choice == 0)
      or (user_choice == 2 and computer_choice == 1)
      or (user_choice == 0 and computer_choice == 2)):
    print("You won.")
else:
    print("You lose.")

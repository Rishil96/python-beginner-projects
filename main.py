# Treasure Island Game

print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.")

if input("You're at a cross road. Where do you want to go?\n\tType \"left\" or \"right\": ") == "left":
    if input("You arrived at a lake. Do you want to swim or wait for a boat.\n\tType \"swim\" or \"wait\": ") == "wait":
        door = input("There are 3 doors in front of you. Which one to open? Type \"red\", \"yellow\" or \"green\": ")
        if door == "red":
            print("You entered a room full of fire. Game Over.")
        elif door == "yellow":
            print("You were squished by the walls. Game Over.")
        elif door == "green":
            print("Congrats! You found the treasure. You win!")
        else:
            print("You waited long enough to activate a rolling stone trap. Game Over.")
    else:
        print("You were eaten by crocodiles. Game Over.")
else:
    print("You fell into a hole. Game Over.")

# Number Guessing Game
import random
import art


# Function to play number guessing game
def play_number_guesser():
    # Generate a number between 1 and 100 for the player to guess
    number_to_guess = random.randint(1, 100)

    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    # Set number of lives left as per difficulty level
    if difficulty == "easy":
        lives_remaining = 10
    elif difficulty == "hard":
        lives_remaining = 5
    else:
        print("Couldn't understand your difficulty option so setting it to 'easy' mode.")
        lives_remaining = 10

    # Start game
    while lives_remaining > 0:
        # Take input guess from player
        print(f"\nYou have {lives_remaining} number of attempts to guess the number.")
        guess = int(input("Make a guess: "))

        # If guess was higher than number
        if guess > number_to_guess:
            lives_remaining -= 1
            print("Too high.")
            print("Guess again.")
        elif guess < number_to_guess:
            lives_remaining -= 1
            print("Too low.")
            print("Guess again.")
        else:
            print(f"You got it. The answer was {number_to_guess}")
            break

    # Check if player lost the game
    if lives_remaining == 0:
        print(f"You've run out of guesses. The number was {number_to_guess}. You lose.")

    # Restart game: Call function recursively to play again
    restart_game = input("\nWould you like to play again? Type 'yes' or 'no': ").lower()
    if restart_game == "yes":
        play_number_guesser()
    else:
        print("Thanks for playing Guess the Number!")


if __name__ == "__main__":
    play_number_guesser()

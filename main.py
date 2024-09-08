# Hangman
import random
import art
from data import words_list


# Randomly choose a word
chosen_word = random.choice(words_list)

# Placeholder string
display = ["_"] * len(chosen_word)

# Keep track of used letters using a list, game over condition and how many lives user has
guessed_letters = []
game_over = False
has_lives_left = 6

# Welcome art
print(art.logo)

while not game_over:

    # Display placeholder
    print("*****************************")
    print(" ".join(display))

    # Ask user to guess a letter
    guess = input("Guess a letter: ").lower()
    is_letter_present = False

    # Check if user guessed a letter that was already guessed before
    if guess in guessed_letters:
        print("You've already guessed this letter.")
        continue

    # Check with the chosen word if the letter is present in the word and place it in display if it is present
    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            display[i] = guess
            is_letter_present = True
        guessed_letters.append(guess)

    # If an incorrect guess was made then reduce lives left
    if not is_letter_present:
        has_lives_left -= 1

    # Display info and hangman art on console
    print(" ".join(display))
    print(f"You have {has_lives_left} lives remaining.")
    print(art.stages[has_lives_left])

    # Game over conditions
    if "_" not in display:
        print("Congrats! You won.")
        game_over = True
    elif has_lives_left == 0:
        print(f"You have run out of lives. The correct word was \"{chosen_word}\". You lose!")
        game_over = True

print("Thanks for playing!")

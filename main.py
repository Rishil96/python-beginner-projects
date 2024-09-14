# Higher Lower Game
import random
import art
import game_data


# Function to get one data row randomly from data list
def get_random_data():
    data_point = random.choice(game_data.data)
    return data_point


# Comparison logic for follower count
def compare(data_a: dict, data_b: dict) -> str:
    follower_a = data_a.get("follower_count", 0)
    follower_b = data_b.get("follower_count", 0)
    if follower_a > follower_b:
        return "A"
    elif follower_a < follower_b:
        return "B"
    else:
        return "E"


# Play game function
def play_higher_lower():

    # Game logic
    game_over = False
    score = 0

    # Get random choices for A and B
    choice_a = get_random_data()
    choice_b = get_random_data()

    print(art.logo)

    # Start game
    while not game_over:
        # Show the 2 choices and ask for user guess
        print(f"Compare A: {choice_a["name"]}, {choice_a["description"]}, from {choice_a["country"]}.")
        print(art.vs)
        print(f"Against B: {choice_b["name"]}, a {choice_b["description"]}, from {choice_b["country"]}.\n")
        user_guess = input("Who has more followers? Type 'A' or 'B': ").upper()

        # Compare user guess with result
        result = compare(choice_a, choice_b)

        # If user guesses correctly, save B data into A and get new data point for B
        if result == "E" or user_guess == result:
            choice_a = choice_b
            choice_b = get_random_data()
            score += 1
            print(art.logo)
            print(f"You're right! Current score: {score}.")
        else:
            game_over = True
            print(f"Sorry that's wrong. Final score: {score}.")

    # Replay game
    play_again = input("\nWould you like to play again? Type 'y' or 'n': ").lower()
    if play_again == 'y':
        play_higher_lower()
    else:
        print("Thanks for playing Higher Lower!")


if __name__ == "__main__":
    play_higher_lower()

# BlackJack Capstone Project
import random
import art

# --------------------------- Useful variables and functions -------------------------- #
# Cards List
CARDS_LIST = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


# Display hand of player/computer depending on bool value
def display_hand(is_player: bool, hand: list, game_is_over: bool) -> None:
    if is_player:                               # Display hand of player
        print("Your cards:", hand, f"Current Score: {sum(hand)}")
    elif is_player and game_is_over:               # Display hand of player when game over
        print("Your final hand:", hand, f"Final Score: {sum(hand)}")
    elif not is_player and game_is_over:           # Display hand of computer when game over
        print("Computer's final hand:", hand, f"Final Score: {sum(hand)}")
    else:                                       # Display first card of computer
        print("Computer's first card:", hand[0])


# Draw card
def draw_card(hand: list) -> None:
    hand.append(random.choice(CARDS_LIST))


# Check if current player is still in game
def is_game_over(hand: list) -> bool:
    total_hand = sum(hand)
    # Handle Ace value if total hand goes over 21
    if total_hand > 21:
        if 11 in hand:
            ace_index = hand.index(11)
            hand[ace_index] = 1
        total_hand = sum(hand)
    # Return if total hand goes over 21
    return total_hand > 21


# ------------------------------- Game logic function ------------------------------- #
def play_blackjack():
    # Hands
    player_hand = []
    computer_hand = []

    # Get 2 cards for both player and computer
    for _ in range(2):
        player_hand.append(random.choice(CARDS_LIST))
        computer_hand.append(random.choice(CARDS_LIST))

    # ---------------------------- Player's turn ---------------------------#
    is_player_playing = True
    game_over = False

    while is_player_playing:
        # Display player and computer hand
        display_hand(True, player_hand, game_over)
        display_hand(False, computer_hand, game_over)

        player_choice = input("Type 'y' to get another card, type 'n' to pass: ")

        # Check if player wants to draw another card or pass to the computer
        if player_choice == 'y':
            draw_card(player_hand)
        elif player_choice == 'n':
            is_player_playing = False
        else:
            print("Invalid option... Try again.")
            continue

        # Check if player is still in game
        if is_game_over(player_hand):
            game_over = True
            is_player_playing = False
            print("\n***************")
            display_hand(True, player_hand, game_over)
            display_hand(False, computer_hand, game_over)
            print("You went over 21. You lose 😭")
            print("***************\n")

    # ------------------ Computer's turn (if not game over) -----------------#
    if not game_over:
        while sum(computer_hand) < 17:
            # Computer draws card
            draw_card(computer_hand)

            # Check if game over for computer, if yes then display hands and break out of the loop
            if is_game_over(computer_hand):
                game_over = True
                print("\n***************")
                display_hand(True, player_hand, game_over)
                display_hand(False, computer_hand, game_over)
                print("Computer went over 21. You win 😊")
                print("***************\n")
                break

    # --------------------------- Get final results ------------------------- #
    if not game_over:
        # Get total of player and computer hands
        game_over = True
        player_total = sum(player_hand)
        computer_total = sum(computer_hand)
        print("\n***************")
        print("Final Score:-")
        display_hand(True, player_hand, game_over)
        display_hand(False, computer_hand, game_over)
        if player_total > computer_total:
            print("You scored more than the dealer. You win 😊")
        elif computer_total > player_total:
            print("You scored less than the dealer. You lose 😭")
        else:
            print("It was a draw 😓")
        print("***************\n")


if __name__ == "__main__":
    # Ask user if they want to play
    play_game = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ").lower()

    # Keep restarting the game if user wants to continue playing a new round
    while play_game == 'y':
        print("\n" * 20)
        print(art.logo)
        play_blackjack()
        play_game = input("\nDo you want to play a game of BlackJack? Type 'y' or 'n': ").lower()

    print("Thanks for playing BlackJack!")

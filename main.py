# Secret Auction Program
import art

# Dictionary to hold the names and amounts of each bid
bids = {}

# Welcome poster
print(art.logo)
print("Welcome to the secret auction program.")

is_auction_on = True

# Start auction till there are bidders left
while is_auction_on:
    name = input("What's your name?: ")
    bid_amount = int(input("What's your bid?: $"))
    # Make entry of name and bid amount in dictionary
    bids[name] = bid_amount

    bidders_left = input("Are there any other bidders? Type \"yes\" or \"no\".\n")
    print("\n" * 50)

    is_auction_on = False if bidders_left == "no" else True

# Calculate the winner
highest_bid = 0
winner_name = ""

for name in bids:
    if bids[name] > highest_bid:
        winner_name = name
        highest_bid = bids[name]

# Declare winner
print(f"The winner is {winner_name} with a bid of ${highest_bid}.")

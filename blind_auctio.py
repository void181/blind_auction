from replit import clear
from art import logo

# Print the logo
print(logo)

# Initialize an empty dictionary to store the bids
auction_list = {}

# Function to add a new bid
def auction(name, bid):
    auction_list[name] = bid

# Function to find the highest bidder
def find_highest_bidder(auction_list):
    highest_bid = 0
    winner = ""
    for bidder in auction_list:
        bid_amount = int(auction_list[bidder])
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while True:
    # Get bidder's name and bid
    name = input("Enter your name: ")
    bid = input("Enter your bid: $")

    # Add the bid to the auction list
    auction(name, bid)

    # Ask if there are any other bidders
    any_other_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if any_other_bidders == "no":
        # Find and print the highest bidder
        find_highest_bidder(auction_list)
        break
    elif any_other_bidders == "yes":
        clear()

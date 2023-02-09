from silent_auction_logo import logo
import os

print(logo)

auction_active = True
auction_list = {}


print("Welcome to the secret auction program.")
count_bidders = 0

while auction_active:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    count_bidders += 1

    auction_list[name] = bid

    checking_another_bid = True
    while checking_another_bid:
        another_bid = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
        if another_bid == "yes" or another_bid == "no":
            checking_another_bid = False
        os.system("cls" if os.name == "nt" else "clear")

    if another_bid == "no":
        auction_active = False

winner = ""
amount = 0
for bidder in auction_list:
    if auction_list[bidder] > amount:
        amount = auction_list[bidder]
        winner = bidder


print(f"The winner is {winner} with a bid of ${amount}.")

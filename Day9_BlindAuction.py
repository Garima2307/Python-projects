# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


import art

print(art.logo)

user_data = {}
auction_continue = True
while auction_continue:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: "))

    user_data[name] = bid

    bidders = input("Are there any other bidders? Type 'yes or 'no'.\n")

    bid_min = 0
    var = user_data[name]
    max_bid = max(bid_min, var)

    winner_name=""
    for key, value in user_data.items():
        if value == max_bid:
            winner_name = key
            break

    if bidders == "no":
        auction_continue = False
        print(f"The winner is {winner_name} with a bid of ${max_bid}")
    else :
        print("\n" * 40)

